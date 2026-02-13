import json
from typing import Any

from flask import flash, request

from db.forms import ArticleForm
from db.models import Tag, Article, User
from utils.tags_manager import add_tag, get_page_tags
from utils.utils import generate_unique_slug

def delete_article_by_id(slug: str, db) -> bool:
    article = db.session.get(Article, slug)
    if article:
        db.session.delete(article)
        db.session.commit()
        return True
    return False


def add_article_to_database(slug, title, description, content, author_id, tags, db):
    article = Article(
            slug=slug,
            title=title,
            description=description,
            content=content,
            author_id=author_id,
            tags=tags
        )
    
    db.session.add(article)
    db.session.commit()


def add_article_to_database_with_form(form: ArticleForm, current_user, db):
    if form.validate_on_submit():
        slug = generate_unique_slug(form.title.data, Article)
        title = form.title.data
        description = form.description.data
        content = form.content.data
        author_id = current_user.id
        
        print(request.form.get("tags_json", "[]"))
        if request.form.get("tags_json", "[]"):
            tags = json.loads(request.form.get("tags_json", "[]"))
        else:
            tags = False
        tags_sql = []

        # ➕ nouveau tag
        if tags:
            for tag in tags:
                name = tag.strip().lower()
                tags_sql.append(add_tag(name, db))

        add_article_to_database(slug, title, description, content, author_id, tags_sql, db)
        print("committed")

        flash("Article publié ✅", "success")


    
    


def edit_article(article: Any, form: ArticleForm, db):
    tags = get_page_tags(request)
    tags_sql = []

    if tags:
        for tag in tags:
            name = tag.strip().lower()
            tag_obj = Tag.query.filter_by(name=name).first()

            if not tag_obj:
                tag_obj = Tag(name=name)  # type: ignore
                db.session.add(tag_obj)

            tags_sql.append(tag_obj)

    # 🔹 Mise à jour des champs
    if article.title != form.title.data:
        new_slug = generate_unique_slug(form.title.data, Article, article.slug)
        if new_slug != article.slug:
            article.slug = new_slug
    article.title = form.title.data
    article.description = form.description.data
    article.content = form.content.data
    article.tags = tags_sql  # remplace complètement les tags

    db.session.commit()
    flash("Article modifié ✏️", "success")


def get_all_article(db):
    return db.session.query(
        Article,
        User.name.label("author_name")
    ).join(User, Article.author_id == User.id).all()
    

def get_article_number():
    return Article.query.count()

