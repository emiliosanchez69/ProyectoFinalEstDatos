from blessed import Terminal
from menu_func import *


if __name__ == "__main__":
    
    term = Terminal()
    try:
        with term.cbreak(), term.hidden_cursor():
            welcome_screen(term)
            main_menu(term)
    finally:
        print(term.normal_cursor)
        print(term.clear())


