def index():
	response.view="inicio/LogIn.html"
	return dict(msj="")

def indexAlumno():
	response.view="inicio/LogInAlumno.html"
	return dict(msj="")

def indexProfesor():
	response.view="inicio/LogInProfesor.html"
	return dict(msj="")

def login():
	datos=request.post_vars
	usuario=db(db.Usuario.Usuario == datos.Usuario, db.Usuario.Pass == datos.Pass).select()
	if len(usuario)!=0:
		session.usuario = datos.Usuario
		session.tipo = usuario[0].Tipo
		redirect(URL('sistema','home'))
		return dict(msj="Bienvenido")

	else:
		response.view="inicio/LogIn.html"
		return dict(msj="Usuario o Contraseña invalida")

def registrar():
	response.view="inicio/Registrar.html"
	return dict()

def registroCorrecto():
	datos=request.post_vars
	db.Usuario.insert(Tipo=datos.tipoU,Usuario=datos.Usuario,Pass=datos.Pass)
	response.view="inicio/LogIn.html"
	return dict(msj="")

def cerrar():
	session.usuario = None
	response.view="inicio/LogIn.html"
	redirect("index")
	return dict()
