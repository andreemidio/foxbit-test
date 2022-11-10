from .posicao import Posicao


class Rover(object):
    COMANDOS = {
        'M': 'mover',
        'L': 'Virar_Esquerda',
        'R': 'Virar_Direita',
    }

    DIRECOES = {
        'N': 1,
        'E': 2,
        'S': 3,
        'W': 4,
    }

    topo = DIRECOES['N']

    def __init__(self, plato, posicao, topo):

        self.plato = plato
        self.posicao = posicao
        self.topo = topo

    def __str__(self):
        return self.posicao_atual

    def set_position(self, x, y, heading):
        if not isinstance(self.posicao, Posicao):
            self.posicao = Posicao(x, y)
        else:
            self.posicao.x = x
            self.posicao.y = y

        self.topo = heading

    @property
    def posicao_atual(self):
        return f'{self.posicao.x} {self.posicao.y} {self.get_heading}'

    @property
    def get_heading(self):
        directions = list(self.DIRECOES.keys())

        try:
            direction = directions[self.topo - 1]
        except IndexError:
            direction = 'N'
            print('Direction error...')

        return direction

    def processamento(self, commands):
        for i in range(len(commands)):
            self.executar(commands[i])

    def executar(self, command):
        if 'L' == command:
            self.virar_esquerda()
        elif 'R' == command:
            self.virar_direita()
        elif 'M' == command:
            if not self.move():
                print("Where are you trying to go?")
        else:
            print("Wrong parameters!..")

    def move(self):
        if not self.plato.direcao_disponivel(self.posicao):
            return False
        # Assume that the square directly North from (x, y) is (x, y+1).
        if self.DIRECOES['N'] == self.topo:
            self.posicao.y += 1
        elif self.DIRECOES['E'] == self.topo:
            self.posicao.x += 1
        elif self.DIRECOES['S'] == self.topo:
            self.posicao.y -= 1
        elif self.DIRECOES['W'] == self.topo:
            self.posicao.x -= 1

        return True

    def virar_esquerda(self):
        self.topo = self.DIRECOES['W'] if (self.topo - 1) < self.DIRECOES['N'] else self.topo - 1

    def virar_direita(self):
        self.topo = self.DIRECOES['N'] if (self.topo + 1) > self.DIRECOES['W'] else self.topo + 1
