class Explorador:
    def _init_(self):
        self.nombre = "Rastreador Veloz"
        self.vida = 110
        self.sigilo = 70
        self.alcance = 100

    def accion_especial(self):
        return " ¡REVELAR MAPA! Has encontrado un objeto raro y una ruta de escape."

heroe_explorador = Explorador()