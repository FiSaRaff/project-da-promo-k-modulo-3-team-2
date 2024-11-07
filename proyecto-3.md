# Proyecto 3. Transformando el Talento: Análisis de Datos para Retener y Potenciar Empleados en ABC Corporation.

{% hint style="info" %}
Recuerda que este proyecto es un ejercicio académico, ante la duda pregunta a tus profesores. 
{% endhint %}

## 1. Resumen.

En el entorno empresarial altamente competitivo de hoy en día, la toma de decisiones informadas es esencial para el éxito a largo plazo. La retención de empleados y la satisfacción en el trabajo son cuestiones críticas para cualquier organización, ya que afectan directamente a la productividad, la moral y la rentabilidad.

Con el objetivo de reducir la rotación de empleados y mejorar la satisfacción en el trabajo la empresa ABC Corporation, nos han contratado para desarrollar un proyecto de análisis de datos y experimentación A/B de gran alcance. Nuestra misión es identificar factores clave que influyen en la satisfacción en el trabajo y, en última instancia, en la retención de empleados.

En este proyecto, presentaremos los resultados de nuestro análisis exploratorio de datos, diseñaremos un experimento A/B para probar hipótesis críticas y analizaremos los resultados para proporcionar a ABC Corporation información valiosa que informe sus decisiones estratégicas. 


**¿Quién es ABC Corporation?**

ABC Corporation, fundada en 1980 en California, es una consultora tecnológica especializada en ofrecer soluciones de inteligencia artificial (IA) y aprendizaje automático (*machine learning*) a empresas de diversos sectores. Su enfoque principal radica en automatizar y optimizar procesos empresariales mediante tecnologías de vanguardia.

La empresa se distingue por tener un equipo multidisciplinario que abarca expertos en UX/UI, marketing, analistas, científicos de datos y otros campos relevantes. Esta diversidad permite una sinergia única entre conocimientos técnicos especializados y perspectivas variadas, lo que les permite ofrecer soluciones personalizadas adaptadas a las necesidades individuales de cada cliente. 

EL último proyecto donde ha estado implicado la empresa ha sido la optimización de procesos de selección de personal, para ello la empresa ha desarrollado una plataforma de selección inteligente, donde los empleados pueden analizar automáticamente los CV de las posibles candidatas, identificar sus habilidades clave para finalmente clasificar los candidatos según si idoneidad para determinados roles. Además, han creado un sistema de recomendación para sugerir a los reclutadores los mejores candidatos. 

**Fases del proyecto:**

- **Fase 1: Análisis Exploratorio de Datos(EDA).**  

    Antes de llevar a cabo el proyecto, el experimento A/B y plantear hipótesis, es crucial comprender mejor el conjunto de datos y sus características. Para ello deberás hacer un análisis exploratorio detallado del conjunto de datos para familiarizarte con ellos y entender que  información tenemos.

- **Fase 2: Transformación de los datos.**  

    Esto puede incluir la limpieza de datos, la normalización, la conversión de tipos de datos y la aplicación de reglas empresariales específicas. Las transformaciones se realizarán mediante funciones de Python que se aplicarán a los datos extraídos. Algunas de las transformaciones que podrías hacer son: 

    - La columna `Gender` tiene valores de 0 y 1, los cuales son pocos intutitivos. Los podrías reemplazar por "Male" y "Female", o "M" y "F" por ejemplo. 

    - Algunas columnas, como la columna `DailyRate` son columnas que incluyen valores numéricos decimales. Pero en el DataFrame aparece como columna de tipo string. Deberás hacer los cambios necesarios para convertirla en columna de tipo numérica. 

    - Evaluar si hay valores duplicados y analizar si tiene sentido eliminarlos o mantenerlos. 

    - Valores inconsistentes, por ejemplo en la columna `DistanceFromHome` tiene valores negativos. 

    - Errores tipográficos en algunos valores de las columnas categóricas. Por ejemplo, en la columna `MaritalStatus` en vez de "Married" en algunas filas aparece "Marreid". 

    - Columnas redundantes, es decir, columnas que nos dan la misma información expresada de forma diferente. 

- **Fase 3: Diseño de BBDD e Insercción de los Datos (estructura).** 

    En esta fase tiene como objetivo la creación y la inserción de datos en una base de datos desde el punto de vista de su arquitectura o estructra, es decir, definir como seria su BBDD final. Los aspectos principales de esta fase del proyecto son: 

    1. **Diseño de la Estructura de la Base de Datos:** Deberás definir la estructura de la base de datos. Esto incluye identificar las tablas necesarias y sus relaciones, así como definir las claves primarias y foráneas.

    2. **Creación de la Base de Datos:** Deberás crear la base de datos utilizando las herramientas aprendidas en el módulo 2. 

    3. **Inserción de Datos Iniciales:** Deberás insertar los datos de los empleados de la empresa en la base de datos. 


- **Fase 4: Problema de A/B Testing.**

    El objetivo de esta fase es determinar si existe una relación entre el nivel de satisfacción en el trabajo y la rotación de empleados, y si es así, cuál es la magnitud de esa relación. Partiremos de la siguiente hipótesis, "Existe una relación entre el nivel de satisfacción en el trabajo y la rotación de empleados en la empresa. Se sospecha que los empleados con niveles de satisfacción más bajos tienen una mayor probabilidad de dejar la empresa". Para ello deberéis crear una columna nueva en base al nivel de satisfacción en el trabajo para crear dos grupos, las condiciones para crear los grupos son: 

    - **Grupo A (Control):** Empleados con un nivel de satisfacción en el trabajo igual o superior a 3 en una escala de 1 a 5.

    - **Grupo B (Variante):** Empleados con un nivel de satisfacción en el trabajo inferior a 3 en la misma escala.

    La **métrica principal** que debes usar es la tasa de rotación de empleados (`Attrition`) en cada grupo. Recordemos que,  en esta columna, "No" indica que el empleado no ha dejado la empresa (sin rotación), mientras que "Yes" indica que el empleado ha dejado la empresa (con rotación). 

    Por lo tanto, los pasos que deberás seguir en esta fase son: 

    1. Divide a los empleados en los grupos A y B según los criterios establecidos.

    2. Calcula la tasa de rotación (porcentaje de empleados que dejaron la empresa) en cada grupo.

    3. Realiza un análisis estadístico para determinar si hay una diferencia significativa en la tasa de rotación entre los grupos A y B.

    4. Analiza los resultados.

    5. Calcular la magnitud de esta relación utilizando estadísticas como la diferencia de medias por ejemplo.

- **Fase 5: Creación de una ETL.**  

    En esta fase del proyecto, deberás crear un archivo .py que llevará a cabo la extracción, transformación y carga (ETL) de datos. El objetivo de esta etapa es automatizar la inserción de datos en la base de datos relacional y garantizar que la información se actualice de manera consistente y también automatizar el proceso de transformación de la información antes de la insercción en la BBDD. Los pasos que deberás seguir en esta fase son:

    1. **Extracción de Datos:** En esta primera parte de la ETL, las alumnas desarrollarán una función para extraer datos desde las fuentes de datos previamente definidas. Estas fuentes pueden incluir hojas de cálculo, archivos CSV, bases de datos externas o cualquier otro formato de datos relevante. El objetivo es obtener datos frescos y relevantes que se cargarán en la base de datos.

    2. **Transformación de Datos:** Deberás desarrollar una función (o varias) para aplicar todas las transformaciones necesarias para garantizar la integridad y la calidad de los datos (estas transformaciones serán las mismas que en la fase 2).

    3. **Creación de la Base de Datos:** En esta etapa, crearás una función con el código para la creación de la BBDD diseñada en la fase 3.

    4. **Carga de Datos:** Después de la creación de las tablas, desarrollaras funciones que permitan la inserción de datos transformados en la base de datos. Esto garantizará que la base de datos esté siempre actualizada con la información más reciente.

    **NOTA** Todo este código deberá estar en funciones y en archivos `.py`.

- **Fase 6: Reporte de los resultados.**

    El objetivo de esta fase será proporcionar a ABC Corporation un informe detallado del contexto general de la empresa utilizando visualizaciones en Python. Este informe permitirá una comprensión más profunda de la situación actual y servirá como base para la toma de decisiones informadas.

    Deberás generar un informe completo que incluirá las visualizaciones junto con análisis descriptivos (se presentará el día de la demo). Las visualizaciones ayudarán a resaltar tendencias, áreas de mejora y fortalezas dentro de la empresa.

## 2. Los Datos.

Las columnas que os encontraréis en el DataFrame son:

1. `Age`: La edad del empleado.

2. `Attrition`: Indica si el empleado ha dejado la empresa ("No" significa que no ha dejado la empresa y "Yes" significa que ha dejado la empresa).

3. `BusinessTravel`: Describe la frecuencia de los viajes relacionados con el trabajo del empleado (por ejemplo, "Travel_Rarely" para raramente).

4. `DailyRate`: La tarifa diaria del empleado.

5. `Department`: El departamento en el que trabaja el empleado (por ejemplo, "Research & Development", "Sales", etc.).

6. `DistanceFromHome`: La distancia desde el hogar del empleado hasta su lugar de trabajo.

7. `Education`: Nivel de educación del empleado (generalmente en una escala del 1 al 5).

8. `EducationField`: El campo de educación del empleado.

9. `EmployeeCount`: Un contador que generalmente es 1 y se usa para contar empleados.

10. `EmployeeNumber`: Un número de identificación único para el empleado.

11. `EnvironmentSatisfaction`: Nivel de satisfacción del empleado en relación con su entorno de trabajo. Con valores que estan comprendidos entre el 1 y el 4, siendo el 4 el nivel de máxima satisfacción. 

12. `Gender`: El género del empleado. Donde 0 corresponde con "hombre" y 1 con "mujer". 

13. `HourlyRate`: La tarifa por hora del empleado.

14. `JobInvolvement`: Nivel de implicación del empleado en su trabajo.

15. `JobLevel`: Nivel jerárquico del empleado en la empresa.

16. `JobRole`: El rol o puesto de trabajo del empleado.

17. `JobSatisfaction`: Nivel de satisfacción del empleado con su trabajo.

18. `MaritalStatus`: El estado civil del empleado (por ejemplo, "Single", "Married", etc.).

19. `MonthlyIncome`: Ingresos mensuales del empleado.

20. `MonthlyRate`: Tasa mensual del empleado.

21. `NumCompaniesWorked`: Número de compañías en las que el empleado ha trabajado.

22. `Over18`: Indica si el empleado es mayor de 18 años.

23. `OverTime`: Indica si el empleado trabaja horas extras ("Yes" para sí o "No" para no).

24. `PercentSalaryHike`: El porcentaje de aumento salarial del empleado.

25. `PerformanceRating`: Calificación de rendimiento del empleado.

26. `RelationshipSatisfaction`: Nivel de satisfacción en las relaciones interpersonales del empleado.

27. `StandardHours`: Las horas estándar de trabajo.

28. `StockOptionLevel`: Nivel de opciones de compra de acciones del empleado.

29. `TotalWorkingYears`: Total de años de experiencia laboral del empleado.

30. `TrainingTimesLastYear`: Número de veces que el empleado recibió capacitación el año pasado.

31. `WorkLifeBalance`: Equilibrio entre trabajo y vida personal del empleado.

32. `YearsAtCompany`: Años que el empleado ha trabajado en la empresa actual.

33. `YearsInCurrentRole`: Años que el empleado ha estado en su puesto actual.

34. `YearsSinceLastPromotion`: Años desde la última promoción del empleado.

35. `YearsWithCurrManager`: Años que el empleado ha estado bajo la supervisión del actual gerente.

36. `SameAsMonthlyIncome`:  Ingresos mensuales del empleado.

37. `DateBirth`: Año de nacimiento del empleado (teniendo en cuenta que los datos fueron recogidos en el 2023)

38. `Salary`: Salario de los empleados.

39. `RoleDepartament`: El departamento y el rol del empleado.

40. `NumberChildren`: Número de hijos de los empleados.

41. `RemoteWork`: Si el empleado puede teletrabajar o no.




## 3. Objetivos

1. Consolidar los conocimientos de Python y SQL.

2. Utilizar control de versiones en equipo para aprender las ventajas y conflictos que genera.

3. Implementar Scrum como marco de referencia para el desarrollo del producto, basándonos siempre en los valores de *Agile* como puntos clave del trabajo en equipo y la mejora continua.

4. Mejorar la comunicación entre los miembros del equipo.

5. Mejorar vuestras habilidades de comunicación en público al exponer el proyecto en la sesión final.


## 4. Planificación del proyecto.

### 4.1. *sprints*

Para la realización de este proyecto trabajaremos en 2 *sprints* (2 iteraciones). Siguiendo los principios ágiles, estableceremos pequeños ciclos iterativos de forma que al final de cada uno generemos valor perceptible por nuestros usuarios. Dedicaremos el primer día a la planificación del *sprint* (*sprint planning*) y el resto a trabajar en el desarrollo del proyecto. Al final de cada *sprint* haremos un *Sprint Review* del proyecto para presentar los resultados conseguidos y recoger *feedback*.

También haremos una retro corta revisando los *working agreements* que hemos acordado al inicio del proyecto y añadiendo cualquier otro *feedback* que nos permita mejorar el proyecto.

Al final del  segundo **sprint** (que coincidirá con el final del proyecto y del módulo), haremos una sesión de presentación más completa, más allá de lo que sería un *Sprint Review*.

### 4.2. Criterios de aceptación.

- Crear la infraestructura necesaria: repositorio en GitHub y con acceso para todos los miembros del equipo.

- Extraer datos de distintas fuentes de datos y creación de una Base de Datos.

- Tener la extracción de datos, creación de la Base de Datos e insercción de datos automatizada en funciones(obligatorio) y clases(optativo).

- Tener en el repositorio de GitHub todo el código del desarrollo del proyecto. 

### 4.3. Historias de usuario.

Para la gestión del proyecto, usaremos historias de usuario. Las historias de usuario son descripciones breves y concretas de las funcionalidades o características que un usuario espera encontrar en un producto o sistema. Recordemos que, las historias de usuario son una herramienta importante para asegurarse de que el equipo de desarrollo (es decir, nosotras) entienda las necesidades de los usuarios y construya el producto de manera efectiva.

Algunas de las historias de usuario que podemos definir son:

1. Exploración del DataFrame para entender que datos hay.

2. Realización del EDA para identificar que transformaciones vhay que hacer a los datos.

3. Transformación de los datos.

4. Decidir que visualizaciones hacer.

## 5. Entrega.

El formato de entrega de este proyecto será mediante la subida de este a la plataforma de GitHub. Para subirlo, se creará un repositorio en vuestro perfil. El nombre del repositorio deberá estar compuesto de las siguientes partes, todo ello separado por guiones:

- La palabra: proyecto-da.

- Letra de la promoción: promo-X.

- Número del módulo: modulo-3.

- Número del equipo: team-X.

Por ejemplo:

- project-da-promo-H-modulo-3-team-1

- project-da-promo-H-modulo-3-team-3

En lo relacionado en las fechas de los *sprints* pueden verlo en vuestros calendarios

En las *sprint review* se revisará que se hayan solucionado todas las tareas técnicas asociadas a la entrega de esos *sprints*, si algo quedara pendiente se arrastraría al siguiente *sprint*.

## 6. Presentación.

El último día del módulo presentaréis la versión final de este proyecto a vuestras compañeras y al equipo de Adalab. Cada equipo realizará una presentación de 10 minutos y posteriormente habrá 5 minutos de *feedback* por parte del público. En este caso, la audiencia podría ser más variada pues no sólo estarán los profesores.

El objetivo es que practiquéis la realización de las demos de los proyectos que habéis desarrollado, explicándolo desde un punto de vista técnico y también desde la perspectiva de producto, mejorando además vuestras habilidades de exposición, objetivo de desarrollo profesional del curso.

Para que la presentación salga bien es imprescindible una buena preparación. Por ello, durante el primer *sprint* del módulo tendréis que asignar responsabilidades dentro del equipo relacionadas con la preparación de ésta. Algunos tips para preparaos este demo son:

- Todas las participantes del equipo deben hablar en la presentación (sin práctica no hay mejora).

- Identificar los objetivos de la presentación: Debemos tener claro qué es lo que queremos lograr con la presentación. ¿Queremos demostrar la funcionalidad de un producto?  ¿Queremos mostrar los resultados de un experimento?  ¿Queremos atraer inversores? Dependiendo del objetivo, deberemos enfocar la presentación de manera distinta.

- Conoce a tu audiencia: La presentación debe estar adaptada al tipo de audiencia que se espera. Si se presentara ante posibles inversores, la presentación debe estar enfocada en los beneficios y la rentabilidad del producto. Si es una presentación para usuarios, deberá enfocarse en la usabilidad y la facilidad de uso.

- Debéis ser claras y concisas: La presentación debe ser fácil de entender y no debe ser demasiado larga. Es importante presentar la información de manera clara y concisa. Debemos tener en cuenta que los detalles técnicos pueden ser interesantes, pero no deberían opacar la idea principal.

- Demostrad la funcionalidad del producto: Si la presentación es para demostrar un producto, es importante que demostremos su funcionalidad. Podemos hacerlo mediante un video o demostrando el producto en vivo. Es importante asegurarse de que el producto funciona correctamente antes de la presentación.

- Resaltad los aspectos más importantes: En cualquier presentación, hay aspectos que son más importantes que otros. Debéis resaltar los aspectos que sean más relevantes para su objetivo. Por ejemplo, si queréis atraer inversores, deberéis resaltar los beneficios y la rentabilidad del producto.

- Practicad la presentación: Es importante que practiquéis la presentación varias veces antes del evento. Debéis aseguraos de que la presentación esté bien estructurada y que os sentís cómodas hablando frente a la audiencia.

- Preparad respuestas a preguntas frecuentes: Es probable que la audiencia tenga preguntas después de la presentación. Debéis preparaos para responder preguntas frecuentes y tener la información necesaria a mano.

Además de esto, para mejorar vuestras habilidades de exposición en público y hacer la presentación más rica, podréis incorporar otros elementos adicionales (son solo ideas, sentíos libres de innovar y ser creativas):

- Dejar muy claro quién ha sido vuestro cliente y qué fue lo que os pidió.

- Explicar qué necesidades cubre o qué problemas soluciona el producto, cuál es el beneficio principal que aporta y qué lo hace único comparado con otros productos parecidos del mercado.

- Aportaciones "únicas y diferenciadoras" de cada equipo al proyecto.

- Cómo ha sido la organización del equipo, el reparto de tareas y la coordinación a la hora de trabajar todas en el mismo código.

- Cuál de las tareas o los puntos ha sido el que más esfuerzo ha requerido.

- Cuál de las tareas o partes del producto es la que hace que el equipo esté más orgulloso.

- Las tecnologías qué habéis utilizado y para qué sirven, y algunas partes del código que habéis desarrollado que merezca la pena resaltar.

- La presentación debe tener un "buen inicio y un buen cierre" que nos haga a todos estar atentos y aplaudir... ahí os dejamos que echéis a volar vuestra imaginación.

- No habléis en primera persona de lo que habéis hecho, hablad del equipo.

- No mencionéis problemas, sino "retos" que os han hecho aprender y crecer.