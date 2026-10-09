"""Pruebas para los algoritmos de subarreglo maximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def probar(serie: list[float], suma_esperada: float) -> None:
    """Verifica ambos algoritmos sobre una serie conocida."""
    resultado_fuerza = subarreglo_fuerza_bruta(serie)

    resultado_divide = subarreglo_maximo(
        serie,
        0,
        len(serie) - 1,
    )

    assert resultado_fuerza[2] == suma_esperada
    assert resultado_divide[2] == suma_esperada


# Serie de la situacion problema.
probar(
    [-3, 5, -2, 8, -6, 3, 9, -4],
    17,
)

# Un solo elemento.
probar(
    [7],
    7,
)

# Todos los valores negativos.
probar(
    [-5, -2, -8, -1],
    -1,
)

# Todos los valores positivos.
probar(
    [2, 4, 3, 5],
    14,
)

# El mejor tramo cruza el punto medio.
probar(
    [-2, 3, 4, -1],
    7,
)


generador = random.Random(42)

for _ in range(20):
    tamano = generador.randint(1, 20)

    serie = [
        generador.randint(-20, 20)
        for _ in range(tamano)
    ]

    resultado_fuerza = subarreglo_fuerza_bruta(serie)

    resultado_divide = subarreglo_maximo(
        serie,
        0,
        len(serie) - 1,
    )

    assert resultado_fuerza[2] == resultado_divide[2]


print("Todas las pruebas pasaron correctamente.")