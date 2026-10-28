
"""Mide el rendimiento de la lista enlazada y la tabla hash."""

import csv
import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


# Configuracion general de los experimentos.
CANTIDAD_BUSQUEDAS = 200
REPETICIONES = 3
ESTADO = "en bodega"

# Las graficas se guardan junto al archivo medicion.py.
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"


def es_primo(numero: int) -> bool:
    """Comprueba si un numero entero es primo.

    Args:
        numero: numero que se desea comprobar.

    Returns:
        True si el numero es primo; False en caso contrario.
    """
    if numero < 2:
        return False

    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


def primo_cercano(numero: int) -> int:
    """Busca el primer primo igual o mayor que un numero.

    Args:
        numero: numero desde el que comienza la busqueda.

    Returns:
        Un numero primo igual o mayor que el recibido.
    """
    candidato = max(2, numero)

    while not es_primo(candidato):
        candidato += 1

    return candidato


def generar_guias(
    cantidad: int, semilla: int = 42
) -> list[int]:
    """Genera numeros de guia unicos de diez digitos.

    Args:
        cantidad: numero de guias que se necesitan.
        semilla: semilla para reproducir la coleccion.

    Returns:
        Una lista de guias sin repeticiones.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), cantidad)


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)

        if guia not in existentes:
            inexistentes.append(guia)

    return inexistentes


def construir_lista(guias: list[int]) -> ListaEnlazada:
    """Construye una lista enlazada con las guias recibidas.

    Args:
        guias: numeros de guia que se van a insertar.

    Returns:
        Lista enlazada con todas las guias.
    """
    lista = ListaEnlazada()

    for guia in guias:
        lista.insertar(guia, ESTADO)

    return lista


def construir_tabla(
    guias: list[int], m: int
) -> TablaHash:
    """Construye una tabla hash con las guias recibidas.

    Args:
        guias: numeros de guia que se van a insertar.
        m: cantidad de casillas de la tabla.

    Returns:
        Tabla hash con todas las guias.
    """
    tabla = TablaHash(m)

    for guia in guias:
        tabla.insertar(guia, ESTADO)

    return tabla


def medir_busquedas(
    estructura: ListaEnlazada | TablaHash,
    inexistentes: list[int]
) -> float:
    """Mide el tiempo medio por busqueda infructuosa.

    Args:
        estructura: lista enlazada o tabla hash que se medira.
        inexistentes: guias que no estan almacenadas.

    Returns:
        Mediana de tres tiempos medios, en milisegundos.
    """
    tiempos_medios = []

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()

        for guia in inexistentes:
            estructura.buscar(guia)

        fin = time.perf_counter()

        tiempo_medio = (
            (fin - inicio) * 1000 / len(inexistentes)
        )

        tiempos_medios.append(tiempo_medio)

    return statistics.median(tiempos_medios)


def guardar_csv(
    nombre: str, resultados: list[dict]
) -> None:
    """Guarda los resultados numericos de un experimento.

    Args:
        nombre: nombre del archivo CSV.
        resultados: filas con los datos medidos.
    """
    ruta = CARPETA_GRAFICAS / nombre

    with ruta.open(
        "w", newline="", encoding="utf-8"
    ) as archivo:
        escritor = csv.DictWriter(
            archivo,
            fieldnames=list(resultados[0].keys())
        )
        escritor.writeheader()
        escritor.writerows(resultados)


def experimento_a() -> None:
    """Compara busquedas en lista y tabla para distintos tamanos."""
    cantidades = [100, 500, 1000, 5000, 20000, 50000]

    resultados = []

    print("\nEXPERIMENTO A: LISTA VS TABLA HASH")
    print("n | m | alfa | lista (ms) | hash (ms)")

    for n in cantidades:
        # La tabla debe tener m primo cercano a n / 2.
        m = primo_cercano(n // 2)

        # Ambas estructuras reciben las mismas guias.
        guias = generar_guias(n)
        lista = construir_lista(guias)
        tabla = construir_tabla(guias, m)

        # Preparamos las 200 guias inexistentes.
        inexistentes = generar_guias_inexistentes(
            set(guias), CANTIDAD_BUSQUEDAS
        )

        # Comprobamos una muestra de guias existentes.
        for guia in guias[:10]:
            estado_lista = lista.buscar(guia)
            assert estado_lista is not None
            assert estado_lista == tabla.buscar(guia)

        # Comprobamos que las guias de prueba no existen.
        for guia in inexistentes:
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None

        # Medimos solamente las busquedas.
        tiempo_lista = medir_busquedas(
            lista, inexistentes
        )
        tiempo_hash = medir_busquedas(
            tabla, inexistentes
        )

        fila = {
            "n": n,
            "m": m,
            "alfa": tabla.factor_carga(),
            "lista_ms": tiempo_lista,
            "hash_ms": tiempo_hash,
        }

        resultados.append(fila)

        print(
            f"{n} | {m} | {fila['alfa']:.4f} | "
            f"{tiempo_lista:.6f} | {tiempo_hash:.6f}"
        )

    # Guardamos los datos reales.
    guardar_csv("resultados_a.csv", resultados)

    # Generamos la primera grafica.
    plt.figure(figsize=(9, 5))

    plt.plot(
        cantidades,
        [fila["lista_ms"] for fila in resultados],
        marker="o",
        label="Lista enlazada",
    )

    plt.plot(
        cantidades,
        [fila["hash_ms"] for fila in resultados],
        marker="s",
        label="Tabla hash",
    )

    plt.title("Busqueda infructuosa: lista vs tabla hash")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo medio por busqueda (ms)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        CARPETA_GRAFICAS / "lista_vs_tabla.png",
        dpi=150,
    )

    plt.close()


def experimento_b() -> None:
    """Mide la busqueda hash para diferentes factores de carga."""
    n = 20000

    factores_objetivo = [0.25, 0.5, 1, 2, 4, 10]

    guias = generar_guias(n)
    inexistentes = generar_guias_inexistentes(
        set(guias), CANTIDAD_BUSQUEDAS
    )

    resultados = []

    print("\nEXPERIMENTO B: FACTOR DE CARGA")
    print("n | m | alfa | hash (ms)")

    for alfa_objetivo in factores_objetivo:
        # Despejamos m de alfa = n / m.
        m = primo_cercano(
            int(n / alfa_objetivo)
        )

        tabla = construir_tabla(guias, m)

        # Comprobamos que las guias existentes se encuentran.
        for guia in guias[:10]:
            assert tabla.buscar(guia) == ESTADO

        # Comprobamos las busquedas infructuosas.
        for guia in inexistentes:
            assert tabla.buscar(guia) is None

        tiempo_hash = medir_busquedas(
            tabla, inexistentes
        )

        fila = {
            "n": n,
            "m": m,
            "alfa": tabla.factor_carga(),
            "hash_ms": tiempo_hash,
        }

        resultados.append(fila)

        print(
            f"{n} | {m} | {fila['alfa']:.4f} | "
            f"{tiempo_hash:.6f}"
        )

    guardar_csv("resultados_b.csv", resultados)

    # Generamos la segunda grafica.
    plt.figure(figsize=(9, 5))

    plt.plot(
        [fila["alfa"] for fila in resultados],
        [fila["hash_ms"] for fila in resultados],
        marker="o",
        label="Tabla hash",
    )

    plt.title("Tiempo de busqueda vs factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo medio por busqueda (ms)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        CARPETA_GRAFICAS / "tiempo_vs_alfa.png",
        dpi=150,
    )

    plt.close()


if __name__ == "__main__":
    # Creamos la carpeta si todavia no existe.
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    experimento_a()
    experimento_b()

    print("\nMediciones y graficas generadas.")
