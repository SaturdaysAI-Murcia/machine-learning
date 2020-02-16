# Ideas de proyectos ([ver proyectos otras ciudades](https://github.com/SaturdaysAI/Projects))


| Propuesta de proyecto             | Tipo de dato               | Propuesto por  | Asigado a |
|-----------------------------------|----------------------------|----------------|-----------|
| Respira aire limpio               | Datos tabulares temporales | Javier Abellán |           |
| Predecir trayectoria escolar      | Datos tabulares temporales | Andrés Meroño  |           |
| Mejora tasa evaluación de la UM   | Datos tabulares temporales | Pacom          |           |
| Predicción lengua materna         | NLP (inglés)               | Pascual Pérez  |           |
| Automapeo de tablas               | NLP (español)              | Andrés Meroño  |           |
| Traductor de código               | NLP (programación)         | Andrés Meroño  |           |
| Analizador de código              | NLP (programación)         | Andrés Meroño  |           |
| SOS Mar Menor                     | Imagen satélite            | J.M. Bolarín   |           |
| Eficiencia placas solares         | Imagen satélite            | Javier Abellán |           |
| Algo relacionado con la comida?   |                            | Javier Abellán |           |
| Algo relacionado con el deporte?  |                            | Javier Abellán |           |
| Algo relacionado con la medicina? |                            | Javier Abellán |           |
| Analiza tu ADN?                   | Bioinfomatica, cadenas ADN | Javier Abellán |           |
| Encuentra aparacmiento libre      | Tráfico tiempo real?       |                |           |

---

<h1 align="center">Datos tabulares</h1>


## Respira aire limpio
Murcia ha sido catalogada como una de las ciudades con peor aire, ayúdanos a buscar las principales causas de este fenómeno (tráfico, industria, quema de restrojos?) para ponerle freno.

- [Noticia SER](https://cadenaser.com/emisora/2019/10/08/radio_murcia/1570530665_899816.html)
- [Activado el protocolo de aviso por contaminación en 2020](https://twitter.com/AytoMurcia/status/1212678697389580288)
- [Cuenta stop quemas murcia twiter](https://twitter.com/stopquemasmurc1)
- [Fuente de datos sinqlair](https://sinqlair.carm.es/calidadaire)


## Predecir trayectoria escolar
partiendo de la información de matriculación, de notas, de faltas de asistencia, centros escolares, etc... de alumnos de la Región de Murcia durante los últimos 'n' años obtener una predicción de la nota media, puntos fuertes/débiles de un alumno en concreto. También se pretende obtener un mapa de la región a modo de probabilidad a priori de obtener una determinada nota media.


## Mejorar la tasa de evaluación de la Universidad de Murcia

#### Introducción
La tasa de evaluación mide el porcentaje de créditos que los estudiantes se presentan, examinan, de los créditos matriculados. Esta tasa junto con las tasas de éxito, porcentaje de créditos aprobados de los examinados, y la tasa de rendimiento, porcentaje de créditos aprobados de los matriculados, son una medida de la calidad de la docencia en las universidades.

En la Universidad de Murcia tenemos tasas de éxito dentro de la media del Sistema Universitario Español (SUE), sin embargo, en algunas titulaciones la tasa de evaluación está por debajo de la media del SUE con lo cual nuestra tasa de rendimiento es menor de la deseada.

#### Objetivo
El objetivo de este proyecto es identificar a aquellos estudiantes que no van a examinarse de algunas de las materias de las que están matriculados para darle soporte y ayudarlos a que tomen la decisión de examinarse, y de paso aprobar, de manera que tanto la tasa de evaluación como la tasa de rendimiento aumenten.


#### Procedimiento
Para entrenar a nuestro modelo necesitamos información histórica de los estudiantes, por una parte de sus resultados académicos y por otra de comportamientos que permitan inferir si van a examinarse o no.

Para los resultados académicos es sencillo, se puede obtener accediendo a las actas de los últimos años. Hay disponibles millones de registros de actas desde hace más de 15 años.

En cuanto a los comportamientos de los alumnos lo más sencillo es observar su interacción con el aula virtual de la UMU. El aula virtual registra las interacciones de los alumnos, cuantas veces entran, cuanto tiempo están dentro del aula, a qué contenidos acceden, etc. En este momento desconozco el detalle de los registros de esta interacción, todos los eventos que se recogen, si se recogen en BBDD o logs, de qué histórico se dispone, etc. Estoy averiguándolo para poder enfocar más el proyecto.

Otra fuente de estudio del comportamiento de los alumnos, aunque de momento me parece un poco peregrina hasta que no lo vea con más detalle, podría ser su asistencia a clase o no. No existe un registro de  asistencia a clase de los alumnos, pero basandonos en su acceso a los puntos de la wifi podemos saber dónde está el alumno en cada momento. Es posible averiguar los puntos de acceso wifi de las aulas, que asignatura se está dando en el aula en un momento dado, etc. y quién está conectado a la wifi a partir de su cuenta de correo que se utiliza para autenticarse. También podría saberse si acude a bibliotecas, salas de estudio, etc.

Por último podríamos bucear en los registros de la biblioteca para saber si pide libros prestados, etc. aunque me parece que no todos los estudiantes piden libros prestados.

#### Conclusión
Acceder y disponer de los datos de resultados, actas, es sencillo y posible y la información que hay es abundante.
Faltaría averiguar la información disponible para inferir el comportamiento. Estoy en ello.



<h1 align="center">Procesamiento del Lenguaje Natural (NLP)</h1>

## Automapeo de tablas
Dadas dos tablas de datos del tipo: código, descripcion las cuales son similares en descripción y diferentes en código, se pretende construir una tercera tabla que relacione los códigos de las dos tablas.
La idea es ir entrenando el modelo con diferentes tipos de casos y esperar que aprenda a relacionar filas con tipos similares.


## Analizador de código
Utilizando la información svn/git de un repositorio de código analizar la ocurrencia de determinados patrones de código: errores típicos de programación (contraseñas enbembidas, números mágicos, estilo de codificación , comentarios, etc...), analizar la estructura de una programa realizando análisis estructural y devolviendo un resumen sintético del código de un proyecto, localizar entidades, analizar sus interdependencias, poder determinar el efecto mariposa (una modificación pequeña aquí produce un cambio enorme allá)...


## Traductor de código inter-framework
ya hice algo similar para migrar Lotus a Java-Oracle. Propongo usar la IA para traducción de lenguajes, por ejemplo de Forms a Java o de Java a NodeJS


## Predecir la lengua materna de un hablante de inglés como lengua extranjera
Me gustaría analizar cómo aprox. unos 500 hablantes de inglés como lengua extranjera con diferentes L1 (francés, alemán, chino, etc…) enfrentan una entrevista oral de 12 -14 minutos que consta de tres partes. El formato de entrevista en el mismo para los 500 hablantes.

Quiero saber si la L1 determina un configuración determinada de características sintácticas y si se puede predecir el grupo de L1 al que pertenece un individuo basándonos en las características presentes en la entrevista.

Este corpus de datos lo he anotado con etiquetas morfológicas (POS tags) y sintácticas que evalúan la complejidad sintáctica a nivel de claúsula y sintagama. Usamos Stanford Core NLP para el análisis. Además puedo añadir al análisis previo unos 400 índices de sofisticación léxica.

Estos índices están basados en:
- [Kyle, K. (2016). Measuring syntactic development in L2 writing: Fine grained indices of syntactic complexity and usage-based indices of syntactic sophistication](https://scholarworks.gsu.edu/cgi/viewcontent.cgi?article=1035&context=alesl_diss) (Doctoral Dissertation).
- [Kyle, K. & Crossley, S. A. (2015). Automatically assessing lexical sophistication: Indices, tools, findings, and application](https://researchlanglit.gsu.edu/files/2016/08/Kyle_et_al-2015-TESOL_Quarterly.pdf). TESOL Quarterly 49(4), pp. 757-786.

Duda: ¿Puede que 500 filas no sean suficientes?


<h1 align="center">Imagen</h1>

## SOS Mar Menor
El Mar Menor esta en estdo crítico. Analiza cual es su estado, y las principales causas de su deteriorio a lo largo de los años así como el impacto de catastrofes actuales como la Dana.

## Eficiencia placas solares
Murcia goza de una gran cantidad de dias de sol al año. Analiza la cantida de energía que se puede obtener según la zona geográfica y orientacion del edificio. Ésto nos servirá para calcular la amortización del uso de placas solares como fuente de energía renobable.

---

# Fuente de ideas

- Competiciones
  - [Kaggle](https://www.kaggle.com)
  - [ML contests](https://mlcontests.com)
- Fast.ai
  - [share your work here](https://forums.fast.ai/t/share-your-work-here)
  - [share your work here (part 2)](https://forums.fast.ai/t/share-your-work-here-part-2)
- Cyberseguridad
  - [Awesome ML for cybersecurity](https://github.com/jivoi/awesome-ml-for-cybersecurity)
