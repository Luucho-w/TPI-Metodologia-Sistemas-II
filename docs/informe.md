# TRABAJO PRÁCTICO INTEGRADOR

## Evolución profesional de un sistema existente: calidad, deuda técnica, refactoring y revisión técnica

**Materia:** Metodología de Sistemas II  
**Carrera:** Tecnicatura Universitaria en Programación  
**Comisión:**  M25 C4-07  
**Fecha:** 8 de noviembre de 2026

### Integrantes

- Wittmund Luciano
- Pighin Bruno
- Benítez Ivans

---

# Resumen ejecutivo

El presente trabajo aborda el análisis y la mejora de un Sistema de Gestión de Solicitudes Académicas desarrollado en Python. Se evaluó la calidad externa e interna de una versión inicial, identificando problemas de diseño y deuda técnica. A partir del diagnóstico, se aplicaron técnicas de refactoring orientadas a mejorar la organización, legibilidad y mantenibilidad del código. También se incorporaron validaciones, manejo de errores y pruebas automatizadas mediante la biblioteca `unittest`. Finalmente, se realizó una revisión técnica de la versión mejorada, considerando principios SOLID y prácticas de Clean Code. El trabajo permitió comprobar la importancia de mantener una estructura interna clara sin perder las funcionalidades que necesita el usuario.

---

# 1. Descripción del sistema y alcance

## 1.1. Sistema

El proyecto consiste en un **Sistema de Gestión de Solicitudes Académicas**.

Su finalidad es permitir el registro y seguimiento de solicitudes realizadas por estudiantes ante una institución educativa.

El sistema permite administrar solicitudes, consultar su información, modificar sus estados y asignar responsables para su atención.

## 1.2. Tecnología utilizada

- Lenguaje de programación: Python.
- Persistencia de datos: archivos JSON.
- Pruebas automatizadas: biblioteca `unittest`.
- Control de versiones: Git.
- Repositorio remoto: GitHub.

## 1.3. Actores principales

- **Estudiante:** realiza solicitudes académicas y puede consultar su información.
- **Responsable:** recibe solicitudes y puede ser asignado para su atención.
- **Operador del sistema:** utiliza las opciones disponibles para administrar y consultar los registros.

## 1.4. Funcionalidades principales

El sistema cuenta con las siguientes operaciones:

1. Registrar solicitudes.
2. Listar solicitudes existentes.
3. Cambiar el estado de una solicitud.
4. Asignar responsables.
5. Buscar solicitudes.
6. Generar reportes generales.

La información se conserva mediante archivos JSON, permitiendo recuperar los registros al iniciar nuevamente el programa.

## 1.5. Alcance

El trabajo se concentra en mejorar la calidad interna de un sistema de alcance acotado, sin buscar incorporar funcionalidades innecesarias.

Se desarrollaron dos versiones:

- **Versión inicial:** implementación funcional utilizada como base para el diagnóstico.
- **Versión refactorizada:** implementación reorganizada, con mejoras en responsabilidades, validaciones, persistencia y pruebas.

El objetivo principal fue mejorar la estructura del código manteniendo las funcionalidades principales del sistema.

## 1.6. Repositorio

Repositorio GitHub:

https://github.com/Luucho-w/TPI-Metodologia-Sistemas-II

---

# 2. Calidad externa e interna

## 2.1. Calidad externa

La calidad externa se relaciona con el comportamiento del sistema desde el punto de vista de sus usuarios.

En el Sistema de Gestión de Solicitudes Académicas se identifican los siguientes aspectos:

- **Funcionalidad:** permite registrar, listar, buscar y modificar solicitudes académicas, asignar responsables y generar reportes.
- **Usabilidad:** cuenta con un menú de opciones por consola que facilita la interacción. Sin embargo, podría mejorarse mediante mensajes más claros y una interfaz gráfica.
- **Confiabilidad:** la información se almacena en archivos JSON, permitiendo conservar los datos entre ejecuciones. En la versión refactorizada se incorporaron controles para manejar errores de lectura y escritura.
- **Rendimiento:** al utilizar archivos JSON, el sistema resulta adecuado para volúmenes pequeños y medianos de información. Para grandes cantidades de registros sería conveniente utilizar una base de datos.
- **Mantenibilidad desde el uso:** las validaciones y los mensajes de error contribuyen a que el usuario pueda operar el sistema con mayor claridad.

## 2.2. Calidad interna

La calidad interna se refiere a las características del código fuente y a la facilidad para comprenderlo, modificarlo, probarlo y mantenerlo.

En la versión inicial se detectaron responsabilidades mezcladas, repetición de operaciones de persistencia, funciones extensas y validaciones insuficientes.

Luego del proceso de refactoring se incorporaron mejoras:

- Separación de las operaciones de almacenamiento en el módulo `repositorio.py`.
- Creación de funciones reutilizables para buscar solicitudes y generar identificadores.
- Uso de constantes para centralizar estados y prioridades válidos.
- Incorporación de `DatosNuevaSolicitud` para agrupar los datos necesarios al registrar una solicitud.
- Manejo de errores durante la lectura y escritura de archivos JSON.
- Incorporación de pruebas automatizadas para verificar funciones y persistencia.

## 2.3. Comparación entre ambas calidades

La versión refactorizada presenta una mejora en su calidad interna, ya que el código está mejor organizado y resulta más sencillo de mantener y probar.

En cuanto a la calidad externa, se conservaron las funcionalidades principales y se reforzaron las validaciones y el manejo de errores.

Sin embargo, el sistema continúa siendo una aplicación de consola y utiliza archivos JSON, por lo que existen oportunidades de mejora para futuras versiones.

---

# 3. Diagnóstico técnico: deuda técnica y Code Smells

Se realizó una revisión del código fuente de la versión inicial del Sistema de Gestión de Solicitudes Académicas.

Durante el análisis se identificaron ocho problemas técnicos que podían dificultar el mantenimiento, las pruebas y la evolución del sistema.

| N.º | Problema identificado | Ubicación o evidencia | Impacto y riesgo de mantenimiento | Prioridad |
|---|---|---|---|---|
| 1 | Responsabilidades mezcladas | Funciones de `main.py` que realizan lectura, validación, procesamiento y almacenamiento. | Los cambios en una responsabilidad pueden afectar otras partes del programa. Dificulta las pruebas y el mantenimiento. | Alta |
| 2 | Código repetido | Operaciones de lectura y escritura JSON repetidas en distintas funciones. | Una modificación de la persistencia debe replicarse en varios lugares, aumentando el riesgo de inconsistencias. | Alta |
| 3 | Validaciones incompletas | Función encargada de cambiar el estado de una solicitud. | Se pueden ingresar estados no permitidos y generar información inconsistente. | Alta |
| 4 | Manejo insuficiente de errores | Operaciones de lectura del archivo JSON. | Un archivo dañado puede provocar que el programa termine inesperadamente. | Alta |
| 5 | Dependencia de una ruta global | Variable global utilizada para definir la ubicación del archivo de datos. | Dificulta cambiar la ubicación del almacenamiento y realizar pruebas aisladas. | Media |
| 6 | Funciones extensas | Funciones del programa principal que concentran varias operaciones. | Son más difíciles de comprender, probar y modificar sin introducir errores. | Media |
| 7 | Acoplamiento entre lógica e interfaz | Funciones que combinan reglas del sistema con instrucciones de entrada y salida por consola. | Dificulta reutilizar la lógica desde otras interfaces y probarla independientemente. | Alta |
| 8 | Generación de identificadores poco robusta | Lógica inicial que obtiene el identificador utilizando la cantidad de registros más uno. | Si se eliminan registros, pueden generarse identificadores repetidos. | Alta |

## 3.1. Consecuencias de la deuda técnica

Los problemas identificados no impedían necesariamente que el sistema cumpliera sus operaciones básicas, pero aumentaban el costo de realizar modificaciones futuras.

La repetición de código, la falta de separación de responsabilidades y las validaciones incompletas podían generar errores difíciles de detectar.

Por este motivo, se estableció como objetivo mejorar la estructura interna del código sin alterar el comportamiento funcional esperado.

---

# 4. Aplicación de SOLID y Clean Code

## 4.1. Análisis de los principios SOLID

Se evaluó la versión refactorizada considerando los principios SOLID.

### SRP – Responsabilidad Única

Se mejoró la separación de responsabilidades al trasladar las operaciones de almacenamiento al módulo `repositorio.py`.

De esta manera, la lectura y escritura de datos dejaron de estar distribuidas por el programa principal.

Sin embargo, algunas funciones de `main.py` todavía combinan interacción con el usuario y lógica del sistema. Por lo tanto, la aplicación de este principio es parcial.

### OCP – Abierto/Cerrado

El menú utiliza un diccionario de operaciones, lo que facilita incorporar nuevas opciones sin agregar más bloques condicionales.

La estructura todavía requiere modificaciones para registrar nuevas operaciones, por lo que no se cumple completamente el principio.

### LSP – Sustitución de Liskov

No resulta directamente aplicable al diseño actual porque el sistema no utiliza jerarquías de herencia ni sustitución entre clases derivadas.

No se considera necesario incorporar herencia artificial únicamente para aplicar este principio.

### ISP – Segregación de Interfaces

El sistema no utiliza interfaces ni clases con contratos amplios que deban dividirse.

Por este motivo, no se identifica una aplicación directa de este principio en la implementación actual.

### DIP – Inversión de Dependencias

Se mejoró la organización al separar el repositorio, aunque `main.py` todavía depende directamente de las funciones concretas del módulo de almacenamiento.

Como mejora futura podría incorporarse una abstracción del repositorio para reducir el acoplamiento entre la lógica principal y la persistencia.

## 4.2. Análisis Clean Code

Se identificaron las siguientes mejoras relacionadas con Clean Code:

- Uso de nombres descriptivos para funciones y variables.
- Definición de constantes para estados y prioridades permitidos.
- Extracción de operaciones reutilizables.
- Reducción de condiciones repetitivas en el menú.
- Incorporación de validaciones y manejo de errores.
- Separación del acceso a datos respecto del módulo principal.
- Agrupación de parámetros relacionados mediante un objeto de datos.

Como aspecto pendiente, la interacción por consola continúa integrada con algunas funciones que realizan operaciones del sistema.

En general, los cambios mejoran la legibilidad y facilitan la comprensión del código.

---

# 5. Refactorings realizados

Durante la mejora del sistema se aplicaron cinco refactorings concretos.

| Refactoring | Aplicación |
|---|---|
| Move Method / reubicación de responsabilidades | Se trasladaron `cargar_datos()` y `guardar_datos()` al módulo `repositorio.py`, separando las operaciones de persistencia del programa principal. |
| Extract Method | Se extrajeron `buscar_por_id()` y `obtener_siguiente_id()` para reutilizar operaciones y evitar duplicación de código. |
| Replace Conditional with Lookup | Se reemplazó la cadena de condiciones del menú por un diccionario de operaciones, simplificando la selección de opciones. |
| Replace Magic Values with Constants | Se definieron `ESTADOS_VALIDOS` y `PRIORIDADES_VALIDAS` para centralizar los valores permitidos. |
| Introduce Parameter Object | Se incorporó la clase de datos `DatosNuevaSolicitud`, que agrupa los parámetros necesarios para crear una solicitud y simplifica el paso de información. |

## 5.1. Detalle de los cambios

### Separación del repositorio

Se creó el archivo `repositorio.py` para centralizar la lectura y escritura de información.

Esto permite que el programa principal no tenga que repetir las operaciones de persistencia en diferentes funciones.

### Extracción de métodos

Se incorporaron funciones reutilizables como `buscar_por_id()` y `obtener_siguiente_id()`.

Esto evita repetir lógica y facilita las pruebas individuales.

### Validación y constantes

Se definieron valores permitidos para los estados y prioridades de las solicitudes.

Esto permite centralizar las reglas y evitar valores inconsistentes.

### Generación de identificadores

Se reemplazó el cálculo basado en la cantidad de registros por un mecanismo que obtiene el identificador máximo existente y suma uno.

De esta forma se reduce el riesgo de generar identificadores repetidos cuando existen eliminaciones.

### Introducción de objeto de parámetros

Se incorporó la clase `DatosNuevaSolicitud`, que agrupa los siguientes datos:

- `estudiante_id`
- `titulo`
- `descripcion`
- `tipo`
- `prioridad`

Este objeto permite representar de manera más clara la información necesaria para crear una nueva solicitud.

## 5.2. Resultados de los refactorings

Los cambios realizados permitieron mejorar la distribución de responsabilidades, reducir la repetición de código, centralizar la persistencia y facilitar las pruebas automatizadas.

La incorporación de `DatosNuevaSolicitud` permitió agrupar los parámetros relacionados con la creación de solicitudes en un único objeto, haciendo más clara la construcción de nuevos registros.

Las mejoras se realizaron procurando conservar las funcionalidades principales del sistema original.

---

# 6. Pruebas y verificación del comportamiento

Se realizaron pruebas manuales y automatizadas sobre la versión refactorizada del sistema.

Para las pruebas automatizadas se utilizó la biblioteca `unittest` de Python.

## 6.1. Pruebas automatizadas

Se implementaron ocho pruebas:

| N.º | Prueba | Resultado |
|---|---|---|
| 1 | Búsqueda de un registro existente. | Aprobada |
| 2 | Búsqueda de un registro inexistente. | Aprobada |
| 3 | Obtención del siguiente identificador. | Aprobada |
| 4 | Obtención del identificador inicial con una lista vacía. | Aprobada |
| 5 | Creación de la estructura inicial de datos. | Aprobada |
| 6 | Guardado y recuperación de información. | Aprobada |
| 7 | Detección de archivos JSON dañados. | Aprobada |
| 8 | Construcción de una solicitud mediante `DatosNuevaSolicitud`, verificando sus atributos principales. | Aprobada |

## 6.2. Ejecución de las pruebas

Las pruebas se ejecutaron desde la carpeta raíz del proyecto mediante el siguiente comando:

```powershell
python -m unittest discover -s sistema_refactorizado/tests -t sistema_refactorizado -v
```

Resultado obtenido:

```text
Ran 8 tests
OK
```

Las ocho pruebas automatizadas se ejecutaron correctamente, sin errores.

## 6.3. Pruebas manuales

También se realizaron pruebas manuales para verificar las operaciones principales:

- Ejecución del menú principal.
- Carga de datos de ejemplo.
- Registro de solicitudes.
- Listado de solicitudes.
- Cambio de estado.
- Rechazo de estados no permitidos.
- Asignación de responsables.
- Búsqueda de solicitudes.
- Generación de reportes.
- Persistencia de los datos después de cerrar y volver a iniciar el programa.

## 6.4. Verificación del comportamiento

Se comprobó que la versión refactorizada mantiene las funcionalidades principales del sistema y que las mejoras incorporadas no impiden su funcionamiento.

Las pruebas automatizadas permiten verificar operaciones específicas, mientras que las pruebas manuales permiten observar el comportamiento general desde la consola.

La persistencia también fue verificada mediante operaciones de guardado y recuperación de datos.

---

# 7. Code Review profesional

Se utilizó una lista de control para revisar aspectos técnicos de la versión refactorizada.

## 7.1. Checklist técnico

| Criterio | Resultado |
|---|---|
| Los nombres de funciones y variables son descriptivos. | Cumple |
| Las responsabilidades están mejor distribuidas. | Cumple parcialmente |
| El almacenamiento está separado de la lógica principal. | Cumple |
| Se utilizan funciones reutilizables. | Cumple |
| Se validan los estados de las solicitudes. | Cumple |
| Se contemplan errores de lectura y escritura. | Cumple |
| Se realizan pruebas automatizadas. | Cumple |
| Se conserva la persistencia de los datos. | Cumple |

## 7.2. Observaciones de la revisión

Durante la revisión se identificaron mejoras importantes respecto de la versión inicial:

- La persistencia está centralizada en un módulo independiente.
- Se redujo la repetición de operaciones.
- Se incorporaron validaciones para evitar estados no permitidos.
- Se mejoró el tratamiento de errores relacionados con archivos JSON.
- Se incorporaron pruebas automatizadas para verificar funciones importantes.

También se identificaron aspectos que todavía pueden mejorarse:

- Algunas funciones mantienen interacción directa con la consola.
- El programa principal continúa dependiendo de funciones concretas del repositorio.
- No se utiliza una abstracción de persistencia que permita intercambiar fácilmente el mecanismo de almacenamiento.

## 7.3. Correcciones realizadas

A partir del diagnóstico y la revisión técnica se realizaron las siguientes correcciones:

1. Centralización de las operaciones de lectura y escritura.
2. Extracción de funciones reutilizables.
3. Validación de los estados permitidos.
4. Mejora del manejo de errores.
5. Corrección de la generación de identificadores.
6. Incorporación de pruebas automatizadas.
7. Simplificación de la creación de solicitudes mediante `DatosNuevaSolicitud`.

## 7.4. Criterios de aceptación técnica

Se consideran criterios de aceptación:

- Que el programa pueda ejecutarse correctamente.
- Que las funcionalidades principales estén disponibles.
- Que los datos puedan guardarse y recuperarse.
- Que los estados inválidos sean rechazados.
- Que las pruebas automatizadas finalicen correctamente.
- Que la estructura del código permita comprender y mantener sus componentes.

La versión refactorizada satisface los criterios funcionales y de pruebas verificados. Se reconocen las limitaciones de diseño mencionadas como oportunidades de mejora futura.

---

# 8. Conclusiones y aprendizaje

El desarrollo de este trabajo permitió comprender que un sistema puede cumplir sus funcionalidades principales y, al mismo tiempo, presentar problemas internos que dificultan su mantenimiento y evolución.

A través del diagnóstico se identificaron distintos problemas de diseño y deuda técnica en la versión inicial.

La aplicación de técnicas de refactoring permitió mejorar la organización del código, reducir la repetición, separar las operaciones de persistencia y facilitar las pruebas.

También se comprobó la importancia de utilizar validaciones, manejar errores y escribir funciones con responsabilidades más claras.

El análisis de SOLID permitió reconocer que no todos los principios se aplican de la misma manera a todos los sistemas. Algunos pudieron mejorarse parcialmente, mientras que otros no resultaron directamente aplicables al diseño actual.

Las pruebas automatizadas fueron importantes para verificar el funcionamiento de las operaciones y detectar posibles errores durante los cambios.

Como limitaciones del proyecto se reconoce que el sistema continúa utilizando una interfaz de consola, archivos JSON y algunas funciones que todavía combinan interacción con el usuario y lógica de negocio.

## 8.1. Mejoras futuras

Como posibles mejoras se proponen:

- Incorporar una interfaz gráfica o web.
- Separar completamente la interfaz de la lógica de negocio.
- Implementar una abstracción para el repositorio de datos.
- Utilizar una base de datos para administrar mayores volúmenes de información.
- Ampliar las pruebas automatizadas.
- Incorporar pruebas de integración.
- Mejorar la validación de las transiciones entre estados.

En conclusión, el trabajo permitió aplicar conceptos de calidad de software, deuda técnica, SOLID, Clean Code, refactoring y revisión técnica sobre un sistema concreto.

---

# 9. Registro de utilización de herramientas de IA

Durante el desarrollo del trabajo se utilizó ChatGPT como herramienta de apoyo para organizar las actividades, comprender conceptos y resolver dificultades técnicas.

El uso de IA no reemplazó la ejecución ni la verificación del proyecto por parte del equipo.

A continuación, se presenta un registro resumido y ordenado de las principales actividades en las que se utilizó esta herramienta. No constituye una transcripción literal de todos los mensajes.

| N.º | Actividad | Uso de la herramienta |
|---|---|---|
| 1 | Organización del proyecto | Se solicitó ayuda para ordenar el desarrollo del trabajo en etapas: código, repositorio y documentación. |
| 2 | Creación de la estructura | Se recibió orientación para organizar las carpetas y archivos del proyecto. |
| 3 | Desarrollo del sistema | Se utilizó asistencia para implementar y revisar las funcionalidades en Python. |
| 4 | Refactoring | Se solicitó orientación para separar responsabilidades, extraer funciones y mejorar la estructura del código. |
| 5 | Pruebas automatizadas | Se recibió ayuda para crear pruebas con `unittest`, ejecutar los comandos y resolver problemas de importación. |


## 9.1. Declaración de uso de IA

Se utilizó ChatGPT como apoyo durante el desarrollo del Trabajo Práctico Integrador, principalmente para interpretar la consigna, organizar el trabajo, recibir orientación sobre programación en Python, aplicar técnicas de refactoring, preparar pruebas y mejorar la documentación.

El equipo revisó y ejecutó el código, verificó los resultados de las pruebas y trabajó sobre el repositorio del proyecto.

La responsabilidad sobre el contenido final, las decisiones técnicas y la defensa del trabajo corresponde a los integrantes del equipo.

---

# 10. Anexos y evidencias

**Repositorio GitHub:**

https://github.com/Luucho-w/TPI-Metodologia-Sistemas-II

**Video de defensa y demostración:**

https://drive.google.com/file/d/1hPutkfLjxGvvWxjWL_8vmSclaO3gOL_E/view?usp=sharing
---
