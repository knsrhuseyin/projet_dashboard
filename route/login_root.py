from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required, logout_user

from db.forms import LoginForm
from utils.utils import authenticate_user

login_bp_root = Blueprint("login_bp_root", __name__, url_prefix="/")


@login_bp_root.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if authenticate_user(form):
        return redirect(url_for("admin_root.dashboard_bp_root.dashboard"))

    return render_template("admin/login.html", form=form)

@login_bp_root.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login_bp_root.login"))