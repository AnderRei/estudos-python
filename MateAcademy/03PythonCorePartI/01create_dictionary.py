# Criar um dicionário onde:
# - cada argumento vira uma chave
# - o valor é a posição dele

# Só aceitar tipos: int, float, str, bool, None, tuple ou função (callable)
# Se não for permitido, imprimir:
# Cannot add {argument} to the dict!

# Não usar hash nem try/except → usar isinstance e callable


def create_dictionary(*args) -> dict:

    my_dict = {}

    for index, element in enumerate(args):
        if isinstance(element, (int, float, str, bool, type(None), tuple)) or callable(
            element
        ):
            my_dict[element] = index
        else:
            print(f"Cannot add {element} to the dict!")

    return my_dict


print(create_dictionary([1, 2], 3, 4, 5))
