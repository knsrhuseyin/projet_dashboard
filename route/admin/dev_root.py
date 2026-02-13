from flask import Blueprint, render_template
from flask_login import login_required, current_user
from db.models import Article, Tag, db

admin_page = "admin/admin_page.html"

dev_bp_root = Blueprint("dev_bp_root", __name__, url_prefix="/dev")


@dev_bp_root.route("/")
@login_required
def dev_root():
    return render_template(admin_page, 
                           page="admin/content/dev.html", 
                           dev="bg-blue-500 text-white", 
                           title="Dev", current_user=current_user)
    

@dev_bp_root.route("/delete-article-db")
@login_required
def delete_article_db():
    Article.query.delete()
    db.session.commit()
    
    return render_template("admin/content/success_page.html")

@dev_bp_root.route("/delete-tags-db")
@login_required
def delete_tags_db():
    Tag.query.delete()
    db.session.commit()
    
    return render_template("admin/content/success_page.html")