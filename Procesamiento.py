class Procesamiento:
    def procesar(self,cadena):
        if cadena == "":
            return [0,0,0,0]
        elif cadena != "":
            if "," in cadena:
                return 2
            else:
                return 1


