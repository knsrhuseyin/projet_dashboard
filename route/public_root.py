from flask import Blueprint, render_template # type: ignore
from route.public.actualite_root import actualite_bp_root

from db.models import Article

public_bp_root = Blueprint("public_bp_root", __name__, url_prefix="/")
public_bp_root.register_blueprint(actualite_bp_root)

@public_bp_root.route("/")
def root():
    articles = Article.query \
        .order_by(Article.created_at.desc()) \
        .paginate(page=1, per_page=10)

    return render_template("public/index.html", 
                           items=["Collège", "Lycée", "Rentrée", "Prépa", "Orientation", "Terminale"],
                           articles=articles)