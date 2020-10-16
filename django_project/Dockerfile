#Imagen de Base
FROM python:3
#Visualizar logs en terminal
ENV PYTHONUNBUFFERED=1 
#Ejecuta el comando y crea la carpeta  al momento de crear la imagen
RUN mkdir /code
#Crea cerpeta de Trabajo del contendor 
WORKDIR /code
#Copia los archivos desde el .txt a la carpeta (fuera->dentro del cont.)
COPY requeriments.txt /code/
#Ejecuta el comando para instalar los requrimientos listados
RUN pip install -r requeriments.txt
#Copia contenido de carpeta actual  (fuera-dentro) del contenedor
COPY . /code/
