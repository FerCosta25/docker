#!/bin/bash

# Borra todas las imagenes sin etiqueta
docker image prune -a

#Borras todos los contenedores detenidos
docker container prune 

# Borras los volumenes no utilizados 
docker volume prune 

# Borra todas las imagenes, contenedores y volúmenes no utilizados 
docker system prune 

# Borra el caché de compilación de docker 
docker builder prune 