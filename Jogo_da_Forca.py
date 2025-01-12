import os
import random

def desenhar_forca(chances):
    estagios = [
        "------\n|    |\n|\n|\n|\n|    ======",
        "------\n|    |\n|    O\n|\n|\n|    ======",
        "------\n|    |\n|    O\n|    |\n|\n|    ======",
        "------\n|    |\n|    O\n|   /|\n|\n|    ======",
        "------\n|    |\n|    O\n|   /|\\\n|\n|    ======",
        "------\n|    |\n|    O\n|   /|\\\n|   /\n|    ======",
        "------\n|    |\n|    O\n|   /|\\\n|   / \\\n|    ======"
    ]
    
    print(estagios[7 - chances])


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

def categoria_palavras():
    palvras_categorias = {
        "frutas": ["maçã", "banana", "laranja", "uva", "manga", "morango", "abacaxi", "melancia", "pêssego", "cereja"],
        "cidades": ["são paulo", "rio de janeiro", "belo horizonte", "brasília", "salvador", "fortaleza", "curitiba", "manaus", "recife", "porto alegre"],
        "animais": ["cachorro", "gato", "elefante", "tigre", "leão", "girafa", "zebra", "urso", "panda", "coelho"] 
    }
    
    for categorias in palvras_categorias.keys():
        print(f"Categoria: {categorias}")
        
    entrada = input("Digite a categria escolhida: ").lower().strip()
    
    while entrada not in palvras_categorias.keys():
        print("Digite uma das categorias existentes")
        entrada = input("Digite a categoria  escolhida: ").lower().strip()
        
    print(f"Categoria escolhida para o jogo {palvras_categorias[entrada]}\n")    
    return palvras_categorias[entrada]
  
def reiniciar_jogo():
    escolha = input("Deseja jogar novamente digite [S] para continuar, ou sair [N] para encerrar: ")
    while escolha not in ["S", "N"]:
        if isinstance(escolha,str):
            if escolha.upper() == "S":
                jogo_da_forca()
            elif escolha.upper() == "N":
                break
            else:
                print("escolha invalida")
              
    
def jogo_da_forca():
    palavras = categoria_palavras()
    palavra_escolhida = random.choice(palavras)
    letras_descobertas = ["_" for _ in palavra_escolhida]
    letras_erradas = []
    chances = 7

    while chances > 0:
        exibir_status(chances, letras_descobertas, letras_erradas)
        entrada = input("Digite uma letra: ").lower()

        if len(entrada) != 1 or (not entrada.isalpha() and entrada != " "):
            print("Por favor, digite apenas uma letra ou espaço.")
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
            print(f"Parabéns, você ganhou! A palavra era '{palavra_escolhida}'.\n")
            reiniciar_jogo()
            
        

    if "_" in letras_descobertas:
        print(f"Você perdeu! A palavra era '{palavra_escolhida}'.")
        reiniciar_jogo()

if __name__ == "__main__":
    jogo_da_forca()
  
     