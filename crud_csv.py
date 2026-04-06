import csv
import os



ARCHIVO_DATA1 = "producto_csv.csv"

def cargar_datos_csv ():
    if not os.path.exists(ARCHIVO_DATA1):
        return []
    
    try: 
        with open(ARCHIVO_DATA1, mode="r",  encoding='utf-8') as f:
            #
            lector = csv.DictReader(f)
            for fila in lector:
                lista_producto.append(fila)
        print("Datos cargardos")
    except FileNotFoundError:
        print("el archivo no existe")
    return lista_producto        


def guardar_producto_csv(lista_producto):
    ARCHIVO_DATA1

    nombres_columnas = lista_producto[0].keys()

    with open(ARCHIVO_DATA1, mode='w', newline='',encoding='utf-8')as f:
        escritor = csv.DictWriter(f,fieldnames= nombres_columnas)

        escritor.writeheader()
        escritor.writerows(lista_producto)

    print(f"datos guardados{ARCHIVO_DATA1}")
    
        
