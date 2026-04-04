

import csv


def guardar_csv(inventario,ruta,incluir_header=True):

# validar que haya datos
    if not inventario:
        print(" no hay datos en el inventario para guardar.")
        return
    
    try:
       
        # 🔹 Abrir archivo en modo escritura
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            # 🔹 Escribir encabezado
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            # 🔹 Escribir filas
            for producto in inventario:
                writer.writerow([
                    producto["nombre"],
                    producto["precio"],
                    producto["cantidad"]
                ])

        print(f" Inventario guardado en: {ruta}")

    except PermissionError:
        print(" Error: No tienes permisos para escribir en esa ubicación.")

    except OSError as e:
        print(f" Error al guardar el archivo: {e}")