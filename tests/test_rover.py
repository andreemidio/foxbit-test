from rover.plato import Plato
from rover.posicao import Posicao
from rover.rover import Rover


def set_up_parameters():
    plato = Plato(5, 5)
    posicao = Posicao(1, 2)

    return plato, posicao


def test_rover():
    plato, posicao = set_up_parameters()

    rover = Rover(plato, posicao, Rover.DIRECOES.get('N'))

    assert rover.posicao.x == 1
    assert rover.posicao.y == 2
    assert rover.plato.MIN_ALTURA == 0
    assert rover.plato.MIN_LARGURA == 0
    assert rover.plato.min_altura == 0
    assert rover.plato.min_largura == 0
    assert rover.DIRECOES.get("N") == 1


def test_rover_processamento():
    plato, posicao = set_up_parameters()

    rover = Rover(plato, posicao, Rover.DIRECOES.get('N'))

    rover.processamento("LMLMLMLMM")
    rover == "1 3 N"
