"""
Diego Diaz
Ci:27352609
"""

import random

def Apostar():

    tiradas = 0
    dinero = 100

    while dinero > 99:
        tiradas += 1
        dinero -= 100

        dado = random.randrange(1, 6)

        if(dado > 3):
            dinero += 200
    return tiradas

if __name__ == "__main__":
    print(Apostar())
    