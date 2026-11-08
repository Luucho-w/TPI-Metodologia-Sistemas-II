# informe del Trabajo Práctico Integrador

## Sistema
Sistema de Gestión de Solicitudes Académicas.

## Tecnología
Python y archivos JSON.

## Integrantes
- Integrante 1:
- Integrante 2:
- Integrante 3:

## Etapa 1: Sistema inicial

Se desarrolló una primera versión funcional
de un sistema de gestión de solicitudes
académicas.

El sistema permite:
- Registrar solicitudes.
- Listar solicitudes.
- Cambiar estados.
- Asignar responsables.
- Buscar solicitudes.
- Generar reportes.

La información se almacena mediante
archivos JSON.

## Evidencias iniciales

- [ ] Captura del menú principal.
- [ ] Captura de carga de datos.
- [ ] Captura de registro de solicitud.
- [ ] Captura del listado.
- [ ] Captura del cambio de estado.
- [ ] Captura del reporte.

## Diagnóstico técnico

Se realizó una revisión del código fuente de la versión inicial del Sistema de Gestión de Solicitudes Académicas.

Durante el análisis se identificaron los siguientes problemas:

1. Responsabilidades mezcladas: algunas funciones realizan lectura de datos, validaciones, procesamiento y almacenamiento.
2. Código repetido: las operaciones de acceso a los datos se repiten en distintas funciones.
3. Validaciones incompletas: el cambio de estado no verifica que el nuevo estado pertenezca a los valores permitidos.
4. Manejo insuficiente de errores: no se contempla adecuadamente la posibilidad de que el archivo JSON esté dañado.
5. Dependencia de una ruta global: la ubicación del archivo de almacenamiento está definida mediante una variable global.
6. Funciones extensas: algunas funciones concentran demasiadas responsabilidades.
7. Acoplamiento entre lógica e interfaz: las funciones combinan la lógica del sistema con instrucciones de entrada y salida por consola.
8. Generación de identificadores poco robusta: se utiliza la cantidad de registros existentes más uno, lo que puede provocar identificadores repetidos si se eliminan registros.

Estos problemas pueden dificultar el mantenimiento, las pruebas, la reutilización y la evolución del sistema.

Se establece como objetivo del refactoring mejorar la estructura interna del código sin alterar el comportamiento funcional esperado.

## Refactoring

Se desarrolló una segunda versión del sistema, manteniendo las funcionalidades de la versión inicial.

Las principales mejoras realizadas fueron:

1. Separación de responsabilidades: se creó el módulo `repositorio.py` para centralizar la lectura y escritura de datos.
2. Centralización de operaciones: se incorporaron funciones reutilizables para buscar registros por identificador.
3. Validación de estados: se definieron estados permitidos para evitar modificaciones incorrectas.
4. Manejo de errores: se incorporó tratamiento de errores relacionados con la lectura y escritura de archivos.
5. Mejora en la generación de identificadores:** se implementó un mecanismo que obtiene el siguiente identificador a partir del máximo existente.
6. Simplificación del menú: se utilizó un diccionario de operaciones para evitar múltiples condiciones repetitivas.

El objetivo fue mejorar la organización, legibilidad y mantenibilidad del código, conservando las funcionalidades principales del sistema.

## Pruebas

Se realizaron pruebas manuales y automatizadas sobre la versión refactorizada del sistema.

Se utilizó la biblioteca `unittest` de Python.

Se implementaron siete pruebas automatizadas:

1. Búsqueda de un registro existente.
2. Búsqueda de un registro inexistente.
3. Obtención del siguiente identificador.
4. Obtención del identificador inicial con una lista vacía.
5. Creación de la estructura inicial de datos.
6. Guardado y recuperación de información.
7. Detección de archivos JSON dañados.
8. Construcción de una solicitud mediante el objeto DatosNuevaSolicitud, verificando sus atributos principales.

Resultado: las ocho pruebas se ejecutaron correctamente, sin errores.

También se realizaron pruebas manuales para verificar el registro de solicitudes, el cambio de estados, la asignación de responsables, la persistencia y la generación de reportes.

## Code Review

Se realizó una revisión técnica de la versión refactorizada utilizando una lista de control.

| Criterio                                                | Resultado |
|---------------------------------------------------------|-----------|
| Los nombres de funciones son descriptivos               |  Cumple   |
| Las responsabilidades están mejor distribuidas          |  Cumple   |
| El almacenamiento está separado de la lógica principal  |  Cumple   |
| Se utilizan funciones reutilizables                     |  Cumple   |
| Se validan los estados de las solicitudes               |  Cumple   |
| Se contemplan errores de lectura y escritura            |  Cumple   |
| Se realizan pruebas automatizadas                       |  Cumple   |
| Se conserva la persistencia de los datos                |  Cumple   |

Observaciones: la revisión permitió comprobar mejoras en la organización, legibilidad y mantenibilidad del código.

Resultado de la revisión: versión aceptada para continuar con la documentación y presentación final.s

## Análisis SOLID

Se evaluó la versión refactorizada considerando los principios SOLID:

- SRP (Responsabilidad Única):s se mejoró la separación de responsabilidades al trasladar las operaciones de almacenamiento al módulo `repositorio.py`. Sin embargo, algunas funciones de `main.py` todavía combinan interacción con el usuario y lógica de negocio.
- OCP (Abierto/Cerrado): el menú utiliza un diccionario de operaciones, lo que facilita incorporar nuevas opciones sin agregar más bloques condicionales. La estructura todavía requiere modificaciones para registrar nuevas operaciones.
- LSP (Sustitución de Liskov): no resulta directamente aplicable porque el sistema no utiliza jerarquías de herencia.
- ISP (Segregación de Interfaces): no se utilizan interfaces ni clases con contratos amplios, por lo que no se identifica una aplicación directa de este principio.
- DIP (Inversión de Dependencias): se mejoró la organización al separar el repositorio, aunque `main.py` todavía depende directamente de las funciones concretas del módulo de almacenamiento.

Por lo tanto, se considera que la versión refactorizada presenta avances en la organización del código, pero no implementa completamente todos los principios SOLID.

## Análisis Clean Code

Se identificaron las siguientes mejoras:

- Uso de nombres descriptivos para funciones y variables.
- Definición de constantes para estados y prioridades permitidos.
- Extracción de operaciones reutilizables.
- Reducción de condiciones repetitivas en el menú.
- Incorporación de validaciones y manejo de errores.
- Separación del acceso a datos respecto del módulo principal.

Como aspecto pendiente, la interacción por consola continúa integrada con algunas funciones que realizan operaciones del sistema.

## Refactorings realizados

| Refactoring | Aplicación |
|---|---|
| Move Method / reubicación de responsabilidades | Se trasladaron `cargar_datos()` y `guardar_datos()` al módulo `repositorio.py`. |
| Extract Method | Se extrajeron `buscar_por_id()` y `obtener_siguiente_id()` para reutilizar operaciones. |
| Replace Conditional with Lookup | Se reemplazó la cadena de condiciones del menú por un diccionario de operaciones. |
| Replace Magic Values with Constants | Se definieron `ESTADOS_VALIDOS` y `PRIORIDADES_VALIDAS` para centralizar valores permitidos. |

Estos cambios mejoran la organización y reducen la repetición. Se completará la simplificación de parámetros mediante un objeto de datos para la creación de solicitudes.