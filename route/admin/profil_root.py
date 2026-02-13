
from flask import Blueprint, render_template
from flask_login import current_user, login_required


profil_bp_root = Blueprint("profil_bp_root", __name__, url_prefix="/profil")

admin_page = "admin/admin_page.html"

@profil_bp_root.route("/")
@login_required
def current_user_profil():
    return render_template(admin_page, 
                           page="admin/content/profil.html", 
                           profil="bg-blue-500 text-white", 
                           title="Profil", user=current_user)
    