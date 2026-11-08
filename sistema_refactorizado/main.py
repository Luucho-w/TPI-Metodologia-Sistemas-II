from dataclasses import dataclass
from datetime import datetime

from repositorio import cargar_datos, guardar_datos


ESTADOS_VALIDOS = [
    "abierta",
    "en_proceso",
    "resuelta",
    "cerrada"
]

PRIORIDADES_VALIDAS = ["baja", "media", "alta"]

@dataclass
class DatosNuevaSolicitud:
    estudiante_id: int
    titulo: str
    descripcion: str
    tipo: str
    prioridad: str

def cargar_ejemplos():
    datos = cargar_datos()

    if not datos["estudiantes"]:
        datos["estudiantes"] = [
            {"id": 1, "nombre": "Juan Perez", "email": "juan@email.com"},
            {"id": 2, "nombre": "Maria Lopez", "email": "maria@email.com"}
        ]

    if not datos["responsables"]:
        datos["responsables"] = [
            {"id": 1, "nombre": "Carlos Gomez", "area": "Sistemas"},
            {"id": 2, "nombre": "Laura Martinez", "area": "Administracion"}
        ]

    guardar_datos(datos)
    print("Datos de ejemplo cargados correctamente.")


def buscar_por_id(registros, identificador):
    return next(
        (registro for registro in registros
         if registro["id"] == identificador),
        None
    )


def obtener_siguiente_id(registros):
    return max(
        (registro["id"] for registro in registros),
        default=0
    ) + 1

def construir_solicitud(datos_solicitud, identificador):
    return {
        "id": identificador,
        "estudiante_id": datos_solicitud.estudiante_id,
        "titulo": datos_solicitud.titulo,
        "descripcion": datos_solicitud.descripcion,
        "tipo": datos_solicitud.tipo,
        "prioridad": datos_solicitud.prioridad,
        "estado": "abierta",
        "responsable_id": None,
        "fecha": str(datetime.now())
    }

def registrar_solicitud():
    datos = cargar_datos()

    print("\nREGISTRAR SOLICITUD")

    try:
        estudiante_id = int(input("ID del estudiante: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    estudiante = buscar_por_id(datos["estudiantes"], estudiante_id)

    if estudiante is None:
        print("El estudiante no existe.")
        return

    titulo = input("Titulo: ").strip()
    descripcion = input("Descripcion: ")
    tipo = input("Tipo (academica/administrativa/tecnica): ").strip()
    prioridad = input("Prioridad (baja/media/alta): ").strip().lower()

    if not titulo:
        print("El titulo no puede estar vacio.")
        return

    if prioridad not in PRIORIDADES_VALIDAS:
        print("Prioridad incorrecta.")
        return

    datos_solicitud = DatosNuevaSolicitud(
        estudiante_id=estudiante_id,
        titulo=titulo,
        descripcion=descripcion,
        tipo=tipo,
        prioridad=prioridad
    )

    nueva_solicitud = construir_solicitud(
        datos_solicitud,
        obtener_siguiente_id(datos["solicitudes"])
    )

    datos["solicitudes"].append(nueva_solicitud)
    guardar_datos(datos)

    print("Solicitud registrada correctamente.")


def listar_solicitudes():
    datos = cargar_datos()

    print("\nLISTADO DE SOLICITUDES")

    if not datos["solicitudes"]:
        print("No hay solicitudes registradas.")
        return

    for solicitud in datos["solicitudes"]:
        print("ID:", solicitud["id"])
        print("Estudiante:", solicitud["estudiante_id"])
        print("Titulo:", solicitud["titulo"])
        print("Tipo:", solicitud["tipo"])
        print("Prioridad:", solicitud["prioridad"])
        print("Estado:", solicitud["estado"])
        print("Responsable:", solicitud["responsable_id"])
        print("\n")


def cambiar_estado():
    datos = cargar_datos()

    print("\nCAMBIAR ESTADO")

    try:
        solicitud_id = int(input("ID de solicitud: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    nuevo_estado = input(
        "Nuevo estado (abierta/en_proceso/resuelta/cerrada): "
    ).strip().lower()

    if nuevo_estado not in ESTADOS_VALIDOS:
        print("El estado ingresado no es válido.")
        return

    solicitud = buscar_por_id(datos["solicitudes"], solicitud_id)

    if solicitud is None:
        print("No se encontro la solicitud.")
        return

    solicitud["estado"] = nuevo_estado
    guardar_datos(datos)
    print("Estado actualizado.")


def asignar_responsable():
    datos = cargar_datos()

    print("\nASIGNAR RESPONSABLE")

    try:
        solicitud_id = int(input("ID de solicitud: "))
        responsable_id = int(input("ID del responsable: "))
    except ValueError:
        print("Los identificadores deben ser números.")
        return

    responsable = buscar_por_id(datos["responsables"], responsable_id)

    if responsable is None:
        print("El responsable no existe.")
        return

    solicitud = buscar_por_id(datos["solicitudes"], solicitud_id)

    if solicitud is None:
        print("No se encontro la solicitud.")
        return

    solicitud["responsable_id"] = responsable_id
    guardar_datos(datos)
    print("Responsable asignado.")


def buscar_solicitudes():
    datos = cargar_datos()

    print("\nBUSCAR SOLICITUDES")
    estado = input("Filtrar por estado (Enter para todos): ").strip()

    resultados = [
        solicitud for solicitud in datos["solicitudes"]
        if not estado or solicitud["estado"] == estado
    ]

    if not resultados:
        print("No se encontraron solicitudes.")
        return

    for solicitud in resultados:
        print(
            "ID:", solicitud["id"],
            "| Titulo:", solicitud["titulo"],
            "| Estado:", solicitud["estado"],
            "| Prioridad:", solicitud["prioridad"]
        )


def generar_reporte():
    datos = cargar_datos()
    solicitudes = datos["solicitudes"]

    print("\nREPORTE GENERAL")
    print("Total de solicitudes:", len(solicitudes))

    for estado in ESTADOS_VALIDOS:
        cantidad = sum(
            1 for solicitud in solicitudes
            if solicitud["estado"] == estado
        )
        print(f"{estado.capitalize()}: {cantidad}")


def menu():
    operaciones = {
        "1": cargar_ejemplos,
        "2": registrar_solicitud,
        "3": listar_solicitudes,
        "4": cambiar_estado,
        "5": asignar_responsable,
        "6": buscar_solicitudes,
        "7": generar_reporte
    }

    while True:
        print("\nSISTEMA DE GESTION ACADEMICA")
        print("1. Cargar datos de ejemplo")
        print("2. Registrar solicitud")
        print("3. Listar solicitudes")
        print("4. Cambiar estado")
        print("5. Asignar responsable")
        print("6. Buscar solicitudes")
        print("7. Generar reporte")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "0":
            print("Saliendo del sistema...")
            break

        operacion = operaciones.get(opcion)

        if operacion:
            try:
                operacion()
            except (ValueError, RuntimeError, OSError) as error:
                print("No se pudo completar la operación:", error)
        else:
            print("Opcion incorrecta.")


if __name__ == "__main__":
    menu()
