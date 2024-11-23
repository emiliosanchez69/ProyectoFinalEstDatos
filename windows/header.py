def header(text, term, buttons="[BACKSPACE] Volver | [I] Información"):
    print(term.clear())
    print(term.bold(text))
    print()
    print(buttons)
    print("-" * 50)
    print()