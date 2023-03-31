import cv2

# Función para procesar la imagen y realizar la predicción
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

    if output.multi_hand_landmarks is None:
        # Si no se detectan manos, devolver None
        return None

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

         # Si ocurre una excepción, devolver None

        return None
    
