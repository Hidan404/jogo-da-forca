import os
import random

"""
def limpar_tela_cli():
    # se for windows executa "cls"
    if os.name == "nt":
        os.system("cls")
    else:
        #caso for linux executa "clear"
        os.system("clear")    


def jogo_da_forca():
    limpar_tela_cli()

    print("Bemvindo ao jogo da forca!\n")
    print("Adivinhe a palvra\n")

    palavras = [
        "maçã",
        "banana",
        "laranja",
        "uva",
        "manga",
        "morango",
        "abacaxi",
        "melancia",
        "pêssego",
        "cereja"
    ]

    palavra_escolhida = random.choice(palavras)
    letras_descobertas = ["_" for letra in palavra_escolhida]

    chances = 10
    letras_erradas = []

    while chances >= 0:
        print(f"chances restantes {chances}")
        print(f"Letras descobertas {letras_descobertas}")
        print(f"Letras erradas {letras_erradas}")

        entrada = input("\nDigite uma letra: ").lower()


        if entrada in palavra_escolhida:
            indice = 0
            for letra in palavra_escolhida:
                letras_descobertas[indice] = letra
            indice+= 1
        else:
            chances-= 1
            letras_erradas.append(entrada)

        if "_" not in letras_descobertas:
            print(f"Parabens vc ganhou a palvra era {palavra_escolhida}")  
            break

    if "_" in letras_descobertas:
        print(f"Voce perderu a palvra era {palavra_escolhida}")


if __name__ == "__main__":
    jogo_da_forca()
    print("irei refatorar ainda ")     
"""    

import os
import random

def desenhar_forca(chances):
    estagios = [
        """
        ------
        |    |
        |    
        |   
        |   
        |   
        ======
        """,
        """
        ------
        |    |
        |    O
        |   
        |   
        |   
        ======
        """,
        """
        ------
        |    |
        |    O
        |    |
        |   
        |   
        ======
        """,
        """
        ------
        |    |
        |    O
        |   /|
        |   
        |   
        ======
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   
        |   
        ======
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   /
        |   
        ======
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |   
        ======
        """
    ]
    # Exibir o estágio correspondente ao número de chances
    print(estagios[10 - chances])

def limpar_tela_cli():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def exibir_status(chances, letras_descobertas, letras_erradas):
    limpar_tela_cli()
    desenhar_forca(chances)
    print("Bem-vindo ao jogo da forca!\n")
    print(f"Chances restantes: {chances}")
    print(f"Letras descobertas: {' '.join(letras_descobertas)}")
    print(f"Letras erradas: {', '.join(letras_erradas)}\n")

def verificar_letra(entrada, palavra_escolhida, letras_descobertas):
    acerto = False
    for i, letra in enumerate(palavra_escolhida):
        if letra == entrada:
            letras_descobertas[i] = letra
            acerto = True
    return acerto

def jogo_da_forca():
    palavras = ["maçã", "banana", "laranja", "uva", "manga", "morango", "abacaxi", "melancia", "pêssego", "cereja"]
    palavra_escolhida = random.choice(palavras)
    letras_descobertas = ["_" for _ in palavra_escolhida]
    letras_erradas = []
    chances = 10

    while chances > 0:
        exibir_status(chances, letras_descobertas, letras_erradas)
        entrada = input("Digite uma letra: ").lower()

        if len(entrada) != 1 or not entrada.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if entrada in letras_descobertas or entrada in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if verificar_letra(entrada, palavra_escolhida, letras_descobertas):
            print("Boa! Você acertou uma letra.")
        else:
            chances -= 1
            letras_erradas.append(entrada)
            print("Ops! Essa letra não está na palavra.")

        if "_" not in letras_descobertas:
            exibir_status(chances, letras_descobertas, letras_erradas)
            print(f"Parabéns, você ganhou! A palavra era '{palavra_escolhida}'.")
            break

    if "_" in letras_descobertas:
        print(f"Você perdeu! A palavra era '{palavra_escolhida}'.")

if __name__ == "__main__":
    jogo_da_forca()
  
     