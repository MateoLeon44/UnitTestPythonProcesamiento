from unittest import TestCase

'''
Cadena vacía
Mínimo
Máximo
Promedio
Cuando solo nos envían un número
Cuando nos envían dos números
Cuando nos envían múltiples números separados por ,
Número de elementos
'''

from Procesamiento import Procesamiento

class ProcesamientoTest(TestCase):
    def test_cadenaVacia(self):
        self.assertEquals(Procesamiento().procesar(""),[0,0,0,0],"Cadena vacía")
    def test_numeroDeElementosUnNumero(self):
        self.assertEquals(Procesamiento().procesar("2"),[1,0,0,0],"Un número")
    def test_numeroDeElementosDosNumeros(self):
        self.assertEquals(Procesamiento().procesar("2,3"),[2,0,0,0],"Un número")
