"""Comparacion experimental entre insertion sort y merge sort."""

import time

from matplotlib import pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


def main() -> None:
    """Mide ambos algoritmos sobre el escenario aleatorio de Tamiza."""

    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    tiempos_insertion = []
    tiempos_merge = []

    for n in tamanos:
        datos = generar_aleatorio(n)

        inicio = time.perf_counter()
        _, comparaciones_insertion = insertion_sort(datos)
        fin = time.perf_counter()

        tiempo_insertion = fin - inicio
        tiempos_insertion.append(tiempo_insertion)

        inicio = time.perf_counter()
        _, comparaciones_merge = merge_sort(datos)
        fin = time.perf_counter()

        tiempo_merge = fin - inicio
        tiempos_merge.append(tiempo_merge)

        print(f"\nTamaño n = {n}")

        print(
            "Insertion sort:",
            comparaciones_insertion,
            "comparaciones -",
            f"{tiempo_insertion:.6f}",
            "segundos",
        )

        print(
            "Merge sort:",
            comparaciones_merge,
            "comparaciones -",
            f"{tiempo_merge:.6f}",
            "segundos",
        )

    plt.figure()

    plt.plot(
        tamanos,
        tiempos_insertion,
        marker="o",
        label="Insertion sort",
    )

    plt.plot(
        tamanos,
        tiempos_merge,
        marker="o",
        label="Merge sort",
    )

    plt.title("Tiempo de ejecución: insertion sort vs. merge sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid()

    plt.savefig(
        "graficas/parte4_tiempo.png",
        bbox_inches="tight",
    )

    plt.close()


if __name__ == "__main__":
    main()