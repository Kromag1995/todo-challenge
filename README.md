# Requerimientos
Esto fue creado usadon python 3.8.7 con django 3.1.5.

# Modelos
Se creo un modelo ToDo. El mismo esta asocidado a un usuario, tiene un titulo y texto, tiene un valor booleano que indica si esta completado o no y tiene un timestamp que indica cuando fue creado.

# Views
La view principal es allTodo, en la misma se muestran todos los ToDo's relacionados con el usuario creado.
Se puede crear nuevos ToDo's con un titulo, text y si lo decea especificar el timestamp (Esto es para propositos de verificar el correcto funcionamiento del programa). No se pueden crear ToDos sin titulo.
Tambien se tiene la posibilidad de filtrar los resultados segun el titulo, texto, se puede especificar un rango de fechas creadas de los todos. Si se indican solo una fecha se indicara se excluye todo lo anterior, para la primera fecha, o todo lo posterior para la segunda (por ejemplo si solo se indicara la segunda fecha siendo 19/01/2021 excluiria todos los todos creados despues de esa fecha).
Para cada ToDo se tiene un boton check/uncheck que permite marcar una tarea como completada, o desmarcarla si se lo desea. Tambien cada Todo tiene un boton para borrarse.

La view de addTodo se encarga de crear un ToDo. Si se pasa un fecha entonces se toma esa fecha como la fecha de creacion del todo.

La view de deleteTodo elimina el todo correspondiente.

La view de checkTodo marca el todo correspondiente como completado/sin completar segun corresponda.

Se creo una app con views para registro/login/logout de usuario para que se pueda probar los ToDos con diferentes usuarios.

# Como levantar la apliacion

Desde la carpeta main donde se encuentra el archivo manage.py  correr python manage.py runserver y dirirse a localhost:8000/singin. De ahi se creara un usuario y luego se redireccionara a /allTodo/ (caso de ejemplo username: Test1234, email: Test1234@testmail.com, password: Contraseña23).