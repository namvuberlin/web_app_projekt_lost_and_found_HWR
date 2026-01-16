from flask import Flask, render_template, request, redirect, url_for, session
from db import db


app = Flask(__name__)

app.config['SECRET_KEY'] = 'dev-key'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  
    is_admin = db.Column(db.Boolean, default=False)



def login_required(f):
    from functools import wraps

    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return wrapper


def admin_required(f):
    from functools import wraps

    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session or not session.get('is_admin'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)

    return wrapper




@app.route('/')
def index():
    """Startseite leitet je nach Rolle weiter."""
    if 'user_id' in session:
        if session.get('is_admin'):
            return redirect(url_for('admin_dashboard'))
        return redirect(url_for('student_dashboard'))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        existing = User.query.filter_by(username=username).first()
        if existing:
            error = "Username existiert bereits."
        else:
            user = User(username=username, password=password, is_admin=False)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))

    return render_template('auth/register.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(
            username=username,
            password=password,
            is_admin=False
        ).first()

        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            session['is_admin'] = False
            return redirect(url_for('student_dashboard'))
        else:
            error = "Login falsch."

    return render_template('auth/login.html', error=error)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        admin = User.query.filter_by(
            username=username,
            password=password,
            is_admin=True
        ).first()

        if admin:
            session['user_id'] = admin.id
            session['username'] = admin.username
            session['is_admin'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            error = "Admin Login falsch."

    return render_template('auth/admin_login.html', error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/student/dashboard')
@login_required
def student_dashboard():
    return render_template('student/dashboard.html')

@app.route('/student/lost')
@login_required
def student_lost():
    return render_template('student/lost.html')

@app.route('/student/post/new')
@login_required
def student_new_post():
    return render_template('student/new_post.html')


@app.route('/student/found')
@login_required
def student_found():
    return render_template('student/found.html')

@app.route('/student/profile')
@login_required
def student_profile():
    return render_template('student/profile.html')


@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/posts')
@admin_required
def admin_posts():
    return render_template('admin/posts.html')

@app.route('/admin/users')
@admin_required
def admin_users():
    return render_template('admin/users.html')

@app.route('/admin/settings')
@admin_required
def admin_settings():
    return render_template('admin/settings.html')




if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        admin_user = User.query.filter_by(username="admin").first()
        if not admin_user:
            admin_user = User(
                username="admin",
                password="admin",
                is_admin=True
            )
            db.session.add(admin_user)
            db.session.commit()
            print(">>> Admin erstellt: username='admin', password='admin'")

    app.run(debug=True)
