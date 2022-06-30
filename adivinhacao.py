import random


def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontuacao_jogador = 1000
    print("Selecione a dificuldade em que deseja jogar:")
    print("Nível 1: Fácil")
    print("Nível 2: Médio")
    print("Nível 3: Difícil")

    while total_de_tentativas == 0:
        nivel_selecionado = int(input("Digite o nível(Apenas números) em que você deseja jogar: "))
        if nivel_selecionado == 1:
            total_de_tentativas = 20
        elif nivel_selecionado == 2:
            total_de_tentativas = 10
        elif nivel_selecionado == 3:
            total_de_tentativas = 5
        else:
            print("Insira um nível válido.")

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        numero_usuario = int(input("Digite um número entre 1 e 100: "))
        acertou = numero_secreto == numero_usuario
        maior = numero_usuario > numero_secreto

        if numero_usuario < 1 or numero_usuario > 100:
            print("Digite um número entre 1 e 100")
            continue

        if acertou:
            print(
                f"Você acertou o número secreto em {total_de_tentativas} tentativas e sua pontuação final foi de {pontuacao_jogador}!")
            break
        else:
            if maior:
                total_de_tentativas
                print("Você errou! O seu chute foi maior que o número secreto.")
            else:
                print("Você errou! O seu chute foi menor que o número secreto.")
                pontos_perdidos = abs(numero_secreto - numero_usuario)
                pontuacao_jogador -= pontos_perdidos

    print("Fim do Jogo!")


if __name__ == "__main__":
    jogar()
