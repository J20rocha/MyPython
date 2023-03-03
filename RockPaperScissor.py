import sys
import random

CP = ('rock', 'paper', 'scissor')


def jogador():

    while True:
        jogada = input("What is your play? ->").lower()

        if jogada in (CP):
            print("Your play is " + jogada + ".")
            return CP.index(jogada)

        print("Invalid input")


def jogo():

    jogada = jogador()
    
    #CPplay=0
    CPplay = random.randint(0,2)

    print(CPplay)
    if jogada == CPplay:
        return "Draw!"

    if (jogada+1) % 3 == CPplay:
        return "LOSE!"
    
    return "WIN!"

    
print("This is a game of Rock Paper Scissor")
print("You will play against the computer, which will randomly generate its play")
resultado = jogo()
print("Result: " + resultado+".")
