import forca
import adivinhacao

def escolher_jogo():
    print("********************************")
    print("Selecione o jogo que deseja jogar!")
    print("********************************")

    print("1 - Adivinhação")
    print("2 - Forca")

    while True:
        jogo_selecionado = int(input("Escolha o seu jogo(Apenas números): "))

        if jogo_selecionado == 1:
            print("Jogando adivinhação!")
            break
        elif jogo_selecionado == 2:
            print("Jogando forca!")
            break
        else:
            print("Selecione um jogo válido!")

    if jogo_selecionado == 1:
        adivinhacao.jogar()
    else:
        forca.jogar()


if __name__ == "__main__":
    escolher_jogo()