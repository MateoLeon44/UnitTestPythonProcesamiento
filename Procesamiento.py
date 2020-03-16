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
                promedio = 0
                for numero in cadena:
                    promedio = promedio + int(numero)
                    if int(numero) <= numeroMinimo:
                        numeroMinimo = int(numero)
                    if int(numero) >= numeroMaximo:
                       numeroMaximo = int(numero)
                numeroElementos = len(cadena)
                promedio = promedio / numeroElementos
                return [numeroElementos, int(numeroMinimo), int(numeroMaximo), promedio]
            else:
                return [1, int(cadena), int(cadena), int(cadena)]
