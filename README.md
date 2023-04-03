
# Reconocimiento de Señales  ✊ ✋ 👈

En este proyecto hemos creado modelo de machine learning para poder reconocer señales que hace una persona con la mano, que indica al modelo acciones que tendrá que realizar en la plataforma de Spotify. 

Es un programa que reconoce en tiempo real la señal que estamos haciendo y realiza una acción tras reconocerla. 

![](/archives/gif.oficial.gif)


## ¿Cómo lo hemos creado?  

1.  Creamos el data Set  y creamos un CSV donde tenga las coordenadas de nuestras señales 
2.  Entrenamos el modelo y lo guardamos
3.  Creamos la App para que actue al ver una señal. 

## Paso a paso


### 1. Crear el data Set

## 1.1 Creamos las imágenes del dataset

Creamos un documento Python que nos permita tomar imágenes de diferentes señales para crear nuestro data set. Hemos creado 3 señales que representarán: 

✋ Play una canción

✊ parar la canción

👈  Cambiar de canción

Para ello utilizaremos Cv2.videoCapture que nos permite acceder a la camara del ordenador y tomar fotos. 

Una vez tomadas las fotos crearemos un CSV donde almacenaremos las coordenadas de estas fotos para poder entranar el modelo. Para crear este CSV creamos un documento llamado "Procesar_imagen" donde cambiaremos las imágenes de color además de conseguir que la imagen también cambie de dirección para poder detectar la mano contraria a la foto. 

## 1.2 Creamos un código que procese las imágenes. 

Creamos un código que procese las imágenes y mediante la librería de MediaPipe conseguiremos que nos den las coordenadas de las manos. 

https://google.github.io/mediapipe/solutions/hands.html

## 1.3 CSV que nos permita tener todas las coordenadas juntas 

Creamos un CSV que nos permita tener todas las coordenadas juntas para poder utilizarlo como modelo. 

### 2. Entrenamos el modelo

Utilizamos el modelo SVC para entrenar nuestro modelo, al haber pocas fotos y muy parecidas el modelo salió muy certero y la matriz de confusión nos sale con cero errores


### 3.Creamos la app para que actue al ver una señal. 

Utilizando la libreria de Spotipy podremos unir nuestro modelo con Spotify para que actue dependiendo de la señal que le hagamos. 

Lo primero de todo tenemos que hacer es dar acceso a la cuenta de Spotify a traves de un token para que puedan sincronizarse entre ellas. 

Creamos una app en https://developer.spotify.com/dashboard que nos va a permitir conseguir esos tokens para dar acceso a nuestra cuenta de Spotify. 

Luego abrimos la camara, y procesamos la imagen para poder realizar la predicción. Dependiendo de la señal que hagamos y gracias a nuestro modelo entrenado podremos conseguir que Spotify cambie, pare o haga play a las caciones. 

## Acknowledgements

 - [CoreCode School ](https://github.com/core-school)
 - [Daniel Alvarado](https://github.com/DanielDls-exe)
