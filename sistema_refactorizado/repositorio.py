
import json
import os

# Rutas y acceso al almacenamiento de datos

CARPETA_DATOS = os.path.join(
    os.path.dirname(__file__),
    "data"
)

ARCHIVO_DATOS = os.path.join(
    CARPETA_DATOS,
    "solicitudes.json"
)


def obtener_datos_vacios():
    """Devuelve la estructura inicial del sistema."""
    return {
        "estudiantes": [],
        "responsables": [],
        "solicitudes": []
    }


def guardar_datos(datos):
    """Guarda la información del sistema en formato JSON."""
    os.makedirs(CARPETA_DATOS, exist_ok=True)

    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(
            datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )


def cargar_datos():
    """Carga los datos almacenados o crea una estructura inicial."""
    os.makedirs(CARPETA_DATOS, exist_ok=True)

    if not os.path.exists(ARCHIVO_DATOS):
        datos = obtener_datos_vacios()
        guardar_datos(datos)
        return datos

    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except json.JSONDecodeError as error:
        raise ValueError(
            "El archivo de datos contiene información JSON inválida."
        ) from error

    except OSError as error:
        raise RuntimeError(
            "No se pudo acceder al archivo de datos."
        ) from error
