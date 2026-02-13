from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from db.models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Mot de passe", validators=[DataRequired()])
    submit = SubmitField("Connexion")
    

class ArticleForm(FlaskForm):
    title = StringField(
        "Titre",
        validators=[DataRequired(), Length(min=3, max=200)]
    )

    description = TextAreaField(
        "Description",
        validators=[DataRequired(), Length(min=10, max=100)]
    )
    
    content = TextAreaField(
        "Contenu",
        validators=[DataRequired(), Length(min=10)]
    )

    tags = SelectMultipleField(
        "Tags",
        coerce=str,
    )
    
    new_tag = StringField("Nouveau tag")

    submit = SubmitField("Publier l'article")
    
    
class CreateUserForm(FlaskForm):
    username = StringField(
        "Nom d'utilisateur",
        validators=[DataRequired(), Length(min=3, max=150)]
    )
    
    name = StringField(
        "Prénom",
        validators=[DataRequired(), Length(max=150)]
    )
    
    surname = StringField(
        "Nom",
        validators=[DataRequired(), Length(max=150)]
    )
    
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(), Length(max=150)]
    )
    
    password = PasswordField(
        "Mot de passe",
        validators=[DataRequired(), Length(min=6)]
    )
    
    confirm_password = PasswordField(
        "Confirmer le mot de passe",
        validators=[
            DataRequired(),
            EqualTo("password", message="Les mots de passe doivent correspondre.")
        ]
    )

    submit = SubmitField("Créer l'utilisateur")

    # Vérification unicité username
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Ce nom d'utilisateur existe déjà.")

    # Vérification unicité email
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Cet email est déjà utilisé.")