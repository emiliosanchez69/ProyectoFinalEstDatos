from blessed import Terminal


class TrenBalaQuicksort:
    def __init__(self, term):
        self.estaciones = []
        self.term = term
        self.opciones = [
            "Agregar Estación",
            "Ordenar Estaciones (Quicksort)",
            "Mostrar Estaciones",
        ]
        self.opcion_actual = 0

    def menu(self):
        # Muestra el menú principal
        with self.term.cbreak(), self.term.hidden_cursor():
            while True:
                self.header("Sistema de Gestión del Tren Bala - Ordenamiento Quicksort")
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
        # Maneja las opciones seleccionadas en el menú
        opcion = self.opciones[self.opcion_actual]
        if opcion == "Agregar Estación":
            self.header("Agregar Estación")
            nombre = self.capturar_texto("Ingrese el nombre de la estación: ")
            self.estaciones.append(nombre)
            print(f"Estación '{nombre}' agregada con éxito.")
        elif opcion == "Ordenar Estaciones (Quicksort)":
            self.header("Ordenar Estaciones (Quicksort)")
            if not self.estaciones:
                print("No hay estaciones en la lista. Agregue algunas primero.")
            else:
                print("Estaciones antes de ordenar:")
                print(" -> ".join(self.estaciones))
                self.estaciones = self.quicksort(self.estaciones)
                print("\nEstaciones ordenadas correctamente.")
        elif opcion == "Mostrar Estaciones":
            self.header("Mostrar Estaciones")
            if not self.estaciones:
                print("No hay estaciones en la lista.")
            else:
                print("Estaciones en la lista:")
                print(" -> ".join(self.estaciones))
        self.esperar_enter()
        return True

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

    def quicksort(self, lista):
        # Implementación del algoritmo Quicksort
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[len(lista) // 2]
            menores = [x for x in lista if x < pivote]
            iguales = [x for x in lista if x == pivote]
            mayores = [x for x in lista if x > pivote]
            return self.quicksort(menores) + iguales + self.quicksort(mayores)

    def esperar_enter(self):
        # Espera a que el usuario presione Enter
        print("\nPresione Enter para continuar...", end="", flush=True)
        while True:
            tecla = self.term.inkey()
            if tecla.name == "KEY_ENTER":
                break

    def header(self, text, buttons="[BACKSPACE] Volver | [I] Información"):
        # Imprime el encabezado para todas las pantallas
        print(self.term.clear())
        print(self.term.bold(self.term.green(text)))
        print()
        print(buttons)
        print("-" * 50)
        print()
