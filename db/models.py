from typing import Any
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

article_tags = db.Table(
    "article_tags",
    db.Column("article_id", db.String(200), db.ForeignKey("article.id"), primary_key=True),
    db.Column("tag_name", db.String(50), db.ForeignKey("tag.name"), primary_key=True)
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    
    def __init__(self, username, name, surname, email):
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    
class Tag(db.Model):
    name = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)
    
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<Tag {self.name}>"


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(200), nullable=False, unique=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Auteur (User)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    author = db.relationship('User', backref='articles')
    # Relation tags
    tags = db.relationship(
        "Tag",
        secondary=article_tags,
        backref=db.backref("articles", lazy="dynamic"),
        lazy="subquery"
    )
    
    def __init__(self, slug: str, title: str, description: str, content: str, author_id: int, tags: list) -> None:
        self.slug = slug
        self.title = title
        self.description = description
        self.content = content
        self.author_id = author_id
        self.tags = tags

    def __repr__(self):
        return f"<Article {self.slug}>"
