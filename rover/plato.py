class Plato:
    MIN_LARGURA = 0
    MIN_ALTURA = 0

    def __init__(self, largura, altura, min_largura=0, min_altura=0):
        self.largura = largura
        self.altura = altura
        self.min_largura = min_largura
        self.min_altura = min_altura

    def direcao_disponivel(self, position):
        return self.min_largura <= position.x <= self.largura and self.min_altura <= position.y <= self.altura
