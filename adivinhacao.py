import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha a dificuldade: ")
    print("(1)-Aprendiz (2)-Mestre (3)-Grão mestre")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentativas = 15
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print ("Você digitou:", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue


        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto

        if(acertou):
            print("******************************************")
            print("Você acertou e fez um total de {} pontos!!".format(pontos))
            print("******************************************")
            break
        else:
            if(maior):
                print("***************************************")
                print("Você errou!! O seu chute foi muito alto")
                print("***************************************")
            elif(menor):
                print("****************************************")
                print("Você errou!! O seu chute foi muito baixo")
                print("****************************************")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    if(acertou):
        print("Fim do jogo. Parabéns")
    else:
        print("Fim de jogo. O número secreto era --{}--.".format(numero_secreto))

if (__name__ == "__main__"):
    jogar()