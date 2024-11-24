# Proyecto de Gestión del Tren Bala Japonés

Este proyecto implementa diversas estructuras de datos y algoritmos en Python, relacionados con la gestión y operación del tren bala japonés. Se usan herramientas de consola y gráficas para representar y manipular datos.

## Tecnologías utilizadas

- **Python**: Lenguaje de programación base del proyecto.
- **Blessed**: Biblioteca para manejar interfaces interactivas en la terminal.
- **Matplotlib**: Para graficar redes y árboles.
- **NetworkX**: Para la representación de grafos.

## Estructuras de datos y funcionalidades

### 1. Listas Doblemente Ligadas Circulares
Módulo: `dcll.py`

- Implementación para manejar estaciones en una línea circular.
- Operaciones incluidas: agregar, eliminar, avanzar y retroceder estaciones.

### 2. Grafos
Módulo: `grafos.py`

- Representación de redes ferroviarias.
- Cálculo de rutas mínimas utilizando algoritmos de grafos.

### 3. Pilas
Módulo: `pila.py`

- Representación de pasajeros subiendo y bajando de un tren usando el modelo de pila (LIFO).

### 4. Colas
Módulo: `cola.py`

- Representación de pasajeros en cola para abordar el tren (FIFO).

### 5. Árboles Binarios
Módulo: `arboles.py`

- Implementación de operaciones básicas en árboles binarios: insertar, eliminar, buscar, y recorridos (preorden, inorden, postorden).
- Visualización del árbol en la consola.

### 6. Algoritmos de Ordenamiento
Módulo: `quicksort.py`

- Implementación del algoritmo Quicksort para ordenar estaciones.

### 7. Búsqueda Binaria
Módulo: `busqbinaria.py`

- Implementación de la búsqueda binaria para encontrar estaciones en una lista ordenada.

### 8. Arreglos
Módulo: `arreglos.py`

- Manejo de horarios de trenes con operaciones de búsqueda y ordenamiento.

## Organización de los archivos

- `dcll.py`: Listas Doblemente Ligadas Circulares.
- `grafos.py`: Implementación y visualización de grafos.
- `header.py`: Configuración para cabeceras de las interfaces.
- `pila.py`: Modelo de Pilas.
- `quicksort.py`: Ordenamiento por Quicksort.
- `arboles.py`: Árboles binarios.
- `arreglos.py`: Gestión de horarios con arreglos.
- `busqbinaria.py`: Algoritmo de búsqueda binaria.
- `cola.py`: Modelo de Colas.
- `menu_func.py`: Funcionalidades generales del menú.
- `window_func.py`: Configuración de ventanas para interfaz gráfica.
- `main.py`: Archivo principal para ejecutar el programa.

## Ejecución del Proyecto

Para ejecutar el proyecto, se necesita Python instalado en el sistema. Asegúrese de instalar las bibliotecas necesarias:

```bash
pip install blessed matplotlib networkx

```
Luego, ejecute el archivo principal:
```bash
python main.py

```

Desarrollado por Emilio J. Sanchez Villalpando.\
ID: 00491563\
Con fines educativos. 


