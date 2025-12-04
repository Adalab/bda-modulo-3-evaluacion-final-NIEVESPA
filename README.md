# ✈️ EVALUACIÓN FINAL MÓDULO 3: TRANSFORMACIÓN DE DATOS

Este repositorio contiene el ejercicio para la **Evaluación Final del Módulo 3: Transformación de Datos**, como parte del Bootcamp de **Data Analytics (Adalab)**.  
El objetivo es aplicar técnicas de **exploración**, **limpieza**, **análisis estadístico** y **visualización** de datos utilizando Python.

---

## 📦 DATOS UTILIZADOS

El proyecto se basa en dos archivos CSV relacionados mediante la columna **`Loyalty Number`**.

### **1. CUSTOMER FLIGHT ACTIVITY.csv**  
Información mensual sobre la actividad de vuelo del cliente:

- Loyalty Number  
- Year, Month  
- Flights Booked, Flights with Companions, Total Flights  
- Distance  
- Points Accumulated, Points Redeemed  
- Dollar Cost Points Redeemed  

### **2. CUSTOMER LOYALTY HISTORY.csv**  
Incluye datos demográficos y de membresía:

- Loyalty Number  
- Country, Province, City, Postal Code  
- Gender, Education, Salary, Marital Status  
- Loyalty Card, CLV  
- Enrollment Type, Enrollment Year/Month  
- Cancellation Year/Month  

---

# 🔍 FLUJO DE TRABAJO

## 🧩 FASE 1 — Exploración y Limpieza

### **1.1 Análisis inicial**
- Verificación de tipos de datos  
- Estadísticas básicas  
- Detección de valores nulos  
- Identificación de outliers  

### **1.2 Limpieza de datos**
- Conversión de tipos  
- Tratamiento de nulos  
- Corrección de inconsistencias  

### **1.3 Integración**
- Unificación de datasets mediante la clave **`Loyalty Number`**

---

## 📊 FASE 2 — Visualización y Análisis

El análisis incluye gráficos que permiten responder a:

- **2.1** Distribución mensual de vuelos reservados  
- **2.2** Relación entre distancia volada y puntos acumulados  
- **2.3** Distribución de clientes por provincia/estado  
- **2.4** Comparación del salario medio por nivel educativo  
- **2.5** Proporción de tipos de tarjeta de fidelidad  
- **2.6** Distribución combinada por estado civil y género  

Las visualizaciones generadas durante el análisis y mostradas en este README se encuentran en `images/`.

---

# 🧱 ARQUITECTURA DEL PROYECTO

├── Files/ # Datos y documentos fuente
│ ├── Customer Flight Activity.csv
│ ├── Customer Loyalty History.csv
│ └── evaluacion-final.md
│
├── images/ # Visualizaciones generadas
│ ├── distribuciones.png
│ ├── correlacion.png
│ └── boxplots.png
│
├── src/ # Código fuente del proyecto
│ ├── pycache/ # Caché de Python
│ ├── init.py # Inicializa el paquete
│ ├── soporte_transformacion.py # Funciones auxiliares para EDA y limpieza
│ └── bda-modulo-3-evaluacion-final-... # Script/notebook de análisis
│
├── README.md # Documentación principal


---

# 🛠️ MÓDULO DE SOPORTE: `soporte_transformacion.py`

Este módulo contiene funciones desarrolladas para agilizar y estructurar el análisis exploratorio:

- Identificación de duplicados  
- Análisis rápido: nulos, tipos de variables, estadísticas  
- Histogramas, KDE, boxplots y otras visualizaciones  
- Comparaciones entre columnas  
- Limpieza específica y utilidades de transformación  

Para usarlo en un notebook:

```python
from src.soporte_transformacion import *
