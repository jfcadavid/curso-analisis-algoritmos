"""Medicion de tiempos para los algoritmos de subarreglo maximo."""

import random
import time
from statistics import median

from matplotlib import pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def main() -> None:
    """Mide y compara los tiempos de los dos algoritmos."""
    tamanos = [10, 50, 100, 500, 1000, 4000, 8000]
    repeticiones = 3

    tiempos_fuerza_bruta = []
    tiempos_divide_venceras = []

    generador = random.Random(42)

    for n in tamanos:
        valores = [
            generador.randint(-100, 100)
            for _ in range(n)
        ]

        mediciones_fuerza = []
        mediciones_divide = []

        for _ in range(repeticiones):
            inicio = time.perf_counter()
            resultado_fuerza = subarreglo_fuerza_bruta(valores)
            fin = time.perf_counter()

            mediciones_fuerza.append(fin - inicio)

            inicio = time.perf_counter()
            resultado_divide = subarreglo_maximo(
                valores, 0, len(valores) - 1
            )
            fin = time.perf_counter()

            mediciones_divide.append(fin - inicio)

            assert resultado_fuerza[2] == resultado_divide[2]

        tiempo_fuerza = median(mediciones_fuerza)
        tiempo_divide = median(mediciones_divide)

        tiempos_fuerza_bruta.append(tiempo_fuerza)
        tiempos_divide_venceras.append(tiempo_divide)

        print(f"\nTamaño n = {n}")
        print(
            f"Fuerza bruta (mediana de {repeticiones}): "
            f"{tiempo_fuerza:.6f} segundos"
        )
        print(
            f"Divide y vencerás (mediana de {repeticiones}): "
            f"{tiempo_divide:.6f} segundos"
        )

    plt.figure()

    plt.plot(
        tamanos,
        tiempos_fuerza_bruta,
        marker="o",
        label="Fuerza bruta",
    )

    plt.plot(
        tamanos,
        tiempos_divide_venceras,
        marker="o",
        label="Divide y vencerás",
    )

    plt.title("Tiempo de ejecución del subarreglo máximo")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid()

    plt.savefig(
        "graficas/tiempo_vs_n.png",
        bbox_inches="tight",
    )

    plt.close()


if __name__ == "__main__":
    main()