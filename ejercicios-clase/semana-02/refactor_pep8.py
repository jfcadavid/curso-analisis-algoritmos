# Código original:
# def CalcularPromedio(Lista):
#     s = 0
#     for x in Lista:
#         s = s + x
#     return s / len(Lista)
#
# l = [1, 2, 3, 4, 5]
# print(CalcularPromedio(l))

def calcular_promedio (lista: list[int]) -> float:
      """Calcula el promedio de una lista de números enteros.

    Args:
        lista: Lista de números enteros.

    Returns:
        El promedio de los números de la lista.
    """
      suma = 0

      for numero in lista:
            suma = suma + numero

      return suma/ len(lista)

def main() -> None:
    """Ejecuta el cálculo del promedio de la lista de ejemplo."""
    numeros = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(numeros)
    print(promedio)


if __name__ == "__main__":
    main()