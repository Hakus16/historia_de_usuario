def agregar_producto(nombre:str,precio:float,cantidad:int,inventario):
    producto={
      "nombre": nombre, 
      "precio": precio,
      "cantidad": cantidad
    }

    inventario.append(producto)

def mostrar_inventario(inventario):

    if not inventario:
        print("esta vacia")

    for producto in inventario:
        print(f"nombre: {producto["nombre"]}, precio {producto["precio"]}, cantidad {producto["cantidad"]}")

def buscar_producto(inventario, nombre):
    
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def actualizar_producto(inventario,nombre,nuevo_precio=None,nueva_cantidad=None):
    resultado=buscar_producto(inventario,nombre)
    
    if resultado is None:
        return False
    
    if nuevo_precio is not None:
        resultado["precio"] = nuevo_precio

    if nueva_cantidad is not None:
        resultado["cantidad"]= nueva_cantidad

    return True

def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario,nombre)

    if producto:
        inventario.remove(producto)
        return True
    return False

def calcular_estadisticas(inventario):
    if not inventario:
        return {
            "total_productos": 0,
            "valor_total": 0,
            "producto_mas_caro": None,
            "producto_mas_barato": None

        }
    # lambda opcional para calcular subtotal

    subtotal = lambda p: p["precio"] * p["cantidad"]

    # calculos

    unidades_totales = sum (p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)

    producto_mas_caro = max(inventario,key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario,key=lambda p: p["precio"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro":{
            "nombre": producto_mas_caro["nombre"],
            "precio": producto_mas_caro["precio"]
        },
        "producto_mayor_stock": {
            "nombre": producto_mayor_stock["nombre"],
            "cantidad": producto_mayor_stock["cantidad"]
        }
    }


import csv

def cargar_csv(ruta):
    productos = []
    errores = 0

    try:
        with open(ruta, newline='', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            encabezado = next(reader, None)

            # Validar encabezado
            if encabezado != ["nombre", "precio", "cantidad"]:
                print(" Encabezado inválido. Debe ser: nombre,precio,cantidad")
                return []

            for fila in reader:
                # Validar columnas
                if len(fila) != 3:
                    errores += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    productos.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except ValueError:
                    errores += 1

        return productos, errores

    except FileNotFoundError:
        print(" Archivo no encontrado.")
    except UnicodeDecodeError:
        print(" Error de codificación del archivo.")
    except Exception as e:
        print(f" Error inesperado: {e}")

    return [], 0




def integrar_inventario(inventario_actual, ruta):
    nuevos_productos, errores = cargar_csv(ruta)

    if not nuevos_productos:
        print(" No se cargaron productos.")
        return inventario_actual

    opcion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()

    if opcion == "S":
        print(" Inventario reemplazado.")
        inventario_final = nuevos_productos
        accion = "reemplazo"

    elif opcion == "N":
        print(" Fusionando inventario...")
        print(" Política: suma cantidades y actualiza precio si cambia.")

        inventario_dict = {p["nombre"]: p for p in inventario_actual}

        for prod in nuevos_productos:
            nombre = prod["nombre"]

            if nombre in inventario_dict:
                inventario_dict[nombre]["cantidad"] += prod["cantidad"]

                if inventario_dict[nombre]["precio"] != prod["precio"]:
                    inventario_dict[nombre]["precio"] = prod["precio"]
            else:
                inventario_dict[nombre] = prod

        inventario_final = list(inventario_dict.values())
        accion = "fusión"

        print(" Fusión completada.")

    else:
        print(" Opción inválida.")
        return inventario_actual

    # Resumen final
    print("\n RESUMEN:")
    print(f"Productos cargados: {len(nuevos_productos)}")
    print(f"Filas inválidas omitidas: {errores}")
    print(f"Acción realizada: {accion}")

    return inventario_final








    
