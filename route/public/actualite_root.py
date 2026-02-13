from pprint import pprint
import markdown
from flask import Blueprint, render_template, request #type: ignore
from markupsafe import Markup


from db.models import Article

actualite_bp_root = Blueprint("actualite_bp_root", __name__, url_prefix="/actualites")

@actualite_bp_root.route("/")
def actualite():
    page = request.args.get("page", 1, type=int)  # page=1 par défaut
    
    articles = Article.query \
        .order_by(Article.created_at.desc()) \
        .paginate(page=page, per_page=9)
    
    return render_template("public/actualite.html", 
                           items=["Collège", "Lycée", "Rentrée", "Prépa", "Orientation", "Terminale"],
                           numero="1",
                           articles=articles)
    
@actualite_bp_root.route("/<string:slug>")
def show_article(slug):
    article = Article.query.filter_by(slug=slug).first_or_404()
    
    article_html = Markup(markdown.markdown(
        article.content,
        extensions=[
            "extra",                    # tableaux, html mixé
            "codehilite",               # blocs de code stylés
            "toc",                      # ids sur titres
            "pymdownx.tasklist",        # ✅ CHECKBOXES
            "pymdownx.superfences",     # meilleurs blocs code
        ],
        extension_configs={
            "pymdownx.tasklist": {
                "clickable_checkbox": False
            }
        }
    ))
        
    return render_template("public/article_detail.html", article_html=article_html, article=article, back_url=request.referrer)