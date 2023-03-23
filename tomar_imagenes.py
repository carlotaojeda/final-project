import numpy as np
import cv2 
from pathlib import Path


def tomar_imagenes ():
    acciones = input ("Como deseas llamar esta accion: ")
    Path("dataset/" + acciones).mkdir(parents=True,exist_ok=True)
    video = cv2.VideoCapture(0)
    iterador = 0
    while True:
        _,imagen = video.read()
        iterador+=1
        if iterador%5 ==0:
            cv2.imwrite(f"dataset/{acciones}/{iterador}.jpg",imagen)
        cv2.imshow("imagen",imagen)
        if cv2.waitKey(1)== 113 or iterador>500:
            break
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__": 
    tomar_imagenes()