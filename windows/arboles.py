from blessed import Terminal


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def nuevo_nodo(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar_nodo(self, valor, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self.buscar_nodo(valor, nodo.izquierda)
        else:
            return self.buscar_nodo(valor, nodo.derecha)

    def borrar_nodo(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.valor = self._min_valor(nodo.derecha).valor
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.valor)
        return nodo

    def _min_valor(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def recorrido_inorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return []
        resultado = []
        if nodo.izquierda is not None:
            resultado += self.recorrido_inorden(nodo.izquierda)
        resultado.append(nodo.valor)
        if nodo.derecha is not None:
            resultado += self.recorrido_inorden(nodo.derecha)
        return resultado

    def recorrido_preorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return []
        resultado = [nodo.valor]
        if nodo.izquierda is not None:
            resultado += self.recorrido_preorden(nodo.izquierda)
        if nodo.derecha is not None:
            resultado += self.recorrido_preorden(nodo.derecha)
        return resultado

    def recorrido_postorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return []
        resultado = []
        if nodo.izquierda is not None:
            resultado += self.recorrido_postorden(nodo.izquierda)
        if nodo.derecha is not None:
            resultado += self.recorrido_postorden(nodo.derecha)
        resultado.append(nodo.valor)
        return resultado

    def graficar(self, nodo=None, nivel=0, prefijo=""):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return "Árbol vacío"

        resultado = ""
        if nodo.derecha is not None:
            resultado += self.graficar(nodo.derecha, nivel + 1, prefijo + "    ")
        resultado += f"{prefijo}{'|-- ' if nivel > 0 else ''}{nodo.valor}\n"
        if nodo.izquierda is not None:
            resultado += self.graficar(nodo.izquierda, nivel + 1, prefijo + "    ")
        return resultado


class ArbolBinarioConsola:
    def __init__(self, term):
        self.arbol = ArbolBinario()
        self.term = term
        self.opciones = [
            "Nuevo Nodo",
            "Borrar Nodo",
            "Buscar Nodo",
            "Recorrido Inorden",
            "Recorrido Preorden",
            "Recorrido Postorden",
            "Graficar Árbol",
            "Salir",
        ]
        self.opcion_actual = 0

    def menu(self):
        with self.term.cbreak(), self.term.hidden_cursor():
            while True:
                print(self.term.clear())
                print(self.term.bold("Gestor de Árbol Binario"))
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
        elif opcion == "Nuevo Nodo":
            valor = self.capturar_texto("Ingrese un valor: ")
            try:
                self.arbol.nuevo_nodo(int(valor))
                print()
                print(f"Nodo {valor} insertado con éxito.")
            except ValueError:
                print()
                print("Entrada inválida. Ingrese un número entero.")
        elif opcion == "Borrar Nodo":
            valor = self.capturar_texto("Ingrese el valor a borrar: ")
            try:
                self.arbol.borrar_nodo(int(valor))
                print()
                print(f"Nodo {valor} eliminado (si existía).")
            except ValueError:
                print()
                print("Entrada inválida. Ingrese un número entero.")
        elif opcion == "Buscar Nodo":
            valor = self.capturar_texto("Ingrese el valor a buscar: ")
            try:
                encontrado = self.arbol.buscar_nodo(int(valor))
                print()
                print(f"El valor {valor} {'fue encontrado' if encontrado else 'no existe'} en el árbol.")
            except ValueError:
                print()
                print("Entrada inválida. Ingrese un número entero.")
        elif opcion == "Recorrido Inorden":
            resultado = self.arbol.recorrido_inorden()
            print()
            print("Recorrido Inorden:", resultado)
        elif opcion == "Recorrido Preorden":
            print()
            resultado = self.arbol.recorrido_preorden()
            print("Recorrido Preorden:", resultado)
        elif opcion == "Recorrido Postorden":
            print()
            resultado = self.arbol.recorrido_postorden()
            print("Recorrido Postorden:", resultado)
        elif opcion == "Graficar Árbol":
            print()
            grafico = self.arbol.graficar()
            print("\nÁrbol Binario:")
            print(grafico)
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
