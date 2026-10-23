# Bitácora del ejercicio: Coffee Shop Analytics

## 1. Objetivo del ejercicio

Construir un prototipo de analítica de ventas para explorar el desempeño de una cadena ficticia de cafeterías. La solución debía permitir consultar indicadores y visualizaciones desde una aplicación web sencilla, además de incorporar una primera aproximación a preguntas formuladas en lenguaje natural.

Se priorizó mantener el alcance controlado, utilizar herramientas gratuitas y trabajar de forma incremental, comprendiendo las decisiones funcionales y técnicas antes de implementarlas.

## 2. Herramientas y entorno

- **Lenguaje:** Python.
- **Aplicación web:** Streamlit.
- **Manipulación de datos:** pandas.
- **Visualizaciones:** Plotly.
- **Lectura de Excel:** openpyxl.
- **Entorno de desarrollo:** VS Code en macOS.
- **Control de versiones:** Git y GitHub.
- **Asistencia durante el desarrollo:** ChatGPT para  generar, revisar y corregir código, analizar las métricas y acompañar la implementación.

 Las dependencias se registraron en `requirements.txt`.

## 3. Fuente y exploración de los datos

Se utilizó el dataset **Coffee Shop Sales**, de Maven Analytics, con información de ventas entre el 1 de enero y el 30 de junio de 2023.

### Características generales

- **Filas:** 149.116.
- **Columnas:** 11.
- **Valores ausentes:** ninguno en las columnas revisadas.
- **Filas duplicadas exactas:** ninguna.
- **Ubicaciones:** Hell's Kitchen, Astoria y Lower Manhattan.

Las columnas incluyen identificador de transacción, fecha y hora, cantidad, tienda, producto, precio unitario, categoría, tipo y detalle del producto.

### Validaciones iniciales

Se revisaron los tipos de datos, el rango de fechas, las categorías, las ubicaciones y los valores de cantidad y precio. También se comparó el número de filas con el número de identificadores de transacción únicos.

El análisis mostró 149.116 filas y 149.116 identificadores únicos. Con base en la estructura observada, se decidió tratar cada fila como una transacción para este prototipo.

## 4. Definiciones analíticas

Se acordaron las siguientes definiciones para mantener consistencia entre los indicadores y las consultas:

- **Ingresos:** suma de `transaction_qty * unit_price` para cada fila.
- **Transacciones:** número de identificadores de transacción únicos.
- **Unidades vendidas:** suma de `transaction_qty`.
- **Ticket promedio:** ingresos totales divididos por el número de transacciones únicas.

### Resultados generales

Los siguientes valores se obtuvieron al analizar el conjunto completo de datos:

- **Ingresos totales:** $698.812,33.
- **Transacciones:** 149.116.
- **Unidades vendidas:** 214.470.
- **Ticket promedio:** $4,69.

Estos resultados se utilizaron como valores de referencia para comprobar el funcionamiento del dashboard.

### Ingresos por categoría

Las cinco categorías con mayores ingresos fueron:

1. **Coffee:** $269.952,45.
2. **Tea:** $196.405,95.
3. **Bakery:** $82.315,64.
4. **Drinking Chocolate:** $72.416,00.
5. **Coffee beans:** $40.085,25.

Coffee y Tea representan conjuntamente aproximadamente el 66,7 % de los ingresos totales.

Este resultado ofrece un primer hallazgo descriptivo, aunque no explica por sí solo las causas del desempeño ni la rentabilidad de las categorías.

### Ingresos por tienda

Los ingresos por ubicación fueron:

- **Hell's Kitchen:** $236.511,17.
- **Astoria:** $232.243,91.
- **Lower Manhattan:** $230.057,25.

Los ingresos de las tres ubicaciones son relativamente próximos durante el período analizado. No se concluyó que una tienda tuviera mayor rentabilidad, ya que el dataset no contiene toda la información de costos necesaria para calcularla.

## 5. Diseño del dashboard

Se construyó una aplicación con Streamlit y Plotly, priorizando una interfaz compacta, clara y fácil de explorar.

### Indicadores principales

El dashboard presenta cuatro indicadores clave:

1. Ingresos totales.
2. Número de transacciones.
3. Unidades vendidas.
4. Ticket promedio.

### Filtros interactivos

Se incorporaron filtros por:

- Rango de fechas.
- Tienda.
- Categoría de producto.

Estos filtros afectan los indicadores y las visualizaciones del dashboard.

### Visualizaciones

- **Ingresos por mes:** gráfico de líneas para observar la evolución temporal.
- **Ingresos por categoría:** gráfico de barras para comparar el aporte de cada categoría.
- **Top 10 productos por ingresos:** gráfico de barras horizontal para facilitar la comparación entre productos.

También se incluyó una sección desplegable para consultar los registros correspondientes a los filtros seleccionados.

## 6. Preguntas en lenguaje natural

Se decidió incorporar una interfaz sencilla de preguntas basada en reglas y palabras clave, sin integrar un modelo de lenguaje ni una API externa.

### Preguntas soportadas inicialmente

- Consultar los ingresos totales.
- Identificar la categoría con mayores ingresos.
- Identificar la tienda con mayores ingresos.
- Consultar los cinco productos con mayores ingresos.
- Consultar ingresos para algunos meses del período disponible.

La implementación identifica patrones de texto, realiza agrupaciones y cálculos con pandas y presenta los resultados en Streamlit.

Cuando la pregunta no coincide con los patrones programados, la aplicación muestra un mensaje de ayuda en lugar de generar una respuesta sin respaldo en los datos.

### Decisión sobre los filtros

Se decidió que el asistente utilizara siempre el conjunto completo de datos, independientemente de los filtros visuales activos en el dashboard.

Por esta razón, las respuestas del asistente pueden diferir de los indicadores filtrados que aparecen