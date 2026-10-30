# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Juan Felipe Cadavid · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `cfc6bf0`

Muy buen trabajo: el código es correcto y el informe responde casi todo lo pedido.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 21 / 25 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **86 / 100** |
| **Nota (0–5)** | **4.30** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar en n = 50 y lo respalda con sus tiempos.
- Compara con el máximo de un arreglo, plantea `T(n) = 2T(n/2) + Θ(1)` y concluye que dividir no mejora.
- Recomienda divide y vencerás, declara que los tiempos a 1.000.000 son estimaciones y no usa una regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 3 explique también por qué la ventaja tarda en aparecer (costo de las llamadas recursivas) con más datos que un solo par de tamaños.
- En la pregunta 4 diga con claridad que el costo de combinar es lo que decide si dividir sirve: en el subarreglo cuesta `Θ(n)` y en el máximo solo `Θ(1)`.
- Su estimación parte del tamaño 4000, que usted mismo señala como poco confiable; sería mejor justificar por qué se escoge ese punto.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Explica de dónde sale cada término: dos subproblemas de tamaño `n/2` y un caso cruzado que cuesta `Θ(n)`.
- Aplica el método maestro y verifica que `n^(log₂ 2) = n` tiene el mismo orden que `f(n)`, así que es el caso 2: `Θ(n log n)`.
- Justifica `Θ(n²)` de la fuerza bruta con la suma `n(n+1)/2`.

**Lo que puede mejorar:**
- Resuelva la recurrencia también paso a paso (por ejemplo con el árbol de recursión) y no solo con el método maestro.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en la serie de ocho días y en todos los casos pedidos; coinciden en 20 listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y no modifica la lista recibida.
- Tiene type hints y docstrings, y el estilo de código es limpio.

**Lo que puede mejorar:**
- `pruebas.py` no incluye un caso con ceros ni con empates para comprobar el desempate; sería un buen complemento.

## 4. Calidad del análisis de las gráficas (21 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con siete tamaños.
- Calcula el factor al duplicar n (3,99 en fuerza bruta, 1,71 en divide y vencerás) y lo contrasta con lo esperado (4 y 2,22).
- Reconoce con honestidad que el dato de 8000 en divide y vencerás parece raro.

**Lo que puede mejorar:**
- No comenta que la fuerza bruta tampoco se cuadruplica entre 4000 y 8000 (en la gráfica pasa de cerca de 1,2 s a cerca de 2,5 s), lo que también pone en duda sus estimaciones.
- Algunas afirmaciones se apoyan en la consola más que en lo que se lee en la gráfica.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- El informe sigue el orden pedido, la gráfica se ve y cada parte práctica enlaza su código.
- Incluye su nombre y los comandos para ejecutar pruebas y medición.

**Lo que puede mejorar:**
- No siguió la estructura acordada: el laboratorio está duplicado, una copia en `lab2-divide-y-vencer/` y otra idéntica en `laboratorios/lab2-divide-y-vencer/`. Debe quedar solo una.
- Solo hay 2 commits del laboratorio, con el mismo mensaje; se piden al menos 3 commits descriptivos.
- El informe no cuenta cómo midió (que repitió 3 veces y usó la mediana), aunque el código sí lo hace.
- El comando para activar el entorno solo sirve en Windows; indique también el de macOS/Linux.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos dan la misma suma en listas aleatorias y la medición genera la gráfica sin errores.

## Para el próximo laboratorio
- Deje el laboratorio en una sola carpeta, con commits pequeños y mensajes distintos que describan cada avance.
- Agregue una tabla con todos los tiempos medidos para respaldar sus afirmaciones.
- Revise los valores que se salen de lo esperado y explíquelos con sus datos antes de hacer estimaciones.
- Describa en el informe cómo midió (repeticiones y mediana).
