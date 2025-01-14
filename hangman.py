import random
import os

class Jogo_da_forca():

    def __init__(self):
        self.palvras_categorias = {
            "frutas": ["maçã", "banana", "laranja", "uva", "manga", "morango", "abacaxi", "melancia", "pêssego", "cereja"],
            "cidades": ["são paulo", "rio de janeiro", "belo horizonte", "brasília", "salvador", "fortaleza", "curitiba", "manaus", "recife", "porto alegre"],
            "animais": ["cachorro", "gato", "elefante", "tigre", "leão", "girafa", "zebra", "urso", "panda", "coelho"] 
        }
        self.categoria = self.escolher_categoria()
        self.palavras = self.palvras_categorias[self.categoria]
        self.iniciar_jogo()

    def desenhar_forca(self,chances):
        estagios = [
            "------\n|       |\n|\n|\n|\n|       ======",
            "------\n|       |\n|       O\n|\n|\n|       ======",
            "------\n|       |\n|       O\n|       |\n|\n|       ======",
            "------\n|       |\n|       O\n|      /|\n|\n|       ======",
            "------\n|       |\n|       O\n|      /|\\\n|\n|       ======",
            "------\n|       |\n|       O\n|      /|\\\n|      /\n|       ======",
            "------\n|       |\n|       O\n|      /|\\\n|      / \\\n|       ======"
        ]
        print(estagios[6 - self.chances])        

    def limpar_tela_cli(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")     

    def exibir_status(self, chances, letras_descobertas, letras_erradas):
        self.limpar_tela_cli()
        self.desenhar_forca(chances)
        print("Bem-vindo ao jogo da forca!\n")
        print(f"Chances restantes: {self.chances}")
        print(f"Letras descobertas: {' '.join(letras_descobertas)}")
        print(f"Letras erradas: {', '.join(letras_erradas)}\n")   

    def verificar_letra(self, entrada, palavra_escolhida, letras_descobertas):
        acerto = False
        for i, letra in enumerate(palavra_escolhida):
            if letra == entrada:
                letras_descobertas[i] = letra
                acerto = True
        return acerto   

    def escolher_categoria(self):
        for categorias in self.palvras_categorias.keys():
            print(f"Categoria: {categorias}")
            
        entrada = input("Digite a categoria escolhida: ").lower().strip()
        
        while entrada not in self.palvras_categorias.keys():
            print("Digite uma das categorias existentes")
            entrada = input("Digite a categoria escolhida: ").lower().strip()
            
        print(f"Categoria escolhida para o jogo: {entrada}\n") 
        return entrada  

    def reiniciar_jogo(self):  # <<<--- MUDANÇA AQUI
        while True:
            escolha = input("Deseja jogar novamente? Digite [S] para continuar ou [N] para encerrar: ").upper()
            if escolha == "S":
                self.categoria = self.escolher_categoria()  # <<<--- MUDANÇA AQUI
                self.palavras = self.palvras_categorias[self.categoria]  # <<<--- MUDANÇA AQUI
                self.iniciar_jogo()
                break 
            elif escolha == "N":
                break
            else:
                print("Escolha inválida.") 

    def iniciar_jogo(self):
        self.palavra_escolhida = random.choice(self.palavras)
        self.letras_descobertas = ["_" for _ in self.palavra_escolhida]
        self.letras_erradas = []
        self.chances = 7

        while self.chances > 0:
            self.exibir_status(self.chances, self.letras_descobertas, self.letras_erradas)
            entrada = input("Digite uma letra: ").lower()

            if len(entrada) != 1 or (not entrada.isalpha() and entrada != " "):
                print("Por favor, digite apenas uma letra ou espaço.")
                continue

            if entrada in self.letras_descobertas or entrada in self.letras_erradas:
                print("Você já tentou essa letra. Tente outra.")
                continue

            if self.verificar_letra(entrada, self.palavra_escolhida, self.letras_descobertas):
                print("Boa! Você acertou uma letra.")
            else:
                self.chances -= 1
                self.letras_erradas.append(entrada)
                print("Ops! Essa letra não está na palavra.")

            if "_" not in self.letras_descobertas:
                self.exibir_status(self.chances, self.letras_descobertas, self.letras_erradas)
                print(f"Parabéns, você ganhou! A palavra era '{self.palavra_escolhida}'.\n")
                break 

        if "_" in self.letras_descobertas:
            print(f"voce perdeu! a palavra era {self.palavra_escolhida}")

        self.reiniciar_jogo()  

jogo = Jogo_da_forca()