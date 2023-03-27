
# Reconocimiento de Señales  ✊ ✋ 👌 👈

En este proyecto hemos creado una red neuronal para poder reconocer señales que hace una persona con la mano, que indica al modelo acciones que tendrá que realizar en la plataforma de Spotify. 

Es un programa que reconoce en tiempo real la señal que estamos haciendo y realiza una acción tras reconocerla. 

## ¿Cómo lo hemos creado?  

1.  Creamos el data Set  y creamos un CSV donde tenga las coordenadas de nuestras señales 
2.  Entrenamos el modelo y lo guardamos
3.  Linkeamos el modelo con la API para que pueda funcionar con Spotify y actue. 

## Paso a paso


### 1. Crear el data Set

Creamos un documento Python que nos permita tomar imágenes de diferentes señales para crear nuestro data set. Nosotros creamos 4 señales que representarán: 

✋ Abrir la aplicación

👌 Pausar una canción

✊ reanudar la canción

👈  Cambiar de canción

Para ello utilizaremos Cv2.videoCapture que nos permite acceder a la camara del ordenador y tomar fotos. 

Una vez tomadas las fotos crearemos un CSV donde almacenaremos las coordenadas de estas fotos para poder entranar el modelo. 


### 2. Entrenamos el modelo


