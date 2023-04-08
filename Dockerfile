#Este archivo contiene una serie de instrucciones que se utilizan para construir una imagen de Docker. 
FROM python:3.9

# Se establece una variable de entorno para asegurarse de que la salida de la aplicación sea inmediatamente visible
ENV PYTHONUNBUFFERED 1

# Se establece el directorio de trabajo para la aplicación
WORKDIR /app

# Se copia el archivo requirements.txt al directorio de trabajo y se instalan las dependencias necesarias
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Se copian todos los archivos y directorios del directorio actual al directorio de trabajo
COPY . /app/

# Se establece el comando predeterminado para la imagen Docker, que ejecuta la aplicación Django en el puerto 1234
CMD ["python", "manage.py", "runserver", "0.0.0.0:1234"]
