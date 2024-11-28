# project-da-promo-k-modulo-3-team-2

# Proyecto 3: 

# ¿Hasta que el burnout nos separe?
## (o cómo los datos pueden crear relaciones laborales estables y felices en ABC Corporation)

## 1. Resumen:

Actualmente, el entorno empresarial es cada vez más competitivo y retener el talento es todo un reto para cualquier empresa. Por esto, este proyecto está basado en la toma de  decisiones basadas en datos para optimizar la retención de empleados y aumentar la satisfacción laboral. El objetivo es ofrecer a nuestro cliente ABC Corporation (consultora tecnológica) la fórmula perfecta para que sus empleados sean lo más felices posibles y, así, disminuir la rotación.

Para ello, hemos hecho un EDA de los datos y diseñado la BBDD de la corporación para extraer insights y conclusiones claves que impactan la satisfacción laboral y la retención de empleados. Posteriormente, hemos diseñado experimentos A/B para validar hipótesis críticas y generar recomendaciones accionables. 
Lo que buscamos en este proyecto es optimizar las estrategias de gestión del talento en ABC Corporation.

## 2. Fases del Proyecto

### Fase 1: Análisis Exploratorio de Datos (EDA):

Comprender el conjunto de datos mediante un análisis exploratorio detallado:

- Identificar patrones y relaciones entre las variables.
- Detectar posibles inconsistencias y datos nulos.

### Fase 2: Transformación de Datos:

Limpieza y normalización de los datos:

- Cambiar valores poco intuitivos (e.g., transformar Gender de 0/1 a "Male"/"Female").
- Corregir errores tipográficos y valores negativos en DistanceFromHome.
- Identificar y eliminar columnas redundantes o calculables.

### Fase 3: Diseño de la Base de Datos:

Definición e implementación de la arquitectura de la base de datos:

- Diseño de tablas y relaciones.
- Creación de la base de datos.
- Inserción de datos transformados.

### Fase 4: Prueba A/B:

Validar la hipótesis: “Existe una relación entre satisfacción laboral y rotación de empleados.”

- Grupo A (Control): Satisfacción ≥ 3 (escala 1 a 5).
- Grupo B (Variante): Satisfacción < 3.
  
Análisis estadístico para determinar diferencias significativas en la tasa de rotación (Attrition).

### Fase 5: Creación de una ETL:

Automatización del proceso de:

- Extracción de datos: Desde fuentes como CSV o bases de datos.
- Transformación: Aplicación de reglas de limpieza y normalización.
- Carga: Inserción en la base de datos relacional.

### Fase 6: Reporte de Resultados:

Presentación de un informe con visualizaciones en Python, destacando:

- Confirmación de hipótesis.
- Tendencias relevantes.
- Áreas de mejora.
- Recomendaciones estratégicas.

### Fas 7: Definición de arquetipos: 

- Un día en la vida de los 4 arquetipos.
- Mapping de posicionamiento de los empleados.
- Plan de acción. 

## 3. Los Datos:
   
Las variables del conjunto de datos incluyen información personal, salarial, satisfacción laboral, historial profesional y otros aspectos clave del empleado. Algunas columnas relevantes:

- Attrition: Rotación de empleados (Sí/No).
- DistanceFromHome: Distancia desde casa al trabajo.
- JobSatisfaction: Satisfacción laboral (escala de 1 a 4).
- MonthlyIncome: Ingresos mensuales.
- WorkLifeBalance: Balance entre vida laboral y personal.
  
(Consulta la sección de datos completa en el archivo data_description.md para más detalles).

## 5. Objetivos:

- Consolidar habilidades en Python y SQL.
- Aplicar metodologías ágiles (Scrum) y control de versiones (GitHub).
- Probar hipótesis mediante experimentos A/B.
- Mejorar la comunicación en equipo y la presentación de resultados técnicos.

## 6. Entregables técnicos:

- Una carpeta de notebook con los Jupyter utilizados y dividos por fases.
- Una carpeta con la data utilizada y desarrollada para el proyecto. 
- Un repositorio de GitHub con un historial de commits descriptivos y explicativos. 
- Una carpeta de img con todos los gráficos que se han llevado a cabo durante la ejecución del proyecto. 
- Una carpeta de src con un archivo .py llamado "soporte" con las funciones utilizadas y otra llamado "variables" con las nuevas variables creadas para su desarrollo. 
- Por último, este README que sintetiza el propósito y contenido del proyecto.

