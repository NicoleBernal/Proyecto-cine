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
    id_rol = SelectField("Rol", coerce=int, choices=[("0","--Rol--"),("1","Usuario")], validators=[DataRequired(message="Seleccione el rol")])
    
class comentarios(FlaskForm):
    id_comentario = StringField("id_comentario")
    comentario = TextAreaField("Comentario")
    titulo = StringField("Pelicula")
    nombre = StringField("Usuario")
    comentar = SubmitField("Enviar")

class funcion(FlaskForm):
    id_funcion = StringField("id_funcion", validators=[DataRequired("Codigo es obligatorio")])
    titulo = StringField("titulo")
    horario = StringField("horario")
    consultar=SubmitField("consultar",render_kw=({"onfocus":"cambiarRuta('/funcion/consultar')"}))
    guardar = SubmitField("guardar",render_kw=({"onfocus":"cambiarRuta('/funcion/guardar')"}))
    actualizar = SubmitField("actualizar",render_kw=({"onfocus":"cambiarRuta('/funcion/actualizar')"}))
    eliminar = SubmitField("eliminar",render_kw=({"onfocus":"cambiarRuta('/funcion/eliminar')"}))

class new(FlaskForm):
    username = StringField("Usuario")
    nombre = StringField("Nombre")
    email = StringField("Correo")
    password = PasswordField("Password")
    registrar = SubmitField("Registrar")
    id_rol = SelectField("Rol", coerce=int, choices=[("0","--Rol--"),("1","Usuario"),("2","Administrador"),("3","Superadministrador")], validators=[DataRequired(message="Campo en blanco")])

    
    