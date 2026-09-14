"""Experimento de los tres escenarios de entrada de Tamiza."""

import time

from matplotlib import pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


def main() -> None:
    """Mide insertion sort sobre los tres escenarios de Tamiza."""

    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    tiempos_aleatorio = []
    tiempos_casi_ordenado = []
    tiempos_inverso = []

    comparaciones_aleatorio = []
    comparaciones_casi_ordenado = []
    comparaciones_inverso = []

    for n in tamanos:
        datos_aleatorio = generar_aleatorio(n)
        datos_casi_ordenado = generar_casi_ordenado(n)
        datos_inverso = generar_inverso(n)

        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos_aleatorio)
        fin = time.perf_counter()

        tiempos_aleatorio.append(fin - inicio)
        comparaciones_aleatorio.append(comparaciones)

        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos_casi_ordenado)
        fin = time.perf_counter()

        tiempos_casi_ordenado.append(fin - inicio)
        comparaciones_casi_ordenado.append(comparaciones)

        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos_inverso)
        fin = time.perf_counter()

        tiempos_inverso.append(fin - inicio)
        comparaciones_inverso.append(comparaciones)

        print(f"\nTamaño n = {n}")

        print(
            "A - Aleatorio:",
            comparaciones_aleatorio[-1],
            "comparaciones -",
            f"{tiempos_aleatorio[-1]:.6f}",
            "segundos",
        )

        print(
            "B - Casi ordenado:",
            comparaciones_casi_ordenado[-1],
            "comparaciones -",
            f"{tiempos_casi_ordenado[-1]:.6f}",
            "segundos",
        )

        print(
            "C - Orden inverso:",
            comparaciones_inverso[-1],
            "comparaciones -",
            f"{tiempos_inverso[-1]:.6f}",
            "segundos",
        )

    plt.figure()

    plt.plot(
        tamanos,
        comparaciones_aleatorio,
        marker="o",
        label="A - Aleatorio",
    )

    plt.plot(
        tamanos,
        comparaciones_casi_ordenado,
        marker="o",
        label="B - Casi ordenado",
    )

    plt.plot(
        tamanos,
        comparaciones_inverso,
        marker="o",
        label="C - Orden inverso",
    )

    plt.title("Comparaciones de insertion sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid()

    plt.savefig(
        "graficas/parte3_comparaciones.png",
        bbox_inches="tight",
    )

    plt.close()

    plt.figure()

    plt.plot(
        tamanos,
        tiempos_aleatorio,
        marker="o",
        label="A - Aleatorio",
    )

    plt.plot(
        tamanos,
        tiempos_casi_ordenado,
        marker="o",
        label="B - Casi ordenado",
    )

    plt.plot(
        tamanos,
        tiempos_inverso,
        marker="o",
        label="C - Orden inverso",
    )

    plt.title("Tiempo de ejecución de insertion sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid()

    plt.savefig(
        "graficas/parte3_tiempo.png",
        bbox_inches="tight",
    )

    plt.close()


if __name__ == "__main__":
    main()