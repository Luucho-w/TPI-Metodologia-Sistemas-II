# TPI – Metodología de Sistemas II

## Evolución profesional de un sistema existente

Trabajo Práctico Integrador sobre calidad de software, deuda técnica, principios SOLID, Clean Code y refactoring.

## Descripción del proyecto

El proyecto consiste en analizar y mejorar un sistema de gestión de solicitudes académicas desarrollado en Python.

Se trabajó sobre una versión inicial con problemas de diseño y mantenimiento, para luego aplicar mejoras estructurales sin modificar el comportamiento funcional esperado.

## Versiones del sistema

- **sistema_inicial:** versión original del programa.
- **sistema_refactorizado:** versión mejorada, con responsabilidades más organizadas y persistencia centralizada.

## Funcionalidades

- Registrar solicitudes.
- Listar solicitudes.
- Cambiar estados.
- Asignar responsables.
- Buscar solicitudes.
- Generar reportes.
- Guardar y recuperar información mediante archivos JSON.

## Tecnologías utilizadas

- Python.
- JSON.
- Git y GitHub.
- unittest para pruebas automatizadas.

## Estructura del repositorio

```text
TP_Metodologia_Sistemas_II/
├── sistema_inicial/
├── sistema_refactorizado/
│   ├── data/
│   └── tests/
├── docs/
│   └── informes.md
├── evidencias/
└── README.md
```

## Ejecución

Para ejecutar la versión inicial:

```bash
python sistema_inicial/main.py
```

Para ejecutar la versión refactorizada:

```bash
python sistema_refactorizado/main.py
```

## Pruebas automatizadas

Desde la carpeta principal, ejecutar:

```bash
python -m unittest discover -s sistema_refactorizado/tests -v
```

## Documentación

El análisis, diagnóstico, refactorings, pruebas y revisión técnica se encuentran documentados en `docs/bitacora.md`.

## Uso de inteligencia artificial

Se utilizó ChatGPT como herramienta de asistencia durante el desarrollo, análisis, refactoring y documentación del trabajo. Las decisiones y verificaciones finales corresponden al equipo.

## Integrantes

- Integrante 1: Wittmund Luciano
- Integrante 2: Pighin Bruno
- Integrante 3: Benítez Ivan
