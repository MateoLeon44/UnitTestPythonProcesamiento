from unittest import TestCase

from Procesamiento import Procesamiento

class ProcesamientoTest(TestCase):
    def test_cadenaVacia(self):
        self.assertEquals(Procesamiento().procesar(""),0,"Cadena vacía")
        