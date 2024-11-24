from blessed import Terminal


class SistemaHorarios:
    def __init__(self):
        self.horarios = []

    def agregar_horario(self, horario, destino):
        """Agrega un nuevo horario con su destino."""
        self.horarios.append({"horario": horario, "destino": destino})
        self.horarios.sort(key=lambda x: x["horario"])  # Mantener la lista ordenada por horarios

    def buscar_horario(self, horario):
        """Busca un horario específico usando búsqueda binaria."""
        izquierda, derecha = 0, len(self.horarios) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if self.horarios[medio]["horario"] == horario:
                return self.horarios[medio]
            elif self.horarios[medio]["horario"] < horario:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return None

    def eliminar_horario(self, horario):
        """Elimina un horario específico si existe."""
        for i, h in enumerate(self.horarios):
            if h["horario"] == horario:
                del self.horarios[i]
                return True
        return False

    def listar_horarios(self):
        """Muestra todos los horarios disponibles."""
        if not self.horarios:
            return "No hay horarios registrados."
        return "\n".join(f"{h['horario']} -> {h['destino']}" for h in self.horarios)


class GestorHorariosConsola:
    def __init__(self, term):
        self.sistema = SistemaHorarios()
        self.term = term
        self.opciones = [
            "Agregar Horario",
            "Buscar Horario",
            "Eliminar Horario",
            "Listar Todos los Horarios",
        ]
        self.opcion_actual = 0

    def header(self, text, buttons="[BACKSPACE] Volver | [ENTER] Seleccionar"):
        """Muestra el encabezado en la consola."""
        print(self.term.clear())
        print(self.term.bold(self.term.cyan(text)))
        print()
        print(buttons)
        print("-" * 50)
        print()

    def menu(self):
        """Muestra el menú principal."""
        with self.term.cbreak(), self.term.hidden_cursor():
            while True:
                self.header("Sistema de Horarios del Tren Bala")
                for idx, opcion in enumerate(self.opciones):
                    # Prefijo "> " para opción seleccionada, "  " para no seleccionada
                    prefijo = "> " if idx == self.opcion_actual else "  "
                    print(f"{prefijo}{opcion}")

                tecla = self.term.inkey()
                if tecla.code == self.term.KEY_UP:
                    self.opcion_actual = (self.opcion_actual - 1) % len(self.opciones)
                elif tecla.code == self.term.KEY_DOWN:
                    self.opcion_actual = (self.opcion_actual + 1) % len(self.opciones)
                elif tecla.name == "KEY_ENTER":
                    self.manejar_opcion()
                elif tecla.name == "KEY_BACKSPACE":
                    break

    def manejar_opcion(self):
        """Gestiona la selección del menú."""
        opcion = self.opciones[self.opcion_actual]
        if opcion == "Agregar Horario":
            self.header("Agregar Horario")
            horario = self.capturar_texto("Ingrese el horario (HH:MM): ")
            destino = self.capturar_texto("Ingrese el destino: ")
            self.sistema.agregar_horario(horario, destino)
            print()
            print(f"Horario {horario} hacia {destino} agregado con éxito.")
        elif opcion == "Buscar Horario":
            self.header("Buscar Horario")
            horario = self.capturar_texto("Ingrese el horario a buscar (HH:MM): ")
            resultado = self.sistema.buscar_horario(horario)
            if resultado:
                print()
                print(f"Horario encontrado: {resultado['horario']} -> {resultado['destino']}")
            else:
                print()
                print("Horario no encontrado.")
        elif opcion == "Eliminar Horario":
            self.header("Eliminar Horario")
            horario = self.capturar_texto("Ingrese el horario a eliminar (HH:MM): ")
            if self.sistema.eliminar_horario(horario):
                print()
                print(f"Horario {horario} eliminado con éxito.")
            else:
                print()
                print("Horario no encontrado.")
        elif opcion == "Listar Todos los Horarios":
            self.header("Listar Todos los Horarios")
            print("Horarios disponibles:")
            print(self.sistema.listar_horarios())
        self.esperar_enter()

    def capturar_texto(self, mensaje):
        """Captura texto ingresado por el usuario."""
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
        """Espera a que el usuario presione Enter para continuar."""
        print("\nPresione Enter para continuar...", end="", flush=True)
        while True:
            tecla = self.term.inkey()
            if tecla.name == "KEY_ENTER":
                break