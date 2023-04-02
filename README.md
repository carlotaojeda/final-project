
# Reconocimiento de Señales  ✊ ✋ 👈

En este proyecto hemos creado una red neuronal para poder reconocer señales que hace una persona con la mano, que indica al modelo acciones que tendrá que realizar en la plataforma de Spotify. 

Es un programa que reconoce en tiempo real la señal que estamos haciendo y realiza una acción tras reconocerla. 

<video width="640" height="480" controls>
  <source src="./videos/Ejemplo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


## ¿Cómo lo hemos creado?  

1.  Creamos el data Set  y creamos un CSV donde tenga las coordenadas de nuestras señales 
2.  Entrenamos el modelo y lo guardamos
3.  Creamos la App para que actue al ver una señal. 

## Paso a paso


### 1. Crear el data Set

Creamos un documento Python que nos permita tomar imágenes de diferentes señales para crear nuestro data set. Hemos creado 3 señales que representarán: 

✋ Play una canción

✊ parar la canción

👈  Cambiar de canción

Para ello utilizaremos Cv2.videoCapture que nos permite acceder a la camara del ordenador y tomar fotos. 

Una vez tomadas las fotos crearemos un CSV donde almacenaremos las coordenadas de estas fotos para poder entranar el modelo. Para crear este CSV creamos un documento llamado "Procesar_imagen" donde cambiaremos las imágenes de color además de conseguir que la imagen también cambie de dirección para poder detectar la mano contraria a la foto. 


### 2. Entrenamos el modelo

Utilizamos el modelo SVC para entrenar nuestro modelo, al haber pocas fotos y muy parecidas el modelo salió muy certero y la matriz de confusión nos sale con cero errores: 

FOTO MATRIZ 


### 3.Creamos la app para que actue al ver una señal. 

Utilizando la libreria de Spotipy podremos unir nuestro modelo con Spotify para que actue dependiendo de la señal que le hagamos. Lo primero de todo tenemos que hacer es dar acceso a la cuenta de Spotify a traves de un token para que puedan sincronizarse entre ellas. 

Luego abrimos la camara, y procesamos la imagen para poder realizar la predicción. Dependiendo de la señal que hagamos y gracias a nuestro modelo entrenado podremos conseguir que Spotify cambie, pare o haga play a las caciones. 


