from flask import Blueprint, redirect, url_for
from flask_login import login_required

from route.admin.article_root import article_root_bp
from route.admin.dashboard_root import dashboard_bp_root
from route.admin.profil_root import profil_bp_root
from route.admin.user_root import user_bp_root
from route.admin.dev_root import dev_bp_root

admin_root_bp = Blueprint("admin_root", __name__, url_prefix="/admin")

admin_page = "admin/admin_page.html"

@admin_root_bp.route("/")
@login_required
def admin():
    return redirect(url_for("admin_root.dashboard_bp_root.dashboard"))
        
admin_root_bp.register_blueprint(article_root_bp)
admin_root_bp.register_blueprint(dashboard_bp_root)
admin_root_bp.register_blueprint(profil_bp_root)
admin_root_bp.register_blueprint(user_bp_root)
admin_root_bp.register_blueprint(dev_bp_root)
