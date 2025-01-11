import os
import random

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