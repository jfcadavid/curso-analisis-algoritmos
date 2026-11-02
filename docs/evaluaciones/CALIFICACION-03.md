# Retroalimentación — Laboratorio 3: Estructuras de datos

**Estudiante:** Juan Felipe Cadavid · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `f389578`

Muy buen trabajo: las estructuras funcionan, las pruebas pasan y el informe se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **93 / 100** |
| **Nota (0–5)** | **4.65** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- Explica bien la colisión con el ejemplo de `10`, `24` y `17` con `m = 7`, y compara encadenamiento con direccionamiento abierto.
- Justifica que la tabla hash no sirve para rangos y propone el árbol de búsqueda.
- Estima la altura del árbol degenerado (cerca de 400.000) y del equilibrado (cerca de 19), con el número de comparaciones de cada uno.
- Declara que las cifras a 5.000.000 de envíos son estimaciones.

**Lo que puede mejorar (y cómo corregirlo):**
- En la comparación entre encadenamiento y direccionamiento abierto, el costo de cada uno queda muy corto (por ejemplo, qué pasa con el rendimiento cuando la tabla se llena).
  → *Cómo corregirlo:* para cada método, diga qué ocurre con la búsqueda cuando el factor de carga sube y si la tabla puede llenarse.
- La estimación de la tabla hash a 5.000.000 de envíos solo repite el valor medido con 50.000 guías, sin explicar por qué ese tiempo se mantendría con una colección 100 veces mayor.
  → *Cómo corregirlo:* explique qué se mantiene fijo en la tabla (el factor de carga) y qué podría cambiar con tanta información (por ejemplo, el uso de la memoria), y diga si eso haría la estimación más alta o más baja.
- La estimación de la lista usa una multiplicación directa desde 50.000 guías, pero usted mismo notó que el último tramo de su curva crece más rápido que la proporción.
  → *Cómo corregirlo:* relacione la estimación con ese comportamiento observado y diga si su cifra es más bien un mínimo o un máximo.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista para una guía inexistente.
- Nombra el supuesto de distribución uniforme y explica que, si todo cae en una casilla, la tabla pasa a costar `Θ(n)`.

**Lo que puede mejorar (y cómo corregirlo):**
- El supuesto se describe como "aproximadamente uniforme", sin decir qué significa para cada guía.
  → *Cómo corregirlo:* diga con qué probabilidad cae una guía en cada casilla y por qué eso lleva a listas de largo `α` en promedio.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` devuelven lo correcto en búsquedas exitosas e infructuosas; la búsqueda usa un ciclo `while`.
- La tabla reutiliza la lista en cada casilla y no usa `dict`, `set` ni `hash()` en las estructuras.
- La colisión forzada con `m = 7` y el factor de carga `3 / 7` están probados, junto con 20 colecciones aleatorias.
- Todas las funciones tienen *type hints*, *docstrings* con `Args` y `Returns`, y dos líneas en blanco entre ellas.

**Lo que puede mejorar (y cómo corregirlo):**
- El tipo `list[dict]` en `guardar_csv` es muy general.
  → *Cómo corregirlo:* precise el tipo, por ejemplo `list[dict[str, float]]`.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de `n` y la segunda seis valores de `α` (de 0,25 a 10).
- Calcula factores de crecimiento (4,08 veces en la lista y 1,02 en la tabla entre 5.000 y 20.000 guías) y los compara con `Θ(n)` y `Θ(1)`.
- Los valores citados coinciden con los que se leen en las gráficas publicadas.

**Lo que puede mejorar (y cómo corregirlo):**
- Para `Θ(1 + α)`, dice que el tiempo creció 4,12 veces mientras `α` creció 40 veces, y lo explica solo con un "costo fijo" sin comprobarlo.
  → *Cómo corregirlo:* compare el crecimiento medido con el que predice `1 + α` entre dos valores de `α` y diga cuánto del tiempo parece ser costo fijo según su propia gráfica.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- El informe sigue el orden pedido, incluye su nombre, las instrucciones para reproducir, los enlaces al código en cada parte y las gráficas incrustadas con ruta relativa que sí se ven.
- Tiene al menos tres commits descriptivos del laboratorio.

**Lo que puede mejorar (y cómo corregirlo):**
- No siguió del todo la estructura de carpetas acordada: el laboratorio aparece duplicado, una vez en `lab3-estructuras-datos/` y otra en `laboratorios/lab3-estructuras-datos/`, con el mismo contenido.
  → *Cómo corregirlo:* deje una sola copia (por ejemplo, con `git rm -r` sobre la carpeta repetida) y mantenga el informe en la que conserve.
- Las instrucciones suponen un entorno `.venv` que usted mismo dice no haber usado.
  → *Cómo corregirlo:* describa el entorno que realmente utilizó y cómo crearlo.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y `medicion.py` corre completo y genera las dos gráficas y los archivos de datos. Las estructuras devuelven los mismos resultados en lista y tabla.
