from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required, current_user

from db.forms import ArticleForm
from db.models import Article, Tag, db
from utils.article_manager import add_article_to_database_with_form, edit_article, delete_article_by_id, get_all_article

article_root_bp = Blueprint("article_root", __name__, url_prefix="/article")

admin_page = "admin/admin_page.html"

@article_root_bp.route("/")
@login_required
def article_page():
    articles = get_all_article(db)
    print(articles)
    return render_template(admin_page,
                           page="admin/content/articles/articles.html",
                           article="bg-blue-500 text-white rounded-b-none",
                           article_content="text-cyan-400",
                           title="Article",
                           current_user=current_user,
                           articles=articles)


@article_root_bp.route("/add_article", methods=["GET", "POST"])
@login_required
def add_article():
    form = ArticleForm()

    form.tags.choices = [t.name for t in Tag.query.order_by(Tag.name).all()]

    if request.method == "POST":
        add_article_to_database_with_form(form, current_user, db)
        return redirect(url_for('admin_root.article_root.add_article'))

    return render_template(admin_page,
                           page="admin/content/articles/add_article.html",
                           article="bg-blue-500 text-white rounded-b-none",
                           add_article_content="text-cyan-400",
                           title="Article",
                           current_user=current_user,
                           form=form
                           )


@article_root_bp.route("/edit/<string:slug>", methods=["GET", "POST"])
@login_required
def modify_article(slug: str):
    form = ArticleForm()

    form.tags.choices = [t.name for t in Tag.query.order_by(Tag.name).all()]

    article_editing = Article.query.filter_by(slug=slug).first_or_404()
    print(article_editing)

    if request.method == "GET":
        form.title.data = article_editing.title
        form.description.data = article_editing.description
        form.content.data = article_editing.content
        form.submit.label.text = "Mettre à jour l'article"
        form.tags.data = [tag.name for tag in article_editing.tags]

    if form.validate_on_submit():
        edit_article(article_editing, form, db)
        return redirect(url_for("admin_root.article_root.article_page"))

    return render_template(admin_page,
                           page="admin/content/articles/edit_article.html",
                           article_content="text-cyan-400",
                           article="bg-blue-500 text-white rounded-b-none",
                           title="Modifier l'article",
                           current_user=current_user,
                           form=form,
                           tags_json=form.tags.data,
                           edit_article=article_editing
                           )


@article_root_bp.post("/delete/<string:slug>")
@login_required
def delete_article(slug: str):
    delete_article_by_id(slug, db)
    return redirect("/admin/article")