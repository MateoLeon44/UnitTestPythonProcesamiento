class Procesamiento:
    def procesar(self,cadena):
        if cadena == "":
            return [0,0,0,0]
        elif cadena != "":
            if "," in cadena:
                numeroElementos = 0
                cadena = cadena.split(",")
                numeroElementos = len(cadena)
                return numeroElementos
            else:
                return 1


