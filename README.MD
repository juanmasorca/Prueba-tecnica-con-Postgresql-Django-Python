Micro servicio el cual es capaz de insertar, actualizar, borrar y consultar (CRUD) información utilizando el FrameWork de Django,
Este micro servicio es capaz de interactuar con una DB de tipo POSTGRESQL, además de esto, el servicio se corre mediante un contenedor en docker
el cual esta disponible en el puerto 1234.

Informacion de importancia:

* Es necesario tener instalado: Python, Pip, Django, Docker, PostgreSQL, Editor de codigo

* "Dockerfile" -> Se encuentran las instrucciones que se utilizan para construir una imagen de Docker

* "requirements.txt" -> Se encuantran las librerias necesarias para un funcionamiento correcto del programa

* "docker-compose.yml" -> Define los servicios que se ejecutarán en contenedores, en este caso se tienen los servicios de la base de datos y la pagina web
    Datos variables dentro de "docker-compose.yml"
        POSTGRES_USER -> Usuario de PostgreSQL
        POSTGRES_PASSWORD: -> Contraseña de PostgreSQL
        POSTGRES_DB: -> Base de datos a la cual se desea conectar

        ports:
        - "5432:5432"
        donde el dato antes de ":" es el puerto de la base de datos, y el segundo dato es el puerto del host

        command: python manage.py runserver 0.0.0.0:1234  -> Define el comando para ejecutar la aplicación web



* "/djangocrud/settings.py" -> Contiene la configuracion para la conexion a la base de datos y las app usadas
    DATABASES = {
        'default': {
            'ENGINE' -> servicio con el cual se va a correr la base de datos
            'NAME' -> Nombre de la base de datos
            'USER' -> usuario
            'PASSWORD' -> Contraseña
            'HOST' -> Termianl a cual se desea conectar
            'PORT' -> Puerto de la DB
        }
    }

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<nombre de la app>',
    ]

*"/djangocrud/url.py"
    Agregar los url usados en la app
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('<nombre de la app>.urls'))
]

Comandos importantes:

    Crear entorno virtual:
    virtualenv venv   
    venv/Scripts/activate


    pip install django -> Instalar Django

    pip install psycopg2 -> Instalar psycopg2     

    django-admin startproject <Nombre de la Proyecto> .  -> Crear Proyecto
    
    python manage.py startapp <Nombre de la app> -> Crear App

    pip install psycopg2 -> conexion a PostgreSQL

    pip freeze > requirements.txt -> Crear archivo "requirements.txt

    crear tablas en db sin docker
    python manage.py makemigrations
    python manage.py migrate

    python manage.py runserver <puerto>   -> Iniciar programa sin docker

    Comandos para realizar la migracion de tablas con docker 
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate

    docker-compose up --build  -> Correr Programa mediante Docker
