from blessed import Terminal
import math
import matplotlib.pyplot as plt
import networkx as nx

class RedShinkansen:
    def __init__(self, estaciones):
        self.estaciones = estaciones  
        self.rutas = []

    def agregar_ruta(self, origen, destino, distancia, costo, tiempo):
        self.rutas.append({"origen": origen, "destino": destino, "distancia": distancia, "costo": costo, "tiempo": tiempo})

    def encontrar(self, padre, i):
        if padre[i] != i:
            padre[i] = self.encontrar(padre, padre[i])
        return padre[i]

    def unir(self, padre, rango, x, y):
        if rango[x] < rango[y]:
            padre[x] = y
        elif rango[x] > rango[y]:
            padre[y] = x
        else:
            padre[y] = x
            rango[x] += 1

    def calcular_kruskal(self, criterio):
        resultado = []
        i = 0
        e = 0
        self.rutas = sorted(self.rutas, key=lambda ruta: ruta[criterio])
        padre = list(range(len(self.estaciones)))
        rango = [0] * len(self.estaciones)

        while e < len(self.estaciones) - 1 and i < len(self.rutas):
            ruta = self.rutas[i]
            i += 1
            x = self.encontrar(padre, self.estaciones.index(ruta["origen"]))
            y = self.encontrar(padre, self.estaciones.index(ruta["destino"]))

            if x != y:
                e += 1
                resultado.append(ruta)
                self.unir(padre, rango, x, y)

        return resultado

class RedShinkansenConsola:
    def __init__(self, term):
        self.term = term
        self.red = RedShinkansen(["Tokio", "Osaka", "Kioto", "Nagoya", "Hiroshima", "Fukuoka"])
        self.menu_opciones = [
            "Agregar ruta (conexión)",
            "Calcular costo mínimo (por distancia, costo, o tiempo)",
            "Visualizar red ferroviaria",
            "Graficar red ferroviaria",
            "Graficar MST"
        ]
        self.opcion_actual = 0

    def header(self, text, buttons="[BACKSPACE] Volver | [I] Información"):
        print(self.term.clear())
        print(self.term.bold(text))
        print()
        print(buttons)
        print("-" * 50)
        print()

    def esperar_enter(self):
        print("\nPresiona Enter para continuar...", end="", flush=True)
        while True:
            key = self.term.inkey()
            if key.name == "KEY_ENTER" or key == "\n":
                break

    def seleccionar_estacion(self, prompt, estaciones):
        opciones = self.red.estaciones
        seleccion = 0
        while True:
            print(self.term.clear())
            self.header(prompt)
            for idx, estacion in enumerate(opciones):
                line = "> " + estacion if idx == seleccion else "  " + estacion
                print(line)
            key = self.term.inkey()
            if key.name == "KEY_DOWN" and seleccion < len(opciones) - 1:
                seleccion += 1
            elif key.name == "KEY_UP" and seleccion > 0:
                seleccion -= 1
            elif key.name == "KEY_ENTER":
                return opciones[seleccion]
            elif key.name == "KEY_BACKSPACE":
                return None
            
    def capturar_texto(self, prompt=""):
        # Captura texto del usuario en modo terminal interactiva
        print(prompt, end="", flush=True)
        buffer = ""
        while True:
            key = self.term.inkey()
            if key.name == "KEY_ENTER" or key == "\n":
                return buffer.strip()
            elif key.name == "KEY_BACKSPACE":
                buffer = buffer[:-1]
                print(f"\r{prompt}{buffer}{' ' * 10}\r{prompt}{buffer}", end="", flush=True)
            elif key.isprintable():
                buffer += key
                print(key, end="", flush=True)

    def agregar_ruta_consola(self):
        # Permite agregar una nueva ruta a la red
        print(self.term.clear())
        self.header("Rutas -> Agregar ruta", "[BACKSPACE] Volver")
        
        # Seleccionar origen
        origen = self.seleccionar_estacion("Rutas -> Agregar ruta -> Selecciona la estación de origen:", self.red.estaciones)
        if origen is None:
            return  # Cancelado por el usuario

        # Seleccionar destino
        destino = self.seleccionar_estacion("Rutas -> Agregar ruta -> Selecciona la estación de destino:", self.red.estaciones)
        if destino is None:
            return  # Cancelado por el usuario

        try:
            self.header("Rutas -> Agregar ruta", "[BACKSPACE] Volver")
            print(f"Origen: {origen}, Destino: {destino}.")
            print()
            distancia = int(self.capturar_texto("Distancia (en km): "))
            print()
            costo = int(self.capturar_texto("Costo (en yenes): "))
            print()
            tiempo = int(self.capturar_texto("Tiempo (en minutos): "))
            print()

            if origen == destino:
                print("Error: Origen y destino no pueden ser iguales.")
            else:
                self.red.agregar_ruta(origen, destino, distancia, costo, tiempo)
                print(f"\nRuta agregada: {origen} -> {destino}, {distancia} km, {costo} yenes, {tiempo} minutos.")
        except ValueError:
            print("\nError: Entrada inválida.")
        self.esperar_enter()

    def calcular_costo_minimo(self):
        # Calcula el costo mínimo usando un criterio especificado
        if not self.red.rutas:
            # Bloquea la operación si no hay rutas
            print(self.term.clear())
            self.header("Rutas -> Calcular costo mínimo", "")
            print("No hay rutas disponibles para calcular el costo mínimo.")
            self.esperar_enter()
            return

        criterios = ["Distancia (km)", "Costo (yenes)", "Tiempo (minutos)"]
        seleccion = 0

        while True:
            print(self.term.clear())
            self.header("Rutas -> Calcular costo mínimo","[BACKSPACE] Volver")
            print("Selecciona el criterio para calcular el costo mínimo:")

            # Mostrar opciones de criterios
            for i, criterio in enumerate(criterios):
                if i == seleccion:
                    print(self.term.on_black(self.term.white(f"> {criterio}")))
                else:
                    print(f"  {criterio}")

            key = self.term.inkey()
            if key.name == "KEY_DOWN":
                seleccion = (seleccion + 1) % len(criterios)
            elif key.name == "KEY_UP":
                seleccion = (seleccion - 1) % len(criterios)
            elif key.name == "KEY_ENTER" or key == "\n":
                # Asignar la clave del criterio seleccionado
                if seleccion == 0:
                    key = "distancia"
                elif seleccion == 1:
                    key = "costo"
                elif seleccion == 2:
                    key = "tiempo"
                break
            elif key.name == "KEY_BACKSPACE":
                return

        # Calcular y mostrar el costo mínimo usando el criterio seleccionado
        resultado = self.red.calcular_kruskal(key)
        print(self.term.clear())
        self.header(f"Red ferroviaria mínima por {key}")
        for ruta in resultado:
            print(f"{ruta['origen']} -> {ruta['destino']}: {ruta[key]}")
        self.esperar_enter()

    def visualizar_red(self):
        # Muestra la red ferroviaria actual
        print(self.term.clear())
        self.header("Rutas -> Visualizar red ferroviaria", "")
        if not self.red.rutas:
            print("La red ferroviaria está vacía. No hay rutas para visualizar.")
        else:
            for ruta in self.red.rutas:
                print(f"{ruta['origen']} -> {ruta['destino']}: {ruta['distancia']} km, {ruta['costo']} yenes, {ruta['tiempo']} minutos")
        self.esperar_enter()

    def mostrar_ayuda(self):
        # Muestra la sección de ayuda
        while True:
            print(self.term.clear())
            self.header("Rutas -> Ayuda", buttons="[BACKSPACE] Volver")
            print("1. Agrega una nueva conexión entre estaciones.")
            print("2. Calcula la red ferroviaria más eficiente.")
            print("3. Visualiza todas las conexiones actuales.")
            print("4. Salir para cerrar el programa.")

            key = self.term.inkey()
            if key.name == "KEY_BACKSPACE":
                break

    def graficar_red(self, mst=False):
        G = nx.Graph()
        for ruta in self.red.rutas:
            G.add_edge(ruta['origen'], ruta['destino'], weight=ruta['distancia'])
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Red Ferroviaria" if not mst else "MST")
        plt.show()

    def mostrar_ayuda(self):
        # Muestra la sección de ayuda
        while True:
            print(self.term.clear())
            self.header("Rutas -> Ayuda", buttons="[BACKSPACE] Volver")
            print("1. Agrega una nueva conexión entre estaciones.")
            print("2. Calcula la red ferroviaria más eficiente.")
            print("3. Visualiza todas las conexiones actuales.")
            print("4. Salir para cerrar el programa.")

            key = self.term.inkey()
            if key.name == "KEY_BACKSPACE":
                break

    def menu(self):
        while True:
            self.header("Rutas")
            for i, option in enumerate(self.menu_opciones):
                if i == self.opcion_actual:
                    print(f"> {option}")
                else:
                    print(f"  {option}")
            key = self.term.inkey()
            if key.name == "KEY_DOWN":
                self.opcion_actual = (self.opcion_actual + 1) % len(self.menu_opciones)
            elif key.name == "KEY_UP":
                self.opcion_actual = (self.opcion_actual - 1) % len(self.menu_opciones)
            elif key.name == "KEY_ENTER":
                if self.opcion_actual == 0:  # Agregar ruta
                    self.agregar_ruta_consola()
                elif self.opcion_actual == 1:  # Calcular costo mínimo
                    self.calcular_costo_minimo()
                elif self.opcion_actual == 2:  # Visualizar red
                    self.visualizar_red()
                elif self.opcion_actual == 3:  # Graficar red
                    self.graficar_red()
                elif self.opcion_actual == 4:  # Graficar MST
                    self.graficar_red(mst=True)
            
            elif key.lower() == "i":
                    self.mostrar_ayuda()

            elif key.name == "KEY_BACKSPACE":
                break
