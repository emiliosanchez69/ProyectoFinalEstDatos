import time
from windows.grafos import *
from windows.arboles import *
from windows.dcll import *
from windows.busqbinaria import *
from windows.quicksort import *
from windows.pila import * 
from windows.arreglos import * 

from windows.header import header #encabezado de ventanas

#FUNCIONES PARA CADA TEMA

def arreglos(term): #arreglos -> horarios
    while True:
       arreglos = GestorHorariosConsola(term)
       arreglos.menu()
       return

def pila(term): #pilas -> pasajeros LISTO
    while True:
        pila = GestorPasajerosConsola(term)
        pila.menu()
        return

def cola(term): #colas -> tickets LISTO
    while True:
        cola = GestorPasajerosConsola(term)
        cola.menu()
        return

def busqbinaria(term): #busqueda binaria LISTO
    while True:
        busqbinaria = TrenBalaBusquedaBinaria(term)
        busqbinaria.menu()
        return

def yamanote(term): #lista dcll LISTO
    while True:
        yamanote = LineaYamanoteConsola(term)
        yamanote.menu()
        return

def quicksort(term): #LISTO
    while True:
        quicksort = TrenBalaQuicksort(term)
        quicksort.menu()
        return

def arboles(term): #arbol listo
    while True:            
        arboles = ArbolBinarioConsola(term)
        arboles.menu()
        return

def grafos(term): #GRAFOS LISTO
    while True:            
        grafos = RedShinkansenConsola(term)
        grafos.menu()
        return

# Asocia cada índice a una función específica
def window(option_index, term):
    windows = [arreglos, pila, cola, busqbinaria, yamanote, quicksort, arboles, grafos]
    if 0 <= option_index < len(windows):
        windows[option_index](term)
