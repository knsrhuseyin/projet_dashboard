
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from db.forms import CreateUserForm

from utils.users_manager import get_all_users, create_user


user_bp_root = Blueprint("user_bp_root", __name__, url_prefix="/user")

admin_page = "admin/admin_page.html"

@user_bp_root.route("/")
@login_required
def users():
    users_data = get_all_users()
    return render_template(admin_page,
                           page="admin/content/users/users.html", 
                           users="bg-blue-500 text-white",
                           users_content="text-cyan-400",
                           title="Users", 
                           users_data=users_data,
                           current_user=current_user
                           )
    

@user_bp_root.route("/add_user", methods=["GET", "POST"])
@login_required
def add_user():
    form = CreateUserForm()
    errors_data = {}
    form.errors.clear()
    
    if not form.validate():
            if form.errors:
                for field, errors in form.errors.items():
                    for error in errors:
                        print(f"Error in field '{field}': {error}")
                        if field != "csrf_token":
                            if field == "username":
                                if error != "This field is required.":
                                    errors_data[field] = {"message": error, "field": field, "category": "danger"}
                            elif field == "email":
                                if error != "This field is required.":
                                    if error == "Invalid email address.":
                                        errors_data[field] = {"message": "L'adresse email n'est pas valide.", "field": field, "category": "danger"}
                                    else:
                                        errors_data[field] = {"message": error, "field": field, "category": "danger"}
                            elif field == "confirm_password":
                                if error != "This field is required.":
                                    errors_data[field] = {"message": error, "field": field, "category": "danger"}
                        
    
    if form.validate_on_submit():
        creation = create_user(
            username=form.username.data,
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            password=form.password.data
        )
        
        print(creation)
        
        return redirect(url_for('admin_root.user_bp_root.add_user'))
    
    return render_template(admin_page,
                           page="admin/content/users/add_user.html", 
                           users="bg-blue-500 text-white",
                           add_users_content="text-cyan-400", 
                           title="Add User",
                           errors=errors_data,
                           form=form
                           )
    