
import json
import os
from datetime import datetime

# SISTEMA DE GESTION DE SOLICITUDES ACADEMICAS
# VERSION INICIAL - ANTES DEL REFACTORING

ARCHIVO = "data/solicitudes.json"

def cargar_datos():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(ARCHIVO):
        datos = {
            "estudiantes": [],
            "responsables": [],
            "solicitudes": []
        }
        guardar_datos(datos)
        return datos

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_datos(datos):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def cargar_ejemplos():
    datos = cargar_datos()

    if len(datos["estudiantes"]) == 0:
        datos["estudiantes"].append({
            "id": 1,
            "nombre": "Juan Perez",
            "email": "juan@email.com"
        })

        datos["estudiantes"].append({
            "id": 2,
            "nombre": "Maria Lopez",
            "email": "maria@email.com"
        })

    if len(datos["responsables"]) == 0:
        datos["responsables"].append({
            "id": 1,
            "nombre": "Carlos Gomez",
            "area": "Sistemas"
        })

        datos["responsables"].append({
            "id": 2,
            "nombre": "Laura Martinez",
            "area": "Administracion"
        })

    guardar_datos(datos)
    print("Datos de ejemplo cargados correctamente.")


def registrar_solicitud():
    datos = cargar_datos()

    print("\nREGISTRAR SOLICITUD")

    estudiante_id = int(input("ID del estudiante: "))
    estudiante = None

    for e in datos["estudiantes"]:
        if e["id"] == estudiante_id:
            estudiante = e

    if estudiante is None:
        print("El estudiante no existe.")
        return

    titulo = input("Titulo: ")
    descripcion = input("Descripcion: ")
    tipo = input("Tipo (academica/administrativa/tecnica): ")
    prioridad = input("Prioridad (baja/media/alta): ")

    if titulo == "":
        print("El titulo no puede estar vacio.")
        return

    if prioridad not in ["baja", "media", "alta"]:
        print("Prioridad incorrecta.")
        return

    nueva = {
        "id": len(datos["solicitudes"]) + 1,
        "estudiante_id": estudiante_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "tipo": tipo,
        "prioridad": prioridad,
        "estado": "abierta",
        "responsable_id": None,
        "fecha": str(datetime.now())
    }

    datos["solicitudes"].append(nueva)
    guardar_datos(datos)

    print("Solicitud registrada correctamente.")


def listar_solicitudes():
    datos = cargar_datos()

    print("\n--- LISTADO DE SOLICITUDES ---")

    for s in datos["solicitudes"]:
        print("----------------------------")
        print("ID:", s["id"])
        print("Estudiante:", s["estudiante_id"])
        print("Titulo:", s["titulo"])
        print("Tipo:", s["tipo"])
        print("Prioridad:", s["prioridad"])
        print("Estado:", s["estado"])
        print("Responsable:", s["responsable_id"])


def cambiar_estado():
    datos = cargar_datos()

    print("\nCAMBIAR ESTADO")

    solicitud_id = int(input("ID de solicitud: "))
    nuevo_estado = input(
        "Nuevo estado (abierta/en_proceso/resuelta/cerrada): "
    )

    for s in datos["solicitudes"]:
        if s["id"] == solicitud_id:
            s["estado"] = nuevo_estado
            guardar_datos(datos)
            print("Estado actualizado.")
            return

    print("No se encontro la solicitud.")


def asignar_responsable():
    datos = cargar_datos()

    print("\nASIGNAR RESPONSABLE")

    solicitud_id = int(input("ID de solicitud: "))
    responsable_id = int(input("ID del responsable: "))

    existe_responsable = False

    for r in datos["responsables"]:
        if r["id"] == responsable_id:
            existe_responsable = True

    if not existe_responsable:
        print("El responsable no existe.")
        return

    for s in datos["solicitudes"]:
        if s["id"] == solicitud_id:
            s["responsable_id"] = responsable_id
            guardar_datos(datos)
            print("Responsable asignado.")
            return

    print("No se encontro la solicitud.")


def buscar_solicitudes():
    datos = cargar_datos()

    print("\nBUSCAR SOLICITUDES")
    estado = input("Filtrar por estado (Enter para todos): ")

    for s in datos["solicitudes"]:
        if estado == "" or s["estado"] == estado:
            print(
                "ID:", s["id"],
                "| Titulo:", s["titulo"],
                "| Estado:", s["estado"],
                "| Prioridad:", s["prioridad"]
            )


def generar_reporte():
    datos = cargar_datos()

    total = len(datos["solicitudes"])
    abiertas = 0
    proceso = 0
    resueltas = 0
    cerradas = 0

    for s in datos["solicitudes"]:
        if s["estado"] == "abierta":
            abiertas += 1
        elif s["estado"] == "en_proceso":
            proceso += 1
        elif s["estado"] == "resuelta":
            resueltas += 1
        elif s["estado"] == "cerrada":
            cerradas += 1

    print("\n--- REPORTE GENERAL ---")
    print("Total de solicitudes:", total)
    print("Abiertas:", abiertas)
    print("En proceso:", proceso)
    print("Resueltas:", resueltas)
    print("Cerradas:", cerradas)


def menu():
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

        if opcion == "1":
            cargar_ejemplos()
        elif opcion == "2":
            registrar_solicitud()
        elif opcion == "3":
            listar_solicitudes()
        elif opcion == "4":
            cambiar_estado()
        elif opcion == "5":
            asignar_responsable()
        elif opcion == "6":
            buscar_solicitudes()
        elif opcion == "7":
            generar_reporte()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion incorrecta.")


if __name__ == "__main__":
    menu()
