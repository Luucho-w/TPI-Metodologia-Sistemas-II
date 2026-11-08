
import unittest

from main import (
    buscar_por_id,
    obtener_siguiente_id,
    DatosNuevaSolicitud,
    construir_solicitud
)


class TestFunciones(unittest.TestCase):

    def setUp(self):
        self.registros = [
            {"id": 1, "nombre": "Juan"},
            {"id": 2, "nombre": "Maria"},
            {"id": 3, "nombre": "Carlos"}
        ]

    def test_buscar_registro_existente(self):
        resultado = buscar_por_id(self.registros, 2)
        self.assertEqual(resultado["nombre"], "Maria")

    def test_buscar_registro_inexistente(self):
        resultado = buscar_por_id(self.registros, 10)
        self.assertIsNone(resultado)

    def test_obtener_siguiente_identificador(self):
        resultado = obtener_siguiente_id(self.registros)
        self.assertEqual(resultado, 4)

    def test_identificador_con_lista_vacia(self):
        resultado = obtener_siguiente_id([])
        self.assertEqual(resultado, 1)

    def test_construir_solicitud(self):
        datos = DatosNuevaSolicitud(
            estudiante_id=1,
            titulo="Certificado de alumno regular",
            descripcion="Solicito certificado",
            tipo="academica",
            prioridad="media"
        )

        solicitud = construir_solicitud(datos, 5)

        self.assertEqual(solicitud["id"], 5)
        self.assertEqual(solicitud["estudiante_id"], 1)
        self.assertEqual(solicitud["titulo"], "Certificado de alumno regular")
        self.assertEqual(solicitud["estado"], "abierta")
        self.assertIsNone(solicitud["responsable_id"])


if __name__ == "__main__":
    unittest.main()
