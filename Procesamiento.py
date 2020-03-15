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
                for numero in cadena:
                    if int(numero) <= numeroMinimo:
                        numeroMinimo = int(numero)
                numeroElementos = len(cadena)
                return [numeroElementos, int(numeroMinimo), 0, 0]
            else:
                return [1, int(cadena), 0, 0]
