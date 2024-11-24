from blessed import Terminal


class ColaPasajeros:
    def __init__(self):
        self.cola = []

    def encolar(self, pasajero):
        # Agrega un pasajero al final de la cola
        self.cola.append(pasajero)

    def desencolar(self):
        # Elimina el pasajero al inicio de la cola
        if not self.is_empty():
            return self.cola.pop(0)
        else:
            return "La cola está vacía. No hay pasajeros para bajar."

    def peek(self):
        # Muestra el pasajero al inicio de la cola sin eliminarlo
        if not self.is_empty():
            return self.cola[0]
        else:
            return "La cola está vacía."

    def is_empty(self):
        # Verifica si la cola está vacía
        return len(self.cola) == 0

    def mostrar_cola(self):
        # Muestra todos los pasajeros en la cola
        if self.is_empty():
            return "La cola está vacía. No hay pasajeros."
        else:
            return " <- ".join(self.cola)


class GestorPasajerosConsola:
    def __init__(self, term):
        self.cola = ColaPasajeros()
        self.term = term
        self.opciones = [
            "Subir Pasajero (Encolar)",
            "Bajar Pasajero (Desencolar)",
            "Ver Próximo Pasajero (Peek)",
            "Mostrar Todos los Pasajeros",
        ]
        self.opcion_actual = 0

    def header(self, text, buttons="[BACKSPACE] Volver | [ENTER] Seleccionar"):
        # Imprime el encabezado para cada pantalla
        print(self.term.clear())
        print(self.term.bold(self.term.green(text)))
        print()
        print(buttons)
        print("-" * 50)
        print()

    def menu(self):
        # Muestra el menú principal
        with self.term.cbreak(), self.term.hidden_cursor():
            while True:
                self.header("Sistema de Gestión de Pasajeros del Tren Bala (Cola)")
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
        # Maneja la opción seleccionada por el usuario
        opcion = self.opciones[self.opcion_actual]
        self.header(f"Opción: {opcion}")
        if opcion == "Subir Pasajero (Encolar)":
            nombre = self.capturar_texto("Ingrese el nombre del pasajero: ")
            self.cola.encolar(nombre)
            print(f"Pasajero '{nombre}' subió al tren.")
        elif opcion == "Bajar Pasajero (Desencolar)":
            resultado = self.cola.desencolar()
            print(f"Resultado: {resultado}")
        elif opcion == "Ver Próximo Pasajero (Peek)":
            resultado = self.cola.peek()
            print(f"Próximo pasajero: {resultado}")
        elif opcion == "Mostrar Todos los Pasajeros":
            print("Pasajeros en el tren:")
            print(self.cola.mostrar_cola())
        self.esperar_enter()
        return True  # Continuar en el menú

    def capturar_texto(self, mensaje):
        # Captura la entrada del usuario
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