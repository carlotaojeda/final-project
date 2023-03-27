import cv2
import pickle
import pickle

# Carga el modelo previamente entrenado
with open('modelo.pkl', 'rb') as file:
    model = pickle.load(file)


# Función para procesar la imagen y realizar la predicción
import cv2
import mediapipe as mp
import numpy as np 

def procesar_img(frame):
    # Procesar imagen
    # 1. Convertir de BGR a RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 2. Mueve la imagen al ege Y
    img_flip = cv2.flip(img_rgb, 1)

    # Acceso a MediaPipe de manos
    mp_hands = mp.solutions.hands

    # Inicializar Hands
    hands = mp_hands.Hands(static_image_mode=True,
    max_num_hands=1, min_detection_confidence=0.7)

    # Resultados
    output = hands.process(img_flip)

    hands.close() # Cerramos Mediapipe porque ya no lo necesitamos

    try:

        #Limieza de los datos

        data = output.multi_hand_landmarks[0]

        data = str(data)

        data = data.strip().split('\n')

        delete = ['landmark {', '}']

        keep = []

        for i in data:
            if i not in delete:
                keep.append(i)

        clean = []

        for i in keep:
            i = i.strip()
            clean.append(i[2:])

        for i in range(0, len(clean)):
            clean[i] = float(clean[i])

        return(clean)

    except:

         # Sino devuelve un array de los puntos de la imagen

        return(np.zeros([1,63], dtype=int)[0])

# Inicializa la cámara
cap = cv2.VideoCapture(0)

# Ciclo principal para obtener los frames de la cámara
while True:
    # Lee el siguiente frame de la cámara
    ret, frame = cap.read()

    # Si el frame se leyó correctamente, procesa la imagen y realiza la predicción
    if ret:
        data = procesar_img(frame) #devuelve los puntos de la imagen del video
        data = np.array(data) #convierte en array
        y_pred = model.predict(data.reshape(-1,63)) #pasamos el modelo para que haga la predicción
        print(y_pred)

    # Si se presiona la tecla 'q', sale del ciclo
    if cv2.waitKey(1) == ord('q'):
        break

# Libera los recursos
cap.release()
cv2.destroyAllWindows()