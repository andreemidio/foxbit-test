import argparse
import sys

from sty import fg

from rover.plato import Plato
from rover.posicao import Posicao
from rover.rover import Rover


def main():
    parser = argparse.ArgumentParser(description='Rover Test')
    parser.add_argument('--largura', help='largura', default=5)
    parser.add_argument('--altura', help='altura', default=5)
    parser.add_argument('--x', help='x', default=1)
    parser.add_argument('--y', help='y', default=2)
    parser.add_argument('--direcao', help='y', default="N")
    parser.add_argument('--processamento', help='processamento', default="LMLMLMLMM")

    argumentos = parser.parse_args()

    plateau = Plato(int(argumentos.largura), altura=int(argumentos.altura))
    position = Posicao(int(argumentos.x), y=int(argumentos.y))
    rover = Rover(plateau, position, Rover.DIRECOES.get(argumentos.direcao))
    rover.processamento(comandos=argumentos.processamento)
    color = fg(201) + str(rover) + fg.rs
    print(color)


if __name__ == "__main__":
    sys.exit(main())
