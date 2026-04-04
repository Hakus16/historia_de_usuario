from servicios import agregar_producto,mostrar_inventario,buscar_producto,actualizar_producto,eliminar_producto,calcular_estadisticas,cargar_csv,integrar_inventario

from archivos import guardar_csv

def main():
    inventario=[]
    sw=True
    while sw is not False:

        print("\n--- MENÚ ---")
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")
        



        option=input("seleccione una opcion: ")

        if not option.isdigit() or int(option) < 1 or int(option) > 9:
            print("Opción inválida.")
            continue
        
        try:
            if option == "1":
                nombre=input("ingrese nombre del producto : ")
                precio=float(input("ingrese el precio: "))
                cantidad=int(input("ingrese la cantidad: "))
                agregar_producto(nombre,precio,cantidad,inventario)

            elif option == "2":
                mostrar_inventario(inventario)
            
            elif option == "3":
                nombre=input("ingresar nombre del producto ")
                resultado=buscar_producto(inventario,nombre)
                print("el resultado es", resultado)

            elif option == "4":
                nombre=input("ingrese nombre del producto: ")
                precio=float(input("ingrese el precio: "))
                cantidad=int(input("ingrese la cantidad: "))
                actualizado=actualizar_producto(inventario,nombre,precio if precio else None,cantidad if cantidad else None)
                
                print("actualizado" if actualizado else "producto no encontrado")

            elif option == "5":
                nombre = input("nombre del producto a eliminar: ")
                eliminado = eliminar_producto(inventario,nombre)
                print("eliminado" if eliminado else "producto no encontrado")

            elif option == "6":
                stats = calcular_estadisticas(inventario)

                print("\n--- ESTADÍSTICAS ---")
                print(f"Unidades totales: {stats['unidades_totales']}")
                print(f"Valor total del inventario: ${stats['valor_total']:.2f}")

                if stats["producto_mas_caro"]:
                    print(f"Producto más caro: {stats['producto_mas_caro']['nombre']} "
                        f"(${stats['producto_mas_caro']['precio']})")

                if stats["producto_mayor_stock"]:
                    print(f"Producto con mayor stock: {stats['producto_mayor_stock']['nombre']} "
                        f"({stats['producto_mayor_stock']['cantidad']} unidades)")


            elif option == "7":
                guardar_csv(inventario,"inventario.csv")
            
            elif option =="8":
             
               inventario = integrar_inventario(
                inventario,"C:/Users/RYZEN/OneDrive/Escritorio/programacion/inventario.csv")
            
            elif option == "9":
                sw = False
                break

   


            else:
                print("opción invalida")
                break
            
            
        

                
                    



                
            
        except ValueError:
            print("Error, intente nuevamente")




        


main()