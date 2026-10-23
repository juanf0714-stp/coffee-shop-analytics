# Bitácora del ejercicio: Coffee Shop Analytics

## 1. Objetivo del ejercicio

Construir un prototipo pequeño de analítica de ventas para explorar el
desempeño de una cadena ficticia de cafeterías. La solución debía
permitir consultar indicadores y visualizaciones desde una aplicación
web sencilla e incorporar una primera aproximación a preguntas
formuladas en lenguaje natural.

Se priorizó mantener el alcance controlado, utilizar herramientas
gratuitas y trabajar de forma incremental, entendiendo las decisiones
funcionales y técnicas antes de implementarlas.

## 2. Herramientas y entorno

-   **Lenguaje:** Python.
-   **Aplicación web:** Streamlit.
-   **Manipulación de datos:** pandas.
-   **Visualizaciones:** Plotly.
-   **Lectura de Excel:** openpyxl.
-   **Entorno de desarrollo:** VS Code en macOS.
-   **Control de versiones:** Git y GitHub.
-   **Asistencia durante el desarrollo:** ChatGPT para definir el
    alcance, razonar sobre las métricas y acompañar la implementación
    paso a paso. Se decidió no utilizar Codex para mantener el proceso
    simple y conservar el control directo sobre los cambios.

El entorno virtual se creó en `.venv`. Las dependencias se registraron
en `requirements.txt`.

## 3. Fuente y exploración de los datos

Se utilizó el dataset **Coffee Shop Sales** de Maven Analytics, con
información de ventas entre el 1 de enero y el 30 de junio de 2023.

El archivo inspeccionado contiene:

-   **149.116 filas**
-   **11 columnas**
-   **0 valores ausentes** en las columnas revisadas
-   **0 filas duplicadas exactas**
-   Tres ubicaciones: Hell's Kitchen, Astoria y Lower Manhattan.

Las columnas incluyen identificador de transacción, fecha y hora,
cantidad, tienda, producto, precio unitario, categoría, tipo y detalle
del producto.

### Validaciones iniciales

Se revisaron los tipos de datos, el rango de fechas, las categorías, las
ubicaciones y los valores de cantidad y precio. También se comparó el
número de filas con el número de identificadores de transacción únicos.

El análisis mostró 149.116 filas y 149.116 identificadores únicos. Con
base en la estructura observada, se decidió tratar cada fila como una
transacción para este prototipo. Algunas filas representan más de una
unidad vendida, por lo que el número de unidades no equivale al número
de transacciones.

## 4. Definiciones analíticas

Se acordaron las siguientes definiciones para mantener consistencia
entre los indicadores y las consultas:

-   **Ingresos:** suma de `transaction_qty × unit_price` para cada fila.
-   **Transacciones:** número de identificadores de transacción únicos.
-   **Unidades vendidas:** suma de `transaction_qty`.
-   **Ticket promedio:** ingresos totales divididos por el número de
    transacciones únicas.

Con el conjunto completo de datos, los valores de referencia obtenidos
fueron:

  Indicador                Resultado
  ------------------- --------------
  Ingresos              \$698.812,33
  Transacciones              149.116
  Unidades vendidas          214.470
  Ticket promedio             \$4,69

Estos resultados se utilizaron como comprobación inicial del dashboard.

### Ingresos por categoría

  Categoría                  Ingresos
  -------------------- --------------
  Coffee                 \$269.952,45
  Tea                    \$196.405,95
  Bakery                  \$82.315,64
  Drinking Chocolate      \$72.416,00
  Coffee beans            \$40.085,25

Coffee y Tea representan conjuntamente aproximadamente el 66,7 % de los
ingresos totales. Esta observación ofrece un primer insight descriptivo,
aunque por sí sola no explica las causas ni la rentabilidad de esas
categorías.

### Ingresos por tienda

  Tienda                  Ingresos
  ----------------- --------------
  Hell's Kitchen      \$236.511,17
  Astoria             \$232.243,91
  Lower Manhattan     \$230.057,25

Los ingresos se encuentran relativamente próximos entre las tres
ubicaciones durante el período observado. No se concluyó que una tienda
tuviera mejor rentabilidad, porque el dataset utilizado no aporta todos
los costos necesarios para calcularla.

## 5. Diseño del dashboard

Se construyó una aplicación con Streamlit y Plotly, priorizando una
interfaz compacta y fácil de explorar.

### Indicadores principales

1.  Ingresos totales.
2.  Número de transacciones.
3.  Unidades vendidas.
4.  Ticket promedio.

### Filtros

Se incorporaron filtros por rango de fechas, tienda y categoría de
producto. Los filtros afectan los KPI y las visualizaciones del
dashboard.

### Visualizaciones

-   **Ingresos por mes:** gráfico de líneas para observar la evolución
    temporal.
-   **Ingresos por categoría:** gráfico de barras para comparar
    categorías.
-   **Top 10 productos por ingresos:** gráfico de barras horizontal para
    facilitar la comparación entre productos.

También se incluyó una sección desplegable para consultar los datos
filtrados.

## 6. Preguntas en lenguaje natural: alcance inicial

Se decidió añadir una interfaz sencilla de preguntas basada en reglas y
palabras clave, sin integrar un modelo de lenguaje ni una API externa.

La primera versión reconoce preguntas relacionadas con ingresos totales,
categorías con mayores ingresos, tiendas con mayores ingresos, productos
con mayores ingresos y algunos meses del período disponible.

La implementación identifica patrones de texto, ejecuta agrupaciones y
cálculos con pandas, y presenta los resultados en Streamlit. Si la
pregunta no coincide con los patrones programados, muestra un mensaje de
ayuda en lugar de inventar una respuesta.

### Decisión sobre los filtros

Se decidió que las preguntas utilizaran siempre el conjunto completo de
datos, independientemente de los filtros visuales activos en el
dashboard. Por tanto, las respuestas del asistente pueden diferir de los
KPI filtrados que aparecen en la parte superior.

### Limitaciones reconocidas

-   El mecanismo se basa en palabras clave y patrones predefinidos, no
    en comprensión general del lenguaje.
-   Solo reconoce un conjunto limitado de formulaciones y meses.
-   El período de datos termina en junio de 2023.
-   Los resultados son descriptivos; no permiten inferir causalidad.
-   El ticket promedio y las transacciones se calculan según las
    definiciones acordadas para la estructura observada del dataset.

## 7. Pasos de implementación

1.  Crear la carpeta del proyecto y configurar un entorno virtual de
    Python.
2.  Instalar Streamlit, pandas, Plotly y openpyxl.
3.  Inspeccionar el Excel mediante un script de Python.
4.  Revisar estructura, calidad básica y métricas de referencia.
5.  Construir el dashboard inicial con KPI, filtros y visualizaciones.
6.  Probar la aplicación localmente y comprobar los valores de
    referencia.
7.  Definir el alcance del asistente de preguntas.
8.  Añadir reglas para reconocer preguntas y calcular respuestas sobre
    los datos.
9.  Probar las preguntas previstas y comprobar que la aplicación
    funcionara correctamente.
10. Preparar `requirements.txt`, `.gitignore` y `README.md`.
11. Inicializar Git, crear el primer commit y publicar el proyecto en
    GitHub.
12. Excluir el entorno virtual y el archivo Excel del repositorio,
    dejando documentado cómo obtener el dataset original.

## 8. Publicación y reproducibilidad

Repositorio: https://github.com/juanf0714-stp/coffee-shop-analytics

El proyecto se publicó en la rama `main`. Se incluyeron los archivos de
aplicación, el script de inspección, las dependencias, el README y
`.gitignore`.

Se excluyeron `.venv/` y `data/` para evitar subir el entorno virtual y
redistribuir el archivo de datos sin confirmar sus condiciones de uso.
El README explica cómo descargar el dataset desde la fuente original,
colocarlo en `data/Coffee Shop Sales.xlsx`, instalar las dependencias y
ejecutar la aplicación.

## 9. Decisiones de alcance

Para mantener el prototipo pequeño y viable, se decidió:

-   No incorporar una API de IA ni un servicio de pago.
-   No utilizar Codex para la implementación.
-   No añadir infraestructura o servicios de despliegue en esta etapa.
-   Priorizar métricas interpretables, visualizaciones directas y
    consultas limitadas pero verificables.
-   Documentar las limitaciones en lugar de presentar el prototipo como
    un asistente conversacional general.

## 10. Estado y siguientes pasos

### Estado alcanzado

-   Dashboard local funcional.
-   KPI y visualizaciones implementados.
-   Filtros interactivos.
-   Primera versión del asistente de preguntas basada en reglas.
-   Dependencias y guía de ejecución documentadas.
-   Código publicado en GitHub.

### Pendiente

-   Verificar que las instrucciones del README permitan a otra persona
    reproducir la aplicación desde cero.
-   Confirmar las condiciones de descarga y uso del dataset según la
    fuente original.
-   Si el alcance de la prueba lo requiere, considerar más adelante una
    forma de desplegar la aplicación. No se considera necesario para la
    versión actual.

------------------------------------------------------------------------

**Nota:** esta bitácora documenta el proceso, las decisiones y los
resultados observados durante el ejercicio. Las cifras corresponden al
análisis del archivo utilizado y no deben interpretarse como información
actual de un negocio real.
