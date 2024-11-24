from blessed import Terminal


class PilaPasajeros:
    def __init__(self):
        self.pila = []

    def push(self, pasajero):
        """Agrega un pasajero a la pila."""
        self.pila.append(pasajero)

    def pop(self):
        """Elimina el pasajero en la parte superior de la pila."""
        if not self.is_empty():
            return self.pila.pop()
        else:
            return "La pila está vacía. No hay pasajeros para bajar."

    def peek(self):
        """Muestra el pasajero en la parte superior sin eliminarlo."""
        if not self.is_empty():
            return self.pila[-1]
        else:
            return "La pila está vacía."

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.pila) == 0

    def mostrar_pila(self):
        """Muestra todos los pasajeros en la pila."""
        if self.is_empty():
            return "La pila está vacía. No hay pasajeros."
        else:
            return " -> ".join(reversed(self.pila))


class GestorPasajerosConsola:
    def __init__(self, term):
        self.pila = PilaPasajeros()
        self.term = term
        self.opciones = [
            "Subir Pasajero (Push)",
            "Bajar Pasajero (Pop)",
            "Ver Pasajero en la Cima (Peek)",
            "Mostrar Todos los Pasajeros",
        ]
        self.opcion_actual = 0

    def header(self, text, buttons="[BACKSPACE] Volver | [ENTER] Seleccionar"):
        """Imprime el encabezado para cada pantalla."""
        print(self.term.clear())
        print(self.term.bold(self.term.green(text)))
        print()
        print(buttons)
        print("-" * 50)
        print()

    def menu(self):
        with self.term.cbreak(), self.term.hidden_cursor():
            while True:
                self.header("Sistema de Gestión de Pasajeros del Tren Bala")
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
        opcion = self.opciones[self.opcion_actual]
        self.header(f"Opción: {opcion}")
        if opcion == "Subir Pasajero (Push)":
            nombre = self.capturar_texto("Ingrese el nombre del pasajero: ")
            self.pila.push(nombre)
            print(f"Pasajero '{nombre}' subió al tren.")
        elif opcion == "Bajar Pasajero (Pop)":
            resultado = self.pila.pop()
            print(f"Resultado: {resultado}")
        elif opcion == "Ver Pasajero en la Cima (Peek)":
            resultado = self.pila.peek()
            print(f"Pasajero en la cima: {resultado}")
        elif opcion == "Mostrar Todos los Pasajeros":
            print("Pasajeros en el tren:")
            print(self.pila.mostrar_pila())
        self.esperar_enter()
        return True  # Continuar en el menú

    def capturar_texto(self, mensaje):
        """Captura la entrada del usuario."""
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
        """Espera a que el usuario presione Enter."""
        print("\nPresione Enter para continuar...", end="", flush=True)
        while True:
            tecla = self.term.inkey()
            if tecla.name == "KEY_ENTER":
                break
