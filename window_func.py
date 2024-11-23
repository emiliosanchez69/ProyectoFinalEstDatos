import time
from windows.grafos import *
from windows.header import header #encabezado de ventanas

#FUNCIONES PARA CADA TEMA

def arreglos(term):

    while True:
        
        header("Opción 1: Arreglos", term)
        
        #aqui va el codigo
        print("ARREGLOS")

        key = term.inkey()
        #funcion para desactivar
        if key.name == "KEY_BACKSPACE": #vuelve al menu
            return
        elif key.lower() == "i":
            while True:
                header("Opción 1: Arreglos > Información", term, buttons="[BACKSPACE] Cerrar esta ventana")
                print("Los arreglos son estructuras de datos lineales.")
                key = term.inkey()
                if key.name == "KEY_BACKSPACE":
                    break


def window_2(term):
    while True:
        header("Opción 2: Pilas", term)
        
        #aqui va el codigo
        print("Aquí iría todo el contenido relacionado con 'Alright'.")

        key = term.inkey()
        if key.name == "KEY_BACKSPACE":
            return
        elif key.lower() == "i":
            while True:
                header("Opción 2: Pilas > Información", term, buttons="[BACKSPACE] Cerrar esta ventana")
                print("Las pilas son estructuras LIFO (Last In, First Out).")
                key = term.inkey()
                if key.name == "KEY_BACKSPACE":
                    break


def window_3(term):
    while True:
        header("Opción 3: Colas", term)
        
        #aqui va el codigo
        print("Aquí iría todo el contenido relacionado con 'DNA.'.")

        key = term.inkey()
        if key.name == "KEY_BACKSPACE":
            return
        elif key.lower() == "i":
            while True:
                header("Opción 3: Colas > Información", term, buttons="[BACKSPACE] Cerrar esta ventana")
                print("Las colas son estructuras FIFO (First In, First Out).")
                key = term.inkey()
                if key.name == "KEY_BACKSPACE":
                    break


def window_4(term):
    while True:
        header("Opción 4: Lista", term)

        #aqui va el codigo
        print("Aquí iría todo el contenido relacionado con 'King Kunta'.")

        key = term.inkey()
        if key.name == "KEY_BACKSPACE":
            return
        elif key.lower() == "i":
            while True:
                header("Opción 4: Lista > Información", term, buttons="[BACKSPACE] Cerrar esta ventana")
                print("Las listas son estructuras dinámicas de datos.")
                key = term.inkey()
                if key.name == "KEY_BACKSPACE":
                    break


def window_5(term):
    while True:
        header("Opción 5: Ordenamiento", term)

        #aqui va el codigo
        print("Aquí iría todo el contenido relacionado con 'Swimming Pools (Drank)'.")

        key = term.inkey()
        if key.name == "KEY_BACKSPACE":
            return
        elif key.lower() == "i":
            while True:
                header("Opción 5: Ordenamiento > Información", term, buttons="[BACKSPACE] Cerrar esta ventana")
                print("El ordenamiento organiza los datos en un orden específico.")
                key = term.inkey()
                if key.name == "KEY_BACKSPACE":
                    break


def window_6(term):
    while True:
        header("Opción 6: Árbol Binario", term)

        #aqui va el codigo
        print("Aquí iría todo el contenido relacionado con 'm.A.A.d city'.")

        key = term.inkey()
        if key.name == "KEY_BACKSPACE":
            return
        elif key.lower() == "i":
            while True:
                header("Opción 6: Árbol Binario > Información", term, buttons="[BACKSPACE] Cerrar esta ventana")
                print("Los árboles binarios son estructuras jerárquicas.")
                key = term.inkey()
                if key.name == "KEY_BACKSPACE":
                    break


def grafos(term):
    while True:            
        grafos_consola = GrafosConsola(term)
        grafos_consola.menu()
        return

# Asocia cada índice a una función específica
def window(option_index, term):
    windows = [arreglos, window_2, window_3, window_4, window_5, window_6, grafos]
    if 0 <= option_index < len(windows):
        windows[option_index](term)
