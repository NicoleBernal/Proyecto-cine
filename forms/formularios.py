from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired("Usuario es obligatorio")])
    password = PasswordField("Password", validators=[DataRequired("Password es obligatorio")])
    enviar = SubmitField ("Iniciar sesion") 
    
class Registro(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired("Usuario es obligatorio")])
    nombre = StringField("Nombre", validators=[DataRequired("Nombre es obligatorio")])
    email = StringField("Correo", validators=[DataRequired("Correo es obligatorio")])
    password = PasswordField("Password", validators=[DataRequired("Password es obligatorio")])
    id_rol = SelectField("Rol", coerce=int, choices=[("0","--Escoja una opción--"),("1","Usuario"),("2","Administrador"),("3","Superadministrador")], validators=[DataRequired(message="Rol es obligatorio")])
    registrar = SubmitField("Registrar")

class Comentarios(FlaskForm):
    id_comentario = SelectField("ID comentario", coerce=int, choices=[("0","--Edite las opciones--")], validators=[DataRequired("ID comentario es obligatorio")])
    comentario = TextAreaField("Comentario", validators=[DataRequired("Comentario es obligatorio")])
    titulo = StringField("Pelicula", validators=[DataRequired("Nombre de la pelicula es obligatorio")])
    nombre = StringField("Nombre", validators=[DataRequired("Nombre es obligatorio")])
    comentar = SubmitField("Enviar")


    
    