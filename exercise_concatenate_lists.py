# Ejercicio 10: Concatenar listas

def concatenate_lists(lista1, lista2):
    """
    Concatena dos listas en una sola.

    Args:
        lista1: Primera lista
        lista2: Segunda lista

    Returns:
        Una nueva lista con todos los elementos de lista1 seguidos de lista2
    """
    lista3 = lista1 + lista2
    if len(lista1) == 0 and len(lista2) == 0:
        return lista1
    else:
        return lista3
