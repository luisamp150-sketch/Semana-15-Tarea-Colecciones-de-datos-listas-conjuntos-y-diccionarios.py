# Programa de Gestión de Inventario para una Tienda
# Utiliza un diccionario para almacenar productos y sus precios.

def mostrar_menu():
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Agregar o actualizar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar un producto")
    print("4. Eliminar un producto")
    print("5. Salir")

def gestionar_inventario():
    # Diccionario para almacenar el inventario (Clave: nombre_producto, Valor: precio)
    inventario = {
        "Manzana": 0.250,
        "Leche": 1.20,
        "Pan": 0.30,
        "Chocolate": 0.50
    }
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            # Operación: Insertar / Agregar datos
            nombre = input("Ingresa el nombre del producto: ").capitalize()
            try:
                precio = float(input(f"Ingresa el precio de {nombre}: "))
                inventario[nombre] = precio
                print(f"¡Producto '{nombre}' guardado exitosamente!")
            except ValueError:
                print("Error: Por favor, ingresa un número válido para el precio.")
                
        elif opcion == "2":
            # Operación: Mostrar / Recorrer elementos
            if not inventario:
                print("El inventario está vacío.")
            else:
                print("\n--- LISTA DE PRODUCTOS ---")
                for producto, precio in inventario.items():
                    print(f"- {producto}: ${precio:.2f}")
                    
        elif opcion == "3":
            # Operación adicional: Buscar elementos
            nombre = input("¿Qué producto deseas buscar?: ").capitalize()
            if nombre in inventario:
                print(f"¡Encontrado! El precio de {nombre} es ${inventario[nombre]:.2f}")
            else:
                print(f"El producto '{nombre}' no se encuentra en el inventario.")
                
        elif opcion == "4":
            # Operación adicional: Eliminar elementos
            nombre = input("¿Qué producto deseas eliminar?: ").capitalize()
            if nombre in inventario:
                del inventario[nombre]
                print(f"El producto '{nombre}' ha sido eliminado del inventario.")
            else:
                print(f"El producto '{nombre}' no existe en el inventario.")
                
        elif opcion == "5":
            print("¡Gracias por usar el sistema de inventario! Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")

# Punto de entrada del programa
if __name__ == "__main__":
    gestionar_inventario()
