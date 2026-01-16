class Atacante:
    def __init__(self):
        self.nombre = "Guerrero de Sombras"
        self.vida = 80
        self.ataque = 90
        self.energia = 40

    def accion_especial(self):
        return "¡GOLPE CRÍTICO! Has causado 500 de daño masivo al enemigo."

heroe_atacante = Atacante()