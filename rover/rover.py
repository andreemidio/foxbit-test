from rover.posicao import Posicao


class Rover:
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
        return f'{self.posicao.x} {self.posicao.y} {self.pegar_topo}'

    @property
    def pegar_topo(self):
        direcoes = list(self.DIRECOES.keys())

        try:
            _direcao = direcoes[self.topo - 1]
        except IndexError:
            _direcao = 'N'
            print('Direção incorreta ...')

        return _direcao

    def processamento(self, comandos):
        for i in range(len(comandos)):
            self.executar(comandos[i])

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
