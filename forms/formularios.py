from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired("Usuario es obligatorio")])
    password = PasswordField("Password", validators=[DataRequired("Password es obligatorio")])
    enviar = SubmitField ("Iniciar sesion") 
    
class Registro(FlaskForm):
    username = StringField("Usuario")
    nombre = StringField("Nombre")
    email = StringField("Correo")
    password = PasswordField("Password")
    registrar = SubmitField("Registrar")
    id_rol = SelectField("Rol", coerce=int, choices=[("0","--Rol--"),("1","Usuario"),("2","Administrador"),("3","Superadministrador")], validators=[DataRequired(message="Campo en blanco")])

class comentarios(FlaskForm):
    id_comentario = StringField("id_comentario")
    comentario = TextAreaField("Comentario")
    titulo = StringField("Pelicula")
    nombre = StringField("Usuario")
    comentar = SubmitField("Enviar")


    
    