import cv2
import mediapipe as mp
import numpy as np


def procesar (ruta):
    mano_foto= cv2.imread(ruta)
    mano_RGB = cv2.cvtColor(mano_foto,cv2.COLOR_BGR2RGB)
    mano_flip = cv2.flip(mano_RGB,1)
    mediapipe_manos = mp.solutions.hands 
    manos = mediapipe_manos.Hands(static_image_mode=True,
    max_num_hands=1, min_detection_confidence=0.7)
    resultado = manos.process(mano_flip)
    manos.close ()
    try:
        # Extraer el primer landmark de mano detectado
        data = resultado.multi_hand_landmarks[0]

        # Imprimir los puntos de referencia de la mano detectada
        print(data)

        # Convertir los landmarks de mano en una cadena
        data = str(data)

        # Quitar los saltos de línea y dividir la cadena por línea
        data = data.strip().split('\n')

        # Los strings a eliminar de la lista
        delete = ['landmark {', '}']

        # Lista para mantener las líneas que no están en 'delete'
        keep = []

        # Iterar sobre cada línea de 'data'
        for i in data:
            # Si la línea no está en 'delete', agregarla a 'keep'
            if i not in delete:
                keep.append(i)

        # Lista para mantener los landmarks limpios
        clean = []

        # Iterar sobre cada línea de 'keep'
        for i in keep:
            # Eliminar los espacios en blanco al principio y al final de la línea
            i = i.strip()
            # Eliminar los primeros dos caracteres ('x:' o 'y:')
            clean.append(i[2:])

        # Convertir los landmarks limpios a valores de punto flotante
        for i in range(0, len(clean)):
            clean[i] = float(clean[i])

        # Devolver los landmarks limpios
        return(clean)

# Si no se detectó ninguna mano, devolver una lista de ceros
    except:
        return(np.zeros([1,63], dtype=int)[0])
    
if __name__ == "__main__":
    procesar()




