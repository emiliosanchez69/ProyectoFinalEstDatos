from blessed import Terminal


class TrenBalaBusquedaBinaria:
    def __init__(self, term):
        self.estaciones = []
        self.term = term
        self.opciones = [
            "Agregar Estación",
            "Buscar Estación (Búsqueda Binaria)",
            "Mostrar Estaciones",
        ]
        self.opcion_actual = 0

    def header(self, text, buttons="[BACKSPACE] Volver | [ENTER] Seleccionar"):
        # Imprime el encabezado para cada pantalla
        print(self.term.clear())
        print(self.term.bold(self.term.cyan(text)))
        print()
        print(buttons)
        print("-" * 50)
        print()

    def menu(self):
        # Muestra el menú principal
        with self.term.cbreak(), self.term.hidden_cursor():
            while True:
                self.header("Sistema de Gestión del Tren Bala")
                for idx, opcion in enumerate(self.opciones):
                    prefijo = "> " if idx == self.opcion_actual else "  "
                    print(f"{prefijo}{opcion}")
                tecla = self.term.inkey()
                if tecla.code == self.term.KEY_UP:
                    self.opcion_actual = (self.opcion_actual - 1) % len(self.opciones)
                elif tecla.code == self.term.KEY_DOWN:
                    self.opcion_actual = (self.opcion_actual + 1) % len(self.opciones)
                elif tecla.name == "KEY_ENTER":
                    if not self.manejar_opcion():
                        break
                elif tecla.name == "KEY_BACKSPACE":
                    break

    def manejar_opcion(self):
        # Maneja la opción seleccionada en el menú
        opcion = self.opciones[self.opcion_actual]
        if opcion == "Agregar Estación":
            self.header("Agregar Estación")
            nombre = self.capturar_texto("Ingrese el nombre de la estación: ")
            self.agregar_estacion(nombre)
            print(f"Estación '{nombre}' agregada con éxito.")
        elif opcion == "Buscar Estación (Búsqueda Binaria)":
            self.header("Buscar Estación (Búsqueda Binaria)")
            if not self.estaciones:
                print("No hay estaciones en la línea. Agregue algunas primero.")
            else:
                nombre = self.capturar_texto("Ingrese el nombre de la estación a buscar: ")
                posicion = self.buscar_estacion(nombre)
                if posicion is not None:
                    print(f"Estación '{nombre}' encontrada en la posición {posicion + 1}.")
                else:
                    print(f"Estación '{nombre}' no encontrada.")
        elif opcion == "Mostrar Estaciones":
            self.header("Mostrar Estaciones")
            if not self.estaciones:
                print("No hay estaciones en la línea.")
            else:
                print("Estaciones en la línea (ordenadas):")
                print(" -> ".join(self.estaciones))
        self.esperar_enter()
        return True  # Continuar en el menú

    def agregar_estacion(self, nombre):
        # Agrega una estación y mantiene la lista ordenada
        self.estaciones.append(nombre)
        self.estaciones.sort()

    def buscar_estacion(self, nombre):
        # Realiza una búsqueda binaria en la lista de estaciones
        inicio = 0
        fin = len(self.estaciones) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.estaciones[medio] == nombre:
                return medio
            elif self.estaciones[medio] < nombre:
                inicio = medio + 1
            else:
                fin = medio - 1
        return None

    def capturar_texto(self, mensaje):
        # Captura texto ingresado por el usuario
        print(self.term.clear() + mensaje, end="", flush=True)
        buffer = ""
        while True:
            tecla = self.term.inkey()
            if tecla.name == "KEY_ENTER":
                return buffer.strip()
            elif tecla.name == "KEY_BACKSPACE":
                buffer = buffer[:-1]
                print(f"\r{mensaje}{buffer}{' ' * 10}", end="", flush=True)
            elif tecla.isprintable():
                buffer += tecla
                print(tecla, end="", flush=True)

    def esperar_enter(self):
        # Espera a que el usuario presione Enter
        print("\nPresione Enter para continuar...", end="", flush=True)
        while True:
            tecla = self.term.inkey()
            if tecla.name == "KEY_ENTER":
                break


if __name__ == "__main__":
    term = Terminal()
    app = TrenBalaBusquedaBinaria(term)
    app.menu()
