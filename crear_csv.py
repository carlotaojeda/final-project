import os
from procesar_imagen import procesar

def crear_csv():
    """
    Función que recorre los archivos de una carpeta 'dataset', procesa cada imagen y crea un archivo CSV 
    con los datos de las imágenes procesadas. Cada línea del archivo CSV contiene los puntos de referencia 
    detectados y la etiqueta de la imagen.
    """
    carpeta = 'dataset'
    archivo_csv = open('dataset.csv', 'a')

    # Recorre cada carpeta de la carpeta 'dataset'
    for carpeta_sub in os.listdir(carpeta):
        # Ignora archivos ocultos
        if '._' in carpeta_sub:
            pass
        else:
            # Recorre cada archivo de la carpeta sub
            for archivo in os.listdir(carpeta + '/' + carpeta_sub):
                # Ignora archivos ocultos
                if '._' in archivo:
                    pass
                else:
                    etiqueta = carpeta_sub

                    # Localiza el archivo de imagen y la procesa
                    ubicacion_archivo = carpeta + '/' + carpeta_sub + '/' + archivo
                    datos_imagen = procesar(ubicacion_archivo)

                    try:
                        # Escribe los puntos de referencia de la imagen en el archivo CSV
                        for id, i in enumerate(datos_imagen):
                            if id == 0:
                                print(i)
                            archivo_csv.write(str(i))
                            archivo_csv.write(',')

                        # Escribe la etiqueta de la imagen en el archivo CSV
                        archivo_csv.write(etiqueta)
                        archivo_csv.write('\n')
                    
                    # Si hay un error al procesar la imagen, escribe ceros en el archivo CSV
                    except:
                        archivo_csv.write('0')
                        archivo_csv.write(',')
                        archivo_csv.write('None')
                        archivo_csv.write('\n')

    # Cierra el archivo CSV
    archivo_csv.close()
    print('CSV creado')

if __name__ == "__main__":
    crear_csv()