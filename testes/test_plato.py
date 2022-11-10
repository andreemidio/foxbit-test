from rover.plato import Plato
from rover.posicao import Posicao


def test_load_plato():
    plato = Plato(5, 5)
    assert plato.MIN_ALTURA == 0
    assert plato.MIN_LARGURA == 0
    assert plato.largura == 5
    assert plato.altura == 5


def test_plato_position():
    plato = Plato(5, 5)
    posicao = Posicao(1, 2)

    direcao = plato.direcao_disponivel(posicao)
    assert direcao is True
