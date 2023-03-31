from dotenv import load_dotenv
import os
load_dotenv()
import spotipy 
from procesado_live import procesar_img
import cv2 
import numpy as np
import pickle
separator = os.path.sep
path_act = os.path.dirname(os.path.abspath(__file__))
dir = separator.join(path_act.split(separator)[:-1])

with open(f'{dir}/modelo/modelo.pkl', 'rb') as f:
    model = pickle.load(f)


client_id =os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

url = "http://localhost:8889/callback"
scope = "user-modify-playback-state user-read-playback-state"
oauth_object = spotipy.SpotifyOAuth(client_id, client_secret, url, scope=scope)
token = oauth_object.get_access_token(as_dict=False)

sp = spotipy.Spotify(auth=token)
# Inicializa la cámara
cap = cv2.VideoCapture(0)

# Inicializar la última predicción como una cadena vacía
last_prediction = ''

cv2.namedWindow ("camara", cv2.WINDOW_AUTOSIZE)


# Ciclo principal para obtener los frames de la cámara
while True:
    # Lee el siguiente frame de la cámara
    ret, frame = cap.read()

    # Si el frame se leyó correctamente, procesa la imagen y realiza la predicción
    if ret:
        data = procesar_img(frame) #devuelve los puntos de la imagen del video
        
        # Comprobar si la mano está presente
        if data != None:
            data = np.array(data) #convierte en array
            y_pred = model.predict(data.reshape(-1,63)) #pasamos el modelo para que haga la predicción
            
            # Comprobar si la nueva predicción es diferente a la última predicción
            if y_pred[0] != last_prediction:
                print(y_pred[0])
                try:
                
                    # Si la predicción es "pausa", pausa la reproducción de la canción
                    if str(y_pred[0]) == "pausa":
                        sp.pause_playback()
                    
                    # Si la predicción es "play", reanuda la reproducción de la canción
                    elif str(y_pred[0]) == "play":
                        sp.start_playback()
                    
                    # Si la predicción es "siguiente", pasa a la siguiente canción
                    elif str(y_pred[0]) == "siguiente":
                        sp.next_track()
                    
                    last_prediction = y_pred[0]
                except spotipy.SpotifyException as e:
                    print ("Error:", str (e))

        fuente = cv2.FONT_HERSHEY_SIMPLEX
        posicion = (50,100)
        font_size = 3
        color = (0,0,0)
        grosor = 5

        frame_actual = cv2.putText(frame,last_prediction,posicion, fuente, font_size,color, grosor, cv2.LINE_AA)
        cv2.imshow("cámara", frame_actual)
    if cv2.waitKey (1) == 113:
        break
cap.release()
cv2.destroyAllWindows()









