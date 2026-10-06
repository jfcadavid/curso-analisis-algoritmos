# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Juan Felipe Cadavid Zabala · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `e4582da`

Muy buen trabajo: el código es correcto y el informe cubre todas las partes.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 17 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **86 / 100** |
| **Nota (0–5)** | **4.30** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Separa bien corrección y tiempo, y nombra la restricción incumplida: la ventana de 4 horas.
- Explica que un servidor más rápido no cambia la forma en que crece insertion sort (unas 3.600 veces más trabajo con 60 veces más datos).
- Da un segundo ejemplo propio con datos y restricción (500.000 comparendos y una consulta de menos de un segundo).
- En la Parte 2 relaciona tiempo con energía acumulada cada madrugada, identifica al paciente y al operador como afectados, dice quién asume el costo y discute que el orden decide a quién se llama primero.

**Lo que puede mejorar:**
- En la dimensión ambiental no da ninguna cifra ni estimación (horas de servidor, ahorro posible); se queda en la idea general.
- Los dos perjuicios podrían ser más concretos, con una persona identificable y una consecuencia puntual en cada uno.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define mejor, peor y promedio sobre entradas del mismo tamaño `n`, justifica que usaría el peor caso por la ventana estricta y deja su predicción antes de medir.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el método maestro verificando que es el caso 2: `Θ(n log n)`.
- La tabla de complejidades por caso es correcta.

**Lo que puede mejorar:**
- La tabla línea a línea de insertion sort es incompleta: no indica el costo de cada línea ni suma los costos para llegar a la expresión final, y solo la usa para el peor caso.
- Al describir el caso promedio no explica de dónde sale el factor aproximado de `n²/4`.

## 3. Corrección de la implementación (17 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, no cambian la lista recibida y cuentan solo comparaciones entre elementos. No usa `sorted()` ni `sort()`.
- Los tres generadores producen lotes del tamaño pedido, con valores distintos y semilla reproducible.
- Los datos tienen *type hints* y *docstrings* en las funciones principales.

**Lo que puede mejorar:**
- Falta una segunda línea en blanco entre `insertion_sort` y `merge_sort`, y hay un salto de línea antes de un operador.
- La función interna `ordenar` de merge sort no tiene *docstring*.

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas tienen título, ejes con unidades y leyenda, y los escenarios aparecen en los mismos ejes.
- Identifica correctamente el escenario C como peor caso, B como mejor y A como cercano al promedio, con cifras tomadas de sus mediciones.
- Contrasta con su predicción y con las complejidades calculadas, y la conclusión sobre merge sort sale de su propia gráfica.

**Lo que puede mejorar:**
- En 4.3 la estimación para 1.200.000 registros (26 horas y 11,3 segundos) no explica cómo hizo la extrapolación; solo da el resultado. Debía escribir el razonamiento.
- La respuesta al servidor del doble de velocidad se apoya en la estimación y no cita explícitamente la gráfica ni el tamaño medido.
- Tiene una sola medición por tamaño; repetirla y promediar daría curvas más confiables.
- Solo discute la memoria como consideración adicional; podía mencionar estabilidad o el riesgo de que el escenario B cambie.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Carpeta y archivos bien ubicados; el informe sigue el orden pedido, con gráficas visibles y enlaces al código en cada parte.
- Tiene diez commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Las instrucciones para activar el entorno solo sirven en Windows; conviene indicar también el comando para macOS/Linux.
- Varios commits seguidos tienen el mismo mensaje; conviene que cada uno describa lo que cambió.

## ¿El código funciona?
Sí. Los dos programas corren sin errores, los algoritmos ordenan bien en mis pruebas y se generan las tres gráficas.

## Para el próximo laboratorio
- Escriba el razonamiento de cada extrapolación (de qué tamaño parte y por qué factor multiplica).
- Complete las tablas línea a línea con el costo de cada instrucción y súmelas.
- Dé cifras aproximadas cuando hable de impacto ambiental.
- Repita las mediciones y grafique el promedio.
- Revise PEP 8 y agregue *docstring* también a las funciones internas.
