import crud


def registrar_producto(lista_producto):
   
    while True:
        try:
            cant_producto = int(input("escriba la cantidad de producto a ingresar: "))
            
            if cant_producto<=0:
                print("ingrese un numero positivo")
                continue
            break
            
        except ValueError:
            print("solo se admiten numeros")

       
    for producto in range(cant_producto):
        print(f"\nRegistro del cliente {producto+1}")
          
        productos = {

                "id": int(input("Ingrese el ID del producto: ")),
                "nombre": input("Ingrese el nombre del producto: "),
                "cantidad": int(input("Ingrese la cantidad del producto: ")),
                "precio": float(input("Ingrese el precio del producto: "),
         
                }
        
        lista_producto.append(productos)
        crud.guardar_datos(lista_producto)
        
    print(f"Esta es la informacion de los clientes, {lista_producto}")


def listar_producto(lista_producto):

    for i,  producto in enumerate(lista_producto, start=1):
        print(f"El producto numero {i} es: Su nombre es {producto["nombre"]}, el id es {producto["id"]} ,la cantidad es {producto["cantidad"]}, su precio es {producto["precio"]}")


def buscar_producto_por_id(lista_producto):
    """Ingresar el numero de ID del cliente que necesita buscar"""
    try:
        id_producto_buscar = int(input("Ingrese el ID del producto a buscar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return 

    for producto in lista_producto:
        if producto.get("id") == id_producto_buscar:
            print(f"El cliente con ID {id_producto_buscar} es: {producto}")
            return producto
        
    print(f"No se encontró ningún cliente con ID {id_producto_buscar}.")
    return 


def actualizar_info_producto (lista_producto):

    try:
        id_producto_actualizar = int(input("Ingrese el ID del producto para actualizar informacion: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return 
    
    encontrado = False
    for producto in lista_producto:
        if producto.get("id") == id_producto_actualizar:          
            producto["cantidad"] = input("Ingrese la nueva cantidad del producto: ")  # Actualiza el valor directamente
            print(f"El producto con ID {id_producto_actualizar} cambio de cantidad: {producto['cantidad']}")
            crud.guardar_datos(lista_producto)
            encontrado = True
            break
    if not encontrado:
        print("producto no encontrado.")

        
    return


def eliminar_producto (lista_producto):   

    try:
        id_producto_para_eliminar = int(input("Ingrese el ID del producto para actualizar informacion: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return 
    
   
    for producto in lista_producto:
        #te elimina el objeto cliente
        if producto.get("id") == id_producto_para_eliminar: 
            lista_producto.remove(producto) #elimino el cliente por medio del id
            print(f"producto con ID {id_producto_para_eliminar} eliminado.")
            print(f"La lista de producto actualizada es: {lista_producto}")
            crud.guardar_datos(lista_producto)
            break
        else:
            print("No se encontró ningún producto con ese ID.")


    return 

