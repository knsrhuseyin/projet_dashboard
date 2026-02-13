import re

from flask import flash
from flask_login import login_user

from db.forms import LoginForm
from db.models import User


def authenticate_user(form: LoginForm) -> bool:
    if form.is_submitted() and not form.validate():
        flash("Saisi invalide", "danger")
        return False
        
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return True
        else:
            flash("Email ou mot de passe incorrect", "danger")
            return False
        
    return False


def add_user(db, username, name, surname, email, password):
    user = User(username=username, name=name, surname=surname, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    
    
def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

    
    
def generate_unique_slug(title, Article_table, slug_of_article=None):
    base_slug = slugify(title)
    slug = base_slug
    counter = 2
    
    while True:
        existing = Article_table.query.filter_by(slug=slug).first()
        
        if not existing or existing.slug == slug_of_article:
            break


        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug
