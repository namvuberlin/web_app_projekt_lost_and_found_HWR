# db.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  
    is_admin = db.Column(db.Boolean, default=False)

    
    matriculation_number = db.Column(db.String(50), unique=True, nullable=True)
    email = db.Column(db.String(200), unique=True, nullable=True)


class ItemPost(db.Model):
    __tablename__ = "item_posts"

    id = db.Column(db.Integer, primary_key=True)
    post_type = db.Column(db.String(10), nullable=False) 
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

    location = db.Column(db.String(200))
    status = db.Column(db.String(20), default="open")  

    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    creator = db.relationship("User", backref="posts")


class PostInterest(db.Model):
   
    __tablename__ = "post_interests"

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("item_posts.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    message = db.Column(db.Text, nullable=True)  # optional
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    post = db.relationship("ItemPost", backref="interests")
    user = db.relationship("User", backref="interests")


class AppSettings(db.Model):
    
    __tablename__ = "app_settings"

    id = db.Column(db.Integer, primary_key=True)
    station_name = db.Column(db.String(200), default="Lost & Found Station")
    contact_email = db.Column(db.String(200), default="lostfound@hwr-berlin.de")
