import argparse

from sty import fg

from rover.plato import Plato
from rover.posicao import Posicao
from rover.rover import Rover


def main(*args, **kwargs):
    plateau = Plato(largura=kwargs.get("largura"), altura=kwargs.get("altura"))
    position = Posicao(x=kwargs.get("x"), y=kwargs.get("y"))
    rover = Rover(plateau, position, Rover.DIRECOES.get(kwargs.get("direcao")))
    rover.processamento(comandos=kwargs.get("processamento"))
    color = fg(201) + str(rover) + fg.rs
    print(color)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rover Test')
    parser.add_argument('--largura', help='largura', default=5)
    parser.add_argument('--altura', help='altura', default=5)
    parser.add_argument('--x', help='x', default=1)
    parser.add_argument('--y', help='y', default=2)
    parser.add_argument('--direcao', help='y', default="N")
    parser.add_argument('--processamento', help='processamento', default="LMLMLMLMM")

    argumentos = parser.parse_args()

    valores = dict(
        largura=int(argumentos.largura),
        altura=int(argumentos.altura),
        x=int(argumentos.x),
        y=int(argumentos.y),
        direcao=argumentos.direcao,
        processamento=argumentos.processamento,
    )

    main(**valores)
