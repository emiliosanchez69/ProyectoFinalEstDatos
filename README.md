""
# Sistema de Gestión del Tren Bala Japonés 🚄

Este proyecto simula diversas operaciones del sistema de gestión del tren bala japonés (Shinkansen). Utiliza estructuras de datos y algoritmos implementados en Python para modelar escenarios como la gestión de pasajeros, estaciones, horarios, y más.

---

## Características

1. **Arreglos**
   - Gestión de horarios de trenes.
   - Funcionalidades:
     - Agregar horarios.
     - Buscar horarios específicos.
     - Listar todos los horarios disponibles.

2. **Pilas**
   - Gestión de pasajeros abordando y descendiendo del tren usando pilas.
   - Funcionalidades:
     - Agregar pasajero (Push).
     - Quitar pasajero (Pop).
     - Ver pasajero en la cima (Peek).
     - Mostrar todos los pasajeros.

3. **Colas**
   - Sistema de gestión de boletos modelado como una cola.
   - Funcionalidades:
     - Encolar (agregar un boleto).
     - Desencolar (procesar un boleto).
     - Ver el próximo boleto (Peek).
     - Mostrar todos los boletos.

4. **Búsqueda Binaria**
   - Búsqueda eficiente de estaciones usando búsqueda binaria.
   - Funcionalidades:
     - Agregar estaciones.
     - Realizar búsqueda binaria.
     - Listar todas las estaciones.

5. **Lista Circular Doble**
   - Gestión de estaciones de la línea Yamanote utilizando una lista circular doblemente enlazada.
   - Funcionalidades:
     - Agregar una estación.
     - Eliminar una estación.
     - Navegar hacia adelante o atrás entre estaciones.
     - Mostrar todas las estaciones en orden circular.

6. **Quicksort**
   - Ordenamiento eficiente de nombres de estaciones usando el algoritmo Quicksort.
   - Funcionalidades:
     - Agregar estaciones.
     - Ordenar estaciones.
     - Listar estaciones ordenadas.

7. **Árbol Binario**
   - Gestión de datos de estaciones usando un árbol binario.
   - Funcionalidades:
     - Agregar una nueva estación.
     - Eliminar una estación.
     - Buscar una estación.
     - Recorrer el árbol (inorden, preorden, postorden).
     - Mostrar el árbol en un formato "gráfico" en consola.

8. **Grafos**
   - Simulación de una red de rutas de tren usando grafos.
   - Funcionalidades:
     - Agregar rutas entre estaciones.
     - Encontrar la ruta más corta basada en criterios como distancia, costo o tiempo.
     - Visualizar el grafo en la terminal.

---

## Estructura de Archivos

- `main.py` - Punto de entrada del programa.
- `menu_func.py` - Funciones para mostrar y navegar por el menú principal.
- `window_func.py` - Funciones que conectan las opciones del menú con los módulos específicos.
- `arboles.py` - Implementación de árboles binarios para gestión de estaciones.
- `busqbinaria.py` - Implementación de búsqueda binaria.
- `cola.py` - Implementación de colas para gestión de boletos.
- `dcll.py` - Lista circular doblemente enlazada para la línea Yamanote.
- `grafos.py` - Implementación de grafos para gestión de rutas.
- `header.py` - Gestión de encabezados para una interfaz consistente en la terminal.
- `pila.py` - Implementación de pilas para gestión de pasajeros.
- `quicksort.py` - Algoritmo Quicksort para ordenamiento de estaciones.
- `arreglos.py` - Implementación basada en arreglos para gestión de horarios.

---

## Uso

### Requisitos

- Python 3.7 o superior
- Biblioteca `blessed` para la interfaz de terminal:
  ```bash
  pip install blessed