from blessed import Terminal


class LineaYamanote:
    class Estacion:
        def __init__(self, nombre):
            self.nombre = nombre
            self.siguiente = None
            self.anterior = None

    def __init__(self):
        self.estacion_actual = None
        self.tamano = 0

    def agregar_estacion(self, nombre):
        nueva_estacion = self.Estacion(nombre)
        if self.estacion_actual is None:
            nueva_estacion.siguiente = nueva_estacion
            nueva_estacion.anterior = nueva_estacion
            self.estacion_actual = nueva_estacion
        else:
            ultima = self.estacion_actual.anterior
            ultima.siguiente = nueva_estacion
            nueva_estacion.anterior = ultima
            nueva_estacion.siguiente = self.estacion_actual
            self.estacion_actual.anterior = nueva_estacion
        self.tamano += 1

    def eliminar_estacion(self, nombre):
        if self.tamano == 0:
            return False
        estacion = self.estacion_actual
        for _ in range(self.tamano):
            if estacion.nombre == nombre:
                if self.tamano == 1:
                    self.estacion_actual = None
                else:
                    estacion.anterior.siguiente = estacion.siguiente
                    estacion.siguiente.anterior = estacion.anterior
                    if estacion == self.estacion_actual:
                        self.estacion_actual = estacion.siguiente
                self.tamano -= 1
                return True
            estacion = estacion.siguiente
        return False

    def avanzar(self):
        if self.tamano > 0:
            self.estacion_actual = self.estacion_actual.siguiente

    def retroceder(self):
        if self.tamano > 0:
            self.estacion_actual = self.estacion_actual.anterior

    def mostrar_estaciones(self):
        if self.tamano == 0:
            return "No hay estaciones en la línea."
        estacion = self.estacion_actual
        estaciones = []
        for _ in range(self.tamano):
            estaciones.append(estacion.nombre)
            estacion = estacion.siguiente
        return " -> ".join(estaciones)


class LineaYamanoteConsola:
    def __init__(self, term):
        self.linea = LineaYamanote()
        self.term = term
        self.opciones = [
            "Agregar Estación",
            "Eliminar Estación",
            "Avanzar a Siguiente Estación",
            "Retroceder a Estación Anterior",
            "Mostrar Estaciones",
            "Salir"
        ]
        self.opcion_actual = 0

    def menu(self):
        with self.term.cbreak(), self.term.hidden_cursor():
            while True:
                print(self.term.clear())
                print(self.term.bold(self.term.green("Línea Yamanote - Sistema de Gestión")))
                print("-" * 40)
                for idx, opcion in enumerate(self.opciones):
                    if idx == self.opcion_actual:
                        print(self.term.reverse(opcion))
                    else:
                        print(opcion)
                tecla = self.term.inkey()
                if tecla.code == self.term.KEY_UP:
                    self.opcion_actual = (self.opcion_actual - 1) % len(self.opciones)
                elif tecla.code == self.term.KEY_DOWN:
                    self.opcion_actual = (self.opcion_actual + 1) % len(self.opciones)
                elif tecla.name == "KEY_ENTER":
                    if not self.manejar_opcion():
                        break

    def manejar_opcion(self):
        opcion = self.opciones[self.opcion_actual]
        if opcion == "Salir":
            return False
        elif opcion == "Agregar Estación":
            nombre = self.capturar_texto("Ingrese el nombre de la estación: ")
            self.linea.agregar_estacion(nombre)
            print(f"Estación '{nombre}' agregada con éxito.")
        elif opcion == "Eliminar Estación":
            if self.linea.tamano == 0:
                print("No hay estaciones para eliminar.")
            else:
                nombre = self.capturar_texto("Ingrese el nombre de la estación a eliminar: ")
                if self.linea.eliminar_estacion(nombre):
                    print(f"Estación '{nombre}' eliminada.")
                else:
                    print(f"Estación '{nombre}' no encontrada.")
        elif opcion == "Avanzar a Siguiente Estación":
            if self.linea.tamano == 0:
                print("No hay estaciones en la línea.")
            else:
                self.linea.avanzar()
                print(f"Ahora en la estación: {self.linea.estacion_actual.nombre}")
        elif opcion == "Retroceder a Estación Anterior":
            if self.linea.tamano == 0:
                print("No hay estaciones en la línea.")
            else:
                self.linea.retroceder()
                print(f"Ahora en la estación: {self.linea.estacion_actual.nombre}")
        elif opcion == "Mostrar Estaciones":
            print(f"Estaciones en la línea: {self.linea.mostrar_estaciones()}")
        self.esperar_enter()
        return True

    def capturar_texto(self, mensaje):
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
        print("\nPresione Enter para continuar...", end="", flush=True)
        while True:
            tecla = self.term.inkey()
            if tecla.name == "KEY_ENTER":
                break

    def header(self, text, buttons="[BACKSPACE] Volver | [I] Información"):
        print(self.term.clear())
        print(self.term.bold(text))
        print()
        print(buttons)
        print("-" * 50)
        print()


if __name__ == "__main__":
    term = Terminal()
    consola = LineaYamanoteConsola(term)
    consola.menu()
