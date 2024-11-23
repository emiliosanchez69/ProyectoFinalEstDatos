from window_func import window
import time

#pantalla de inicio
def welcome_screen(term): 

    #TEXTO DE PANTALLA DE INICIO
    print(term.clear())
    print(term.center(term.bold_orange("UNIVERSIDAD ANÁHUAC MAYAB")))
    print(term.center("Estructuras de Datos"))
    print()
    print(term.center(term.bold("PROYECTO FINAL")))
    print()
    print(term.center("Emilio Jose Sanchez Villalpando"))
    print(term.center("Prof. Luis Abel Calcaneo Murillo"))
    print()
    print(term.center("Presiona Enter para continuar..."))

    #PRESIONAR ENTER PARA CONTINUAR
    while True:
        key = term.inkey()
        if key.name == "KEY_ENTER" or key == "\n":
            break  #entra al programa
        else:
            pass

    print(term.clear())

#menu principal (TECNICAMENTE ES UN ARREGLO)
def main_menu(term):

    #N. OPCION
    menu_options = [
        "1. Arreglos",
        "2. Pilas",
        "3. Colas",
        "4. Lista",
        "5. Ordenamiento",
        "6. Árbol Binario",
        "7. Grafos",
        "8. Salir...",
    ]
    selected_index = 0

    #loop para mostrar el menu
    while True:
        print(term.clear())
        print(term.bold("Menú Principal\n"))
        print("-" * 50)

        # mostar opciones del menu, con colores
        for i, option in enumerate(menu_options):
            if i == selected_index:
                if "Salir" in option:
                    print(term.bold_red(f"> {option}"))  #salir en rojo bold cuando esta seleccionado
                else:
                    print(term.bold_green(f"> {option}"))  #opcion seleccionada con flecha, color verde
            else:
                if "Salir" in option:
                    print(term.red(f"  {option}"))  # mostrar salir en rojo
                else:
                    print(f"  {option}")  #mostrar opcion en blanco

        #leer input de teclado
        key = term.inkey()

        #inputs para navegar en el menu
        if key.name == "KEY_DOWN":
            selected_index = (selected_index + 1) % len(menu_options)
        elif key.name == "KEY_UP":
            selected_index = (selected_index - 1) % len(menu_options)
        elif key.name == "KEY_ENTER" or key == "\n":
            if selected_index == 7: #INPUT PARA SALIR
                print(term.clear() + "Saliendo del programa...")
                time.sleep(3)
                break
            else:
                window(selected_index, term)
