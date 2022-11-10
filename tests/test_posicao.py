from rover.posicao import Posicao


def test_posicao():
    posicao = Posicao(1, 2)

    assert posicao.x == 1
    assert posicao.y == 2
    assert posicao.__eq__(posicao) is True
