# Introducción

Este documento recopila y organiza toda la información generada durante el **proceso exploratorio realizado en el entorno Jupyter Notebook**.
Su objetivo es documentar de forma clara y estructurada cada uno de los pasos llevados a cabo: la exploración inicial, la unión de datos, la identificación de duplicados, el análisis de valores nulos, la limpieza de datos y las visualizaciones finales.

Los comentarios, observaciones y decisiones que se tomaron a lo largo del notebook han sido reunidos aquí para ofrecer una visión completa del proceso, manteniendo la lógica y detalle del trabajo original, pero presentados en un formato más limpio y coherente.

---

# 1. Exploración inicial

## 1.1 Lectura de CSV

Dos archivos describen el comportamiento de los clientes dentro de un programa de lealtad de una aerolínea.

Ambos CSV comparten la columna **“Loyalty Number”**, por lo que realizamos la unión por esta columna:

1. Verificamos que en ambos archivos la columna es de tipo *int*.
2. Comprobamos valores nulos para evitar pérdida de coincidencias.
3. Un *outer merge* conserva todos los registros, incluso sin coincidencias.

A simple vista, los valores únicos parecen no tener relación directa entre ambos archivos, aunque el rango es amplio.

## 1.2 Unión de CSV

Finalmente, sí existían coincidencias en *Loyalty Number*, ya que el número de filas no aumentó, pero las columnas sí.
Como usamos *outer merge*, todos los clientes (df_sub) tenían al menos una transacción.

Se observan duplicados en *Loyalty Number*, pero corresponden a distintos vuelos, no a duplicación de datos personales.

## 1.3 Exploración de duplicados

Buscamos duplicados considerando los pasos anteriores y encontramos:

* Filas **100% idénticas** (información duplicada que distorsiona conteos).
* Clientes con **más de un registro**.
* Confirmamos que no son duplicados: representan **registros mensuales del mismo cliente**, por lo que no deben eliminarse.

### Eliminación de duplicados exactos

Eliminamos solo las filas duplicadas idénticas al 100%, manteniendo la primera aparición. Necesario para trabajar con datos limpios.

## 1.4 Exploración inicial: `info()` y porcentaje de nulos

Notas:

* **Salary**, **Cancellation Year**, **Cancellation Month** son *float*. Podrían ser *Int64*, pero depende del tratamiento de nulos.
* **Points Accumulated** es float pero con formato 152.0 sin nulos → se mantiene como float.
* **Salary** aparece como float pese a ser enteros (probable efecto de los nulos).
* Datos limpios tras la exploración.

### Observaciones mediante `describe()`

**Distance:**
La mediana es baja respecto a la media → existen distancias largas que elevan la media.

**Flights Booked:**
Mediana de 1 frente a un máximo de 21 → valores atípicos elevan la media (4). Lo normal es un vuelo.

**Flights with Companions / Total Flights:**
Igualmente afectados por valores atípicos.

**Salary:**
Existe un valor negativo y un 25% de nulos.

**Points Accumulated / Redeemed:**
No presentan relación entre máximos.

## 1.5 Exploración de columnas numéricas y categóricas

* La mayoría de vuelos son de baja distancia; los atípicos aparecen por encima de 6000 km.
* Las reservas se concentran entre 0 y 1 con sesgo positivo.
* Salary tiene ligera distribución asimétrica con outliers altos y valores negativos (error).
* Total Flights presenta fuerte asimetría con valores atípicos a partir de 25.
* La mayoría de clientes tiene pocos puntos acumulados, salvo algunos valores dispersos (+600).
* Ciudadanía: todos son de Canadá. Ciudades principales: Toronto, Vancouver, Montreal.

---

# 2. Limpieza de datos

## Salary

1. 25.3% nulos
2. Datos negativos (error evidente)
3. `float64`

Los valores negativos se convierten en absolutos, asumiendo error de registro.

### Decisión sobre Salary

* Mantenemos **NaN** como nulos.
* No imputamos media o mediana porque los outliers distorsionan.
* No eliminamos registros para no perder clientes.
* Mantenemos tipo `float64` (necesario para almacenar NaN).

## Nulos en Cancellation Year / Month

* Ambas son `float64`.
* Interpretamos **NaN = no cancelación**.
* No se modifican los tipos.

Además, añadimos la columna **Cancellation** (booleana):

* `True` si existe valor en *Cancellation Year*.
* `False` si es NaN.

## Limpieza final

Exportamos el CSV limpio a la carpeta **`data_privada`**.

---

# 3. Fase 2: Visualización

## 1. Distribución de vuelos reservados por mes

* No hay grandes diferencias entre años.
* 2018 aumenta reservas en meses 6–8 y 12.
* La mediana es 2 en ambos años; la media es algo mayor por los valores altos.
* Los meses de menor demanda no superan 3 reservas.

## 2. Relación entre distancia y puntos acumulados

El scatter muestra líneas claras más que una nube de puntos:

* A mayor distancia, aumentan los puntos, pero no con la misma intensidad para todos.
* Indica posibles **niveles de fidelización** con distintos sistemas de puntos.
* Con hue por *Loyalty Card*, se observa que las tarjetas de mayor nivel acumulan más puntos por distancia.

## 3. Distribución de clientes por provincia

Provincias con mayor representación:

* **Ontario:** 32.26%
* **British Columbia:** 26.36%
* **Quebec:** 19.71%

## 4. Comparación salarial por nivel educativo

* **Doctor** → salarios más altos, pero con outliers superiores a 400.000 (media ~155.000).
* **Master** → promedio ~130.000.
* **Bachelor** → promedio ~80.000 con outliers bajos.
* **High School** → promedio ~60.000.

Conclusión: **a mayor nivel educativo, mayor salario**.

## 5. Proporción de tarjetas de fidelidad

* **Star:** 45.5%
* **Nova:** 34%
* **Aurora:** ~21%

## 6. Distribución por estado civil y género

* Géneros equilibrados en todas las categorías.
* Principales estados civiles:

  * Married (58%)
  * Single (27%)
  * Divorced (15%)