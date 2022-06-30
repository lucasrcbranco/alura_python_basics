from random import randrange


def jogar():
    dar_boas_vindas()

    palavra_secreta = gerar_palavra_secreta()

    # Gerando a palavra mascarada
    palavra_mascarada: list = ["_" for letra in palavra_secreta]

    # Variáveis de apoio
    enforcou: bool = False
    acertou: bool = False
    erros: int = 0
    tentativas: int = 0

    while not acertou and not enforcou:
        print(f"A palavra é {palavra_mascarada} e tem {len(palavra_mascarada)} letras. Você tem {6 - erros} "
              f"tentativas restantes.")
        letra_usuario: chr = input("Digite uma letra: ").strip().lower()
        tentativas += 1

        if letra_usuario in palavra_secreta:
            verificar_letra_usuario(letra_usuario, palavra_secreta, palavra_mascarada)
        else:
            erros += 1
            enforcou = erros > 5

        acertou = "_" not in palavra_mascarada

    if enforcou:
        print("Você perdeu, tente novamente!")
    else:
        print(f"{palavra_mascarada}")
        print(f"Você acertou a palavra secreta em {tentativas} tentativas! Parabéns! ")


def dar_boas_vindas():
    print("********************************")
    print("Bem vindo ao jogo da forca!")
    print("********************************")


def gerar_palavra_secreta():
    palavras_secretas: tuple = \
        ("Banana", "Laranja", "Acerola", "Conserto",
         "Algoz", "Escopo", "Pertinente", "Iniquidade")
    indice_aleatorio: int = randrange(0, len(palavras_secretas))

    return palavras_secretas[indice_aleatorio].strip().lower()


def verificar_letra_usuario(
        letra_usuario: chr,
        palavra_secreta:str,
        palavra_mascarada: list):
    index: int = 0
    for letra in palavra_secreta:
        if letra == letra_usuario:
            palavra_mascarada[index] = letra
        index += 1


if __name__ == "__main__":
    jogar()
