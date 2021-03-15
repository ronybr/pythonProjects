import random

class GuessGame:
    def __init__(self, number, random_number):
        self.number = number
        self.random_number = random_number

    def guess_number(self):
        return self.number == self.random_number

print("######### Welcome to Guess Number Game #########\n")

result = False
attempts = 7
secret_number = random.randint(1, 100)
while result is False:

    player_number = int(input("Escolha um numero de 1 a 100 "))
    obj_player = GuessGame(player_number, secret_number)
    result = obj_player.guess_number()

    if secret_number > player_number:
        attempts -= 1
        if attempts == 0:
            print("############################################")
            print("O jogo acabou! voce usou todas as tentativas")
            print("############################################")
            break
        else:
            print("Voce errou o palpite, escolha um numero MAIOR.")
            print("Voce ainda tem", attempts, "tentativas. O maximo sao 7\n")
    else:
        print("Voce errou o palpite, escolha um numero MENOR.")
        attempts -= 1
        print("Voce ainda tem", attempts, "tentativas. O maximo sao 7\n")
        continue
else:
    print("PARABENS!! Voce acertou o numero.")
    print("Total de tentativas utilizadas:", 7 - attempts, "\nO maximo sao 7")