class ClerigoDeLuz:
    def __init__(self):
        self.nombre = "Clérigo de Luz"
        self.vida = 100
        self.magia = 80
        self.fe = 100

    def accion_especial(self):
        return "El Clérigo de Luz usa Curación Grupal: todos los aliados recuperan 50 puntos de vida."


if __name__ == "__main__":
    heroe_sanador = ClerigoDeLuz()
    print(heroe_sanador.accion_especial())
