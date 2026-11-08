
import json
import os
import tempfile
import unittest
from unittest.mock import patch

import repositorio


class TestRepositorio(unittest.TestCase):

    def setUp(self):
        self.directorio_temporal = tempfile.TemporaryDirectory()

        self.ruta_carpeta = os.path.join(
            self.directorio_temporal.name,
            "data"
        )

        self.ruta_archivo = os.path.join(
            self.ruta_carpeta,
            "solicitudes.json"
        )

        self.parche_carpeta = patch.object(
            repositorio,
            "CARPETA_DATOS",
            self.ruta_carpeta
        )

        self.parche_archivo = patch.object(
            repositorio,
            "ARCHIVO_DATOS",
            self.ruta_archivo
        )

        self.parche_carpeta.start()
        self.parche_archivo.start()

    def tearDown(self):
        self.parche_archivo.stop()
        self.parche_carpeta.stop()
        self.directorio_temporal.cleanup()

    def test_cargar_datos_crea_estructura_inicial(self):
        datos = repositorio.cargar_datos()

        self.assertEqual(datos, {
            "estudiantes": [],
            "responsables": [],
            "solicitudes": []
        })

        self.assertTrue(os.path.exists(self.ruta_archivo))

    def test_guardar_y_cargar_datos(self):
        datos_originales = {
            "estudiantes": [
                {"id": 1, "nombre": "Juan"}
            ],
            "responsables": [],
            "solicitudes": []
        }

        repositorio.guardar_datos(datos_originales)
        datos_cargados = repositorio.cargar_datos()

        self.assertEqual(datos_cargados, datos_originales)

    def test_detectar_archivo_json_danado(self):
        os.makedirs(self.ruta_carpeta, exist_ok=True)

        with open(
            self.ruta_archivo,
            "w",
            encoding="utf-8"
        ) as archivo:
            archivo.write("{json incorrecto")

        with self.assertRaises(ValueError):
            repositorio.cargar_datos()


if __name__ == "__main__":
    unittest.main()
