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
        self.assertEquals(Procesamiento().procesar("2"),[1,2,2,2],"Un número")
    def test_numeroDeElementosDosNumeros(self):
        print(Procesamiento().procesar("2,3"))
        self.assertEquals(Procesamiento().procesar("2,3"),[2,2,3,2.5],"2 números")
    def test_numeroDeElementosNNumeros(self):
        self.assertEquals(Procesamiento().procesar("2,3,4,5"),[4,2,5,3.5], "N números")
    def test_minimoNumeroDeElementosYMinimoUnElemento(self):
        self.assertEquals(Procesamiento().procesar("3"), [1,3,3,3], "Un Número")
    def test_minimoNumeroDeElementosYMinimoDosElementos(self):
        self.assertEquals(Procesamiento().procesar("2,7"), [2,2,7,4.5], "Dos números")
    def test_minimoNumeroDeElementosYMinimoNElementos(self):
        self.assertEquals(Procesamiento().procesar("9,7,22,44"), [4,7,44,20.5], "N números")
    def test_NumeroDeElementosMinimoMaximoUnNumero(self):
        self.assertEquals(Procesamiento().procesar("3"), [1,3,3,3], "N números")
    def test_NumeroDeElementosMinimoMaximoDosNumeros(self):
        self.assertEquals(Procesamiento().procesar("3,2"), [2,2,3,2.5], "N números")
    def test_NumeroDeElementosMinimoMaximoNNumeros(self):
        self.assertEquals(Procesamiento().procesar("3,2,8,6"), [4,2,8,4.75], "N números")
    def test_NumeroDeElementosMinimoMaximoPromedioUnNumero(self):
        self.assertEquals(Procesamiento().procesar("3"), [1,3,3,3], "N números")
    def test_NumeroDeElementosMinimoMaximoPromedioDosNumeros(self):
        self.assertEquals(Procesamiento().procesar("3,9"), [2,3,9,6], "N números")
    def test_NumeroDeElementosMinimoMaximoPromedioNNumeros(self):
        self.assertEquals(Procesamiento().procesar("3,9,10,15"), [4,3,15,9.25], "N números")