import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1)-Jogo da Forca  (2)-Jogo da Adivinhação")

    jogo = int(input("Qual jogo você quer jogar?"))

    if (jogo == 1):
        print("Jogando jogo da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando jogo de Adivinhação")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()