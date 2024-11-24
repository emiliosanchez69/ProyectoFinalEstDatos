from blessed import Terminal
import math

class Grafos:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def addEdge(self, u, v, w):
        self.grafo.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def Kruskal(self):
        result = []
        i = 0
        e = 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        parent = list(range(self.V))
        rank = [0] * self.V

        while e < self.V - 1 and i < len(self.grafo):
            u, v, w = self.grafo[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        costoMinimo = sum([weight for u, v, weight in result])
        return result, costoMinimo

class GrafosConsola:
    def __init__(self, term):
        self.grafo = Grafos(7)
        self.positions = self.calcular_posiciones_nodos()
        self.term = term
        self.menu_options = [
            "Agregar destino (arista)",
            "Calcular costo mínimo (Kruskal)",
            "Visualizar Grafo",
        ]
        self.current_option = 0

    def header(self, text, buttons="[BACKSPACE] Volver | [I] Información"):
        print(self.term.clear())
        print(self.term.bold(text))
        print()
        print(buttons)
        print("-" * 50)
        print()

    def calcular_posiciones_nodos(self):
        positions = {}
        radius = 10
        center_x, center_y = 20, 10
        for i in range(self.grafo.V):
            angle = 2 * math.pi * i / self.grafo.V
            x = round(center_x + radius * math.cos(angle))
            y = round(center_y + radius * math.sin(angle))
            positions[i] = (x, y)
        return positions

    def agregar_arista(self):
        try:
            print(self.term.clear())
            self.header("Opción 8 - Grafos -> Agregar destino (arista)", "")
            print("Ingresa los datos de la nueva arista:")
            print("Origen (0-6): ", end="", flush=True)
            u = int(self.capturar_numero(0, 6))

            print("\nDestino (0-6): ", end="", flush=True)
            v = int(self.capturar_numero(0, 6))

            print("\nPeso de la arista: ", end="", flush=True)
            w = int(self.capturar_numero(0, 1000))

            if u == v:
                print("Error: No se pueden agregar bucles.")
                self.esperar_enter()
                return

            self.grafo.addEdge(u, v, w)
            print(f"\nArista {u} -- {v} con peso {w} agregada correctamente.")
            self.esperar_enter()

        except ValueError:
            print("Error: Entrada inválida.")
            self.esperar_enter()

    def capturar_numero(self, min_val, max_val):
        numero = ""
        while True:
            key = self.term.inkey()
            if key.is_sequence and key.name == "KEY_ENTER":
                if numero.isdigit() and min_val <= int(numero) <= max_val:
                    return int(numero)
                else:
                    print(f"\nPor favor, ingresa un número válido entre {min_val} y {max_val}: ", end="", flush=True)
                    numero = ""
            elif key.is_sequence and key.name == "KEY_BACKSPACE":
                numero = numero[:-1]
            elif key.isdigit():
                numero += key
                print(key, end="", flush=True)

    def esperar_enter(self): # corregir
        print("\nPresiona Enter para continuar...", end="", flush=True)
        while True:
            key = self.term.inkey()
            if key.name == "KEY_ENTER" or key == "\n":
                break

    def calcularKruskal(self):
        result, cost = self.grafo.Kruskal()
        print(self.term.clear())
        self.header("Opción 8 - Grafos -> Calcular costo mínimo (Kruskal)", "")
        print(f"Costo total del MST: {cost}")
        for u, v, w in result:
            print(f"Arista {u} -- {v} con peso {w}")
        self.esperar_enter()

    def visualizar_grafo(self): #corregir
        print(self.term.clear())
        self.header("Opción 8 - Grafos -> Visualizar Grafo", "")
        if not self.grafo.grafo:
            print("El grafo está vacío. No hay nada que visualizar.")
            self.esperar_enter()
            return

        grid_height = 20
        grid_width = 40
        grid = [[" " for _ in range(grid_width)] for _ in range(grid_height)]

        for node, (x, y) in self.positions.items():
            if 0 <= x < grid_width and 0 <= y < grid_height:
                grid[y][x] = str(node)

        for row in grid:
            print("".join(row))
        self.esperar_enter()

    def menu(self):
        with self.term.fullscreen(), self.term.cbreak():
            while True:
                self.header("Opción 8 - Grafos")

                print(self.term.move_y(4))

                for i, option in enumerate(self.menu_options):
                    if i == self.current_option:
                        print(self.term.on_black(self.term.white(f"> {option}")))
                    else:
                        print(f"  {option}")

                key = self.term.inkey()
                if key.name == "KEY_DOWN":
                    self.current_option = (self.current_option + 1) % len(self.menu_options)
                elif key.name == "KEY_UP":
                    self.current_option = (self.current_option - 1) % len(self.menu_options)
                elif key.name == "KEY_ENTER" or key == "\n":
                    if self.current_option == 0:
                        self.agregar_arista()
                    elif self.current_option == 1:
                        self.calcularKruskal()
                    elif self.current_option == 2:
                        self.visualizar_grafo()

                elif key.name == "KEY_BACKSPACE":
                    break

                elif key.lower() == "i":
                    while True:
                        self.header("Opción 8: Grafos > Información", buttons="[BACKSPACE] Cerrar esta ventana")
                        print("1. Agregar una arista entre dos nodos (origen, destino y peso).")
                        print("2. Calcular el árbol de expansión mínima (MST) usando el algoritmo de Kruskal.")
                        print("3. Visualizar el grafo como texto ASCII.")
                        print("4. Salir para cerrar el programa.")
                        key = self.term.inkey()
                        if key.name == "KEY_BACKSPACE":
                            break