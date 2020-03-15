import math

class Procesamiento:
    def procesar(self, cadena):
        if cadena == "":
            return [0, 0, 0, 0]
        elif cadena != "":
            if "," in cadena:
                numeroElementos = 0
                cadena = cadena.split(",")
                numeroMinimo = math.inf
                numeroMaximo = 0
                for numero in cadena:
                    if int(numero) <= numeroMinimo:
                        numeroMinimo = int(numero)
                numeroElementos = len(cadena)
                for numeroMax in cadena:
                    if int(numeroMax) >= numeroMaximo:
                        numeroMaximo = int(numeroMax)
                return [numeroElementos, int(numeroMinimo), int(numeroMaximo), 0]
            else:
                return [1, int(cadena), int(cadena), 1]
