# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from db import db, User, ItemPost, PostInterest, AppSettings

app = Flask(__name__)

app.config["SECRET_KEY"] = "dev-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# ----------------------------
# DECORATORS
# ----------------------------
def login_required(f):
    from functools import wraps

    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return wrapper


def admin_required(f):
    from functools import wraps

    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session or not session.get("is_admin"):
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)

    return wrapper


def get_settings():
    settings = AppSettings.query.first()
    if not settings:
        settings = AppSettings()
        db.session.add(settings)
        db.session.commit()
    return settings


@app.route("/")
def index():
    if "user_id" in session:
        if session.get("is_admin"):
            return redirect(url_for("admin_dashboard"))
        return redirect(url_for("student_dashboard"))
    return redirect(url_for("login"))


# ----------------------------
# AUTH
# ----------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""

        matriculation_number = (request.form.get("matriculation_number") or "").strip()
        email = (request.form.get("email") or "").strip()

        if not username or not password:
            error = "Bitte Username und Passwort eingeben."
        elif not matriculation_number or not email:
            error = "Bitte Matrikelnummer und HWR Email eingeben."
        elif User.query.filter_by(username=username).first():
            error = "Username existiert bereits."
        elif User.query.filter_by(matriculation_number=matriculation_number).first():
            error = "Matrikelnummer existiert bereits."
        elif User.query.filter_by(email=email).first():
            error = "Email existiert bereits."
        else:
            user = User(
                username=username,
                password=password,
                is_admin=False,
                matriculation_number=matriculation_number,
                email=email,
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("login"))

    return render_template("auth/register.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""

        user = User.query.filter_by(username=username, password=password, is_admin=False).first()
        if user:
            session["user_id"] = user.id
            session["username"] = user.username
            session["is_admin"] = False
            return redirect(url_for("student_dashboard"))

        error = "Login falsch."

    return render_template("auth/login.html", error=error)


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    error = None

    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""

        admin = User.query.filter_by(username=username, password=password, is_admin=True).first()
        if admin:
            session["user_id"] = admin.id
            session["username"] = admin.username
            session["is_admin"] = True
            return redirect(url_for("admin_dashboard"))

        error = "Admin Login falsch."

    return render_template("auth/admin_login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ----------------------------
# ADMIN
# ----------------------------
@app.route("/admin/dashboard")
@admin_required
def admin_dashboard():
    total_posts = ItemPost.query.count()
    open_posts = ItemPost.query.filter_by(status="open").count()
    claimed_posts = ItemPost.query.filter_by(status="claimed").count()
    closed_posts = ItemPost.query.filter_by(status="closed").count()
    student_users = User.query.filter_by(is_admin=False).count()

    settings = get_settings()

    return render_template(
        "admin/dashboard.html",
        total_posts=total_posts,
        open_posts=open_posts,
        claimed_posts=claimed_posts,
        closed_posts=closed_posts,
        student_users=student_users,
        settings=settings,
    )


@app.route("/admin/posts")
@admin_required
def admin_posts():
    q = (request.args.get("q") or "").strip()
    post_type = (request.args.get("type") or "").strip().lower()
    status = (request.args.get("status") or "").strip().lower()

    query = ItemPost.query

    if q:
        like = f"%{q}%"
        query = query.filter(
            (ItemPost.title.ilike(like))
            | (ItemPost.description.ilike(like))
            | (ItemPost.location.ilike(like))
        )

    if post_type in ("lost", "found"):
        query = query.filter_by(post_type=post_type)

    if status in ("open", "claimed", "closed"):
        query = query.filter_by(status=status)

    posts = query.order_by(ItemPost.created_at.desc()).all()

    return render_template("admin/posts.html", posts=posts, q=q, filter_type=post_type, filter_status=status)


@app.route("/admin/posts/new", methods=["GET", "POST"])
@admin_required
def admin_posts_new():
    error = None

    if request.method == "POST":
        post_type = (request.form.get("post_type") or "").strip().lower()
        title = (request.form.get("title") or "").strip()
        description = (request.form.get("description") or "").strip()
        location = (request.form.get("location") or "").strip()
        status = (request.form.get("status") or "open").strip().lower()

        if post_type not in ("lost", "found"):
            error = "Please choose Lost or Found."
        elif not title or not description:
            error = "Title and description are required."
        elif status not in ("open", "claimed", "closed"):
            error = "Invalid status."
        else:
            post = ItemPost(
                post_type=post_type,
                title=title,
                description=description,
                location=location or None,
                status=status,
                created_by=session["user_id"],
            )
            db.session.add(post)
            db.session.commit()
            return redirect(url_for("admin_posts"))

    return render_template("admin/post_form.html", mode="new", error=error, post=None)


@app.route("/admin/posts/<int:post_id>/edit", methods=["GET", "POST"])
@admin_required
def admin_posts_edit(post_id: int):
    post = ItemPost.query.get(post_id)
    if not post:
        return redirect(url_for("admin_posts"))

    error = None

    if request.method == "POST":
        post_type = (request.form.get("post_type") or "").strip().lower()
        title = (request.form.get("title") or "").strip()
        description = (request.form.get("description") or "").strip()
        location = (request.form.get("location") or "").strip()
        status = (request.form.get("status") or "open").strip().lower()

        if post_type not in ("lost", "found"):
            error = "Please choose Lost or Found."
        elif not title or not description:
            error = "Title and description are required."
        elif status not in ("open", "claimed", "closed"):
            error = "Invalid status."
        else:
            post.post_type = post_type
            post.title = title
            post.description = description
            post.location = location or None
            post.status = status
            db.session.commit()
            return redirect(url_for("admin_posts"))

    return render_template("admin/post_form.html", mode="edit", error=error, post=post)


@app.route("/admin/posts/<int:post_id>/delete", methods=["POST"])
@admin_required
def admin_posts_delete(post_id: int):
    post = ItemPost.query.get(post_id)
    if not post:
        return redirect(url_for("admin_posts"))

    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("admin_posts"))


@app.route("/admin/users")
@admin_required
def admin_users():
    users = User.query.order_by(User.id.asc()).all()
    return render_template("admin/users.html", users=users)


@app.route("/admin/users/<int:user_id>/delete", methods=["POST"])
@admin_required
def admin_user_delete(user_id: int):
    user = User.query.get(user_id)
    if not user:
        return redirect(url_for("admin_users"))

    if user.is_admin:
        return redirect(url_for("admin_users"))

    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("admin_users"))


@app.route("/admin/settings", methods=["GET", "POST"])
@admin_required
def admin_settings():
    settings = get_settings()
    error = None

    if request.method == "POST":
        station_name = (request.form.get("station_name") or "").strip()
        contact_email = (request.form.get("contact_email") or "").strip()

        if not station_name or not contact_email:
            error = "Bitte Station Name und Contact Email ausfüllen."
        else:
            settings.station_name = station_name
            settings.contact_email = contact_email
            db.session.commit()
            return redirect(url_for("admin_settings"))

    return render_template("admin/settings.html", settings=settings, error=error)


# ----------------------------
# STUDENT
# ----------------------------
@app.route("/student/dashboard")
@login_required
def student_dashboard():
    user_id = session["user_id"]

    my_posts = (
        ItemPost.query
        .filter_by(created_by=user_id)
        .order_by(ItemPost.created_at.desc())
        .all()
    )

    my_open = ItemPost.query.filter_by(created_by=user_id, status="open").count()
    my_total = ItemPost.query.filter_by(created_by=user_id).count()

    now = datetime.utcnow()
    start_of_week = datetime(now.year, now.month, now.day) - timedelta(days=now.weekday())

    my_post_ids = [p.id for p in my_posts]

    if my_post_ids:
        weekly_interests = (
            PostInterest.query
            .filter(PostInterest.post_id.in_(my_post_ids))
            .filter(PostInterest.created_at >= start_of_week)
            .order_by(PostInterest.created_at.desc())
            .all()
        )
    else:
        weekly_interests = []

    weekly_messages_count = len(weekly_interests)

    return render_template(
        "student/dashboard.html",
        my_posts=my_posts,
        my_open=my_open,
        my_total=my_total,
        weekly_interests=weekly_interests,          
        weekly_messages_count=weekly_messages_count 
    )

@app.route("/student/lost")
@login_required
def student_lost():
    posts = ItemPost.query.filter_by(post_type="lost").order_by(ItemPost.created_at.desc()).all()
    return render_template("student/lost.html", posts=posts)


@app.route("/student/found")
@login_required
def student_found():
    posts = ItemPost.query.filter_by(post_type="found").order_by(ItemPost.created_at.desc()).all()
    return render_template("student/found.html", posts=posts)


@app.route("/student/post/new", methods=["GET", "POST"])
@login_required
def student_new_post():
    error = None

    if request.method == "POST":
        post_type = (request.form.get("post_type") or "").strip().lower()
        title = (request.form.get("title") or "").strip()
        description = (request.form.get("description") or "").strip()
        location = (request.form.get("location") or "").strip()

        if post_type not in ("lost", "found"):
            error = "Please choose Lost or Found."
        elif not title or not description:
            error = "Title and description are required."
        else:
            post = ItemPost(
                post_type=post_type,
                title=title,
                description=description,
                location=location or None,
                status="open",
                created_by=session["user_id"],
            )
            db.session.add(post)
            db.session.commit()

            return redirect(url_for("student_lost" if post_type == "lost" else "student_found"))

    return render_template("student/post_form.html", mode="new", error=error, post=None)


@app.route("/student/post/<int:post_id>")
@login_required
def student_post_detail(post_id: int):
    post = ItemPost.query.get(post_id)
    if not post:
        return redirect(url_for("student_dashboard"))

    creator = post.creator 

    interests = (
        PostInterest.query
        .filter_by(post_id=post.id)
        .order_by(PostInterest.created_at.desc())
        .all()
    )

    settings = get_settings()

    return render_template(
        "student/post_detail.html",
        post=post,
        creator=creator,
        interests=interests,
        settings=settings
    )


@app.route("/student/post/<int:post_id>/respond", methods=["POST"])
@login_required
def student_post_respond(post_id: int):
    post = ItemPost.query.get(post_id)
    if not post:
        return redirect(url_for("student_dashboard"))

    existing = PostInterest.query.filter_by(post_id=post_id, user_id=session["user_id"]).first()
    if existing:
        return redirect(url_for("student_post_detail", post_id=post_id))

    message = (request.form.get("message") or "").strip()

    interest = PostInterest(
        post_id=post_id,
        user_id=session["user_id"],
        message=message or None
    )
    db.session.add(interest)
    db.session.commit()

    return redirect(url_for("student_post_detail", post_id=post_id))


@app.route("/student/post/<int:post_id>/edit", methods=["GET", "POST"])
@login_required
def student_edit_post(post_id: int):
    post = ItemPost.query.get(post_id)
    if not post:
        return redirect(url_for("student_dashboard"))

    if post.created_by != session["user_id"]:
        return redirect(url_for("student_dashboard"))

    error = None

    if request.method == "POST":
        title = (request.form.get("title") or "").strip()
        description = (request.form.get("description") or "").strip()
        location = (request.form.get("location") or "").strip()

        if not title or not description:
            error = "Title and description are required."
        else:
            post.title = title
            post.description = description
            post.location = location or None
            db.session.commit()
            return redirect(url_for("student_dashboard"))

    return render_template("student/post_form.html", mode="edit", error=error, post=post)


@app.route("/student/post/<int:post_id>/delete", methods=["POST"])
@login_required
def student_delete_post(post_id: int):
    post = ItemPost.query.get(post_id)
    if not post:
        return redirect(url_for("student_dashboard"))

    if post.created_by != session["user_id"]:
        return redirect(url_for("student_dashboard"))

    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("student_dashboard"))


@app.route("/student/messages")
@login_required
def student_messages():
    """
    Inbox: zeigt alle Meldungen (Interests) auf eigene Posts
    """
    user_id = session["user_id"]
    my_post_ids = [p.id for p in ItemPost.query.filter_by(created_by=user_id).all()]

    if not my_post_ids:
        interests = []
    else:
        interests = (
            PostInterest.query
            .filter(PostInterest.post_id.in_(my_post_ids))
            .order_by(PostInterest.created_at.desc())
            .all()
        )

    return render_template("student/messages.html", interests=interests)


@app.route("/student/profile")
@login_required
def student_profile():
    user = User.query.get(session["user_id"])
    return render_template("student/profile.html", user=user, settings=get_settings())



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        admin_user = User.query.filter_by(username="admin").first()
        if not admin_user:
            admin_user = User(username="admin", password="admin", is_admin=True)
            db.session.add(admin_user)
            db.session.commit()
            print(">>> Admin erstellt: username='admin', password='admin'")

        get_settings()

    app.run(debug=True)
