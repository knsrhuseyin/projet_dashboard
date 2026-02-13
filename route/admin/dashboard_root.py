from flask import Blueprint, render_template
from flask_login import login_required, current_user
from utils.article_manager import get_article_number

admin_page = "admin/admin_page.html"

dashboard_bp_root = Blueprint("dashboard_bp_root", __name__, url_prefix="/dashboard")


@dashboard_bp_root.route("/")
@login_required
def dashboard():
    return render_template(admin_page, 
                           page="admin/content/dashboard.html", 
                           dashboard="bg-blue-500 text-white", 
                           title="Dashboard", 
                           current_user=current_user, 
                           article_count=get_article_number()
                           )
    