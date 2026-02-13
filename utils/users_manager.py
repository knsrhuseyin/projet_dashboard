from db.models import User, db

def create_user(username, name, surname, email, password):
    user = User(username=username, name=name, surname=surname, email=email)
    user.set_password(password)
    
    db.session.add(user)
    db.session.commit()
    
    print("ajouté")
    
    return True


def get_all_users():
    return User.query.all()