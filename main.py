from flask import Flask #type: ignore
from flask_login import LoginManager #type: ignore
from db.config import Config
from db.models import db, User
from route.admin_root import admin_root_bp
from route.login_root import login_bp_root
from route.public_root import public_bp_root
# from utils.add_user import add_user


app = Flask(__name__)
app.register_blueprint(admin_root_bp)
app.register_blueprint(login_bp_root)
app.register_blueprint(public_bp_root)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


login_manager = LoginManager()
login_manager.login_view = "login_bp_root.login" #type: ignore
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    
# with app.app_context():
#     condition = input("Voulez vous ajouter un utilisateur ? : (Y or N)")

#     if condition == "Y":
#         username = input("username : ")
#         name = input("name : ")
#         surname = input("surname : ")
#         email = input("email : ")
#         password = input("password : ")

#         add_user(db, username, name, surname, email, password)


    




