
"""Pruebas de la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash


# Prueba 1: busquedas exitosas e infructuosas.
lista = ListaEnlazada()
tabla = TablaHash(7)

lista.insertar(1000000010, "en bodega")
tabla.insertar(1000000010, "en bodega")

assert lista.buscar(1000000010) == "en bodega"
assert tabla.buscar(1000000010) == "en bodega"

assert lista.buscar(1000000099) is None
assert tabla.buscar(1000000099) is None


# Prueba 2: colision forzada con m = 7.
tabla_colisiones = TablaHash(7)

for guia in (10, 24, 17):
    tabla_colisiones.insertar(guia, "en bodega")

assert tabla_colisiones.hash(10) == 3
assert tabla_colisiones.hash(24) == 3
assert tabla_colisiones.hash(17) == 3

assert tabla_colisiones.buscar(10) == "en bodega"
assert tabla_colisiones.buscar(24) == "en bodega"
assert tabla_colisiones.buscar(17) == "en bodega"
assert tabla_colisiones.buscar(99) is None

assert tabla_colisiones.casillas[3].tamano == 3
assert tabla_colisiones.factor_carga() == 3 / 7


# Prueba 3: veinte colecciones aleatorias.
azar = random.Random(42)

for _ in range(20):
    lista = ListaEnlazada()
    tabla = TablaHash(101)

    # Generamos 50 guias diferentes de diez digitos.
    guias = azar.sample(range(10**9, 10**10), 50)

    # Insertamos los mismos datos en ambas estructuras.
    for guia in guias:
        estado = azar.choice(
            ["en bodega", "en reparto", "entregado"]
        )
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    # Comprobamos las 50 guias existentes.
    for guia in guias:
        assert lista.buscar(guia) == tabla.buscar(guia)
        assert lista.buscar(guia) is not None

    # Generamos y comprobamos 10 guias inexistentes.
    inexistentes = []

    while len(inexistentes) < 10:
        guia = azar.randint(10**9, 10**10 - 1)

        if guia not in guias and guia not in inexistentes:
            inexistentes.append(guia)

    for guia in inexistentes:
        assert lista.buscar(guia) is None
        assert tabla.buscar(guia) is None


print("Todas las pruebas pasaron correctamente.")