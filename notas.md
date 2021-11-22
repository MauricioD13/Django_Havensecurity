# Crear proyecto

Despues de la instalacion de django, se usa el comando django-admin


        django-admin startproject [nombre de proyecto] .

El punto (.) despues del comando indica donde se creara el proyecto 

### Manage.py

Archivo que tiene los comandos necesarios para interactuar con todo le proyecto de django

        python3 manage.py [comando]

# Template System
Manera de presentar los datos usando HTML
- Mayor flexibilidad
- Similitud con la sintaxis de jinja

URL -> Encargadas de encontrar el recurso
Vista -> Logica de traer los datos
Template -> Logica de presentar los datos
# Apps

Una app dentro de Django es un modulo de python que provee un conjunto de funcionalidades relacionadas entre sí.
Las apps son una combinación de models, vistas, urls, archivos estaticos.

        python3 manage.py startapp [nombre(plural)]

Se debe anotar el nombre de la nueva aplicacion en el archivo settings.py y referenciar
las vistas en el archivos urls.py
# Patrones de diseño

Patrones reutilizables para hacer codigo
MVL -> Model View Controller

Controller -> Logica del request 
Model -> Define la estructura y el acceso a los datos
View -> Como se presentan los datos

Django implementa el MTV (Model Template View)

# Migraciones

Hay cambios que se le han hecho a la base de datos en django que no se han reflejado en la base de datos actualmente

        python3 manage.py migrate

Ejecuta los cambios en la base de datos

# ORM Django (Object relational mapper)

La M de MTV
El Modelo en Django usa diferentes opciones para conectarse a múltiples bases de datos relacionales, entre las que se encuentran: SQLite, PostgreSQL, Oracle y MySQL.
Para la creación de tablas, Django usa la técnica del ORM (Object Relational Mapper), una abstracción del manejo de datos usando OOP.

ORM -> Conjunto de clases que nos permiten interactuar con la base de datos

Modelos que existen para los campos de la tabla en la db:
    https://docs.djangoproject.com/en/3.2/topics/db/models/
## Cambios en ORM

Cuando se hacen cambios en django es necesario reflejarlos en la base de datos con:

        python3 manage.py makemigrations

Posteriormente ser debe hacer:

        python3 manage.py migrate


### ***Queries y Grabar datos***
Todo esto en el archivo models.py de la aplicación
    https://docs.djangoproject.com/en/3.2/topics/db/queries/
        
**python3 manage.py shell** -> Abrir shell con las apps de django cargas
        Al entrar en el sheel se de importar la clase e usar una funcion para crear el objeto
        
    from posts.models import User
        [nombre_clase] = User.objects.create(
            email='prueba@gmail.com',
            password='12341234',
            first_name='Pablo',
            last_name='Trinidad'
        )
        
Para saber si esta en la base de datos se usa:
            
    [nombre_clase].id 
            
    [nombre_clase].pk -> De primary key
            
Si se editan los datos entonces se debe usar el método:

    [nombre_clase].save()
    
También es posible grabar datos instanciando la clase y asignarle valores a los atributos de la instancia de la clase
    - En este caso se debera usar el método .save() para que los datos se graben en al base de datos
    
**Eliminar entrada en la tabla**
    Se usa el método .delete() de la instancia

    [nombre_clase].delete()

## Queries
Documentacion: https://docs.djangoproject.com/en/3.2/topics/db/queries/
    user = User.objects.get([parametros de busqueda])
    Ej:
        user = User.objects.get(email='freddier@platzi.com')
El metodo get solo esta diseñado para traer un objeto

Querie especial

    user_object = User.objects.filter(email__endswith='@platzi.com')

Debido a que si no encuentra una entrada con las características entonces no lanzara una error ademas de que tiene otras caracteristicas de busqueda

Si se quiere determina que devuelve la clases que se obtiene de los queries entonces se define el método 

        __str__ 
        def __str__(self):
            return self.email
        
Metodo especial para actualizar un campo de la base de datos

    user_object = User.object.filter(email__endswith='@platzi.com').update(is_admin=True)

# Extendiendo el modelo de usuario

Haciendo uso del modelo user que tiene django por defecto, en el shell de django:

        from django.objects.auth.models import User
        u = User.obejct.create_user(username='yesika', password='admin123')

Las contraseñas son guardadas con su hash y no en texto plano

Creando super usuario

        python3 manage.py createsuperuser

Las opciones que Django propone para implementar Usuarios personalizados
son:

- Usando el Modelo proxy
- Extendiendo la clase abstracta de Usuario existente

La opcion de OneToOneField restringe la posibildiad de tener perfiles duplicados

Django no guarda archivos de imagen en la base de datos sino la referencia
de su ubicacion

# Dashboard de administracion


Editaremos el detalle para que sea igual de complejo que el detalle de Usuario y le agregaremos los datos del perfil para no tener que estar cambiando de urls. Usaremos fieldsets y admin.StackedInline.

En la documentación de Django, https://docs.djangoproject.com/en/2.0/ref/contrib/admin/ podemos ver cómo funcionan los fieldsets.


# Creando modelos

Para reflejar los cambios en la base de datos, siempre que se crea o se edita un modelo debemos cancelar el server, ejecutar makemigrations, migrate y luego de nuevo volver a correr el servidor con runserver.
Con respecto a las imágenes, Django por defecto no está hecho para servir la media, pero editando las urls logramos que se puedan mostrar. Para servir archivos de media, usamos MEDIA_ROOT y MEDIA_URLS.

# Templates y archivos estaticos

Los templates quedarán definidos en un nuevo folder que llamaremos /templates/.

El concepto de archivos estáticos en Django, son archivos que se usan a través de la aplicación para pintar los datos. Pueden ser archivos de imagen, audio y video, o archivos css y scripts js.

Para servir archivos estáticos, nos apoyamos en STATIC_ROOT y STATIC_URLS.

