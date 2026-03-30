import crud
import crud_csv
import prueba

def menu ():
    lista_clientes = crud.cargar_datos() 
    opciones ="" 
    while opciones != "8":

        print("Marca 1 para registrar usuario")
        print("Marca 2 para mostrar usuarios")
        print("Marca 3 para buscar ususario")
        print("Marca 4 para actualizar usuario")
        print("Marca 5 para eliminar usuario")
        print("Marca 6 para guardar archivo en formato json")
        print("Marca 7 para cargar archivo en formato json")
        print("Marca 8 para cargar archivo en formato csv")
        print("Marca 9 para guardar archivo en formato csv")
        print("Marca 0 para salir del sistema")

        opciones = input("Ingrese la opcion que desea realizar: ")

        match opciones:
            case "1" :
                prueba.registrar_clientes(lista_clientes)

            case "2":
                prueba.listar_clientes(lista_clientes)

            case "3":
                prueba.buscar_clientes_por_id(lista_clientes)

            case "4":
                prueba.actualizar_info_clientes(lista_clientes)    

            case "5":    
                prueba.eliminar_cliente(lista_clientes)

            case "6":
                crud.guardar_datos(lista_clientes)
                print("Archivo guardado exitosamente en formato JSON...")

            case "7":
                lista_clientes = crud.cargar_datos()      
                print("Archivo cargado exitosamente en formato JSON...")

            case "8":
                lista_clientes = crud_csv.cargar_datos_csv()
                print("Archivo cargado exitosamente en formato CSV...")    

            case "9":
                lista_clientes = crud_csv.guardar_clientes_csv(lista_clientes)
                print("Archivo guardado exitosamente en formato CSV...")

            case "0":
                print("Saliendo del sistema...")
                break


if __name__ == "__main__":
    menu()







