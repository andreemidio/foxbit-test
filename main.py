from rover.plato import Plato
from rover.posicao import Posicao
from rover.rover import Rover


def main():
    plateau = Plato(5, 5)
    position = Posicao(1, 2)
    rover = Rover(plateau, position, Rover.DIRECOES.get('N'))
    rover.processamento("LMLMLMLMM")
    print(rover)  # prints 1 3 N

    rover.set_position(3, 3, Rover.DIRECOES.get('E'))
    rover.processamento("MMRMMRMRRM")
    print(rover)  # prints 5 1 E


if __name__ == "__main__":
    main()
