import flet as ft
import random
import os

class Jogo_da_forca():
    def __init__(self, page):
        self.page = page
        self.palvras_categorias = {
            "frutas": ["maçã", "banana", "laranja", "uva", "manga", "morango", "abacaxi", "melancia", "pêssego", "cereja"],
            "cidades": ["são paulo", "rio de janeiro", "belo horizonte", "brasília", "salvador", "fortaleza", "curitiba", "manaus", "recife", "porto alegre"],
            "animais": ["cachorro", "gato", "elefante", "tigre", "leão", "girafa", "zebra", "urso", "panda", "coelho"] 
        }
        self.categoria = None
        self.palavra_escolhida = None
        self.letras_descobertas = []
        self.letras_erradas = []
        self.chances = 7
        self.categoria_input = ft.TextField(hint_text="Escolha uma categoria", on_submit=self.escolher_categoria)
        self.letra_input = ft.TextField(hint_text="Digite uma letra", on_submit=self.processar_letra)
        self.status = ft.Text("")
        self.page.add(self.categoria_input, self.letra_input, self.status)
        self.page.update()

    def escolher_categoria(self, e):
        categoria = self.categoria_input.value.lower().strip()
        if categoria in self.palvras_categorias:
            self.categoria = categoria
            self.palavra_escolhida = random.choice(self.palvras_categorias[self.categoria])
            self.letras_descobertas = ["_" for _ in self.palavra_escolhida]
            self.letras_erradas = []
            self.chances = 7
            self.atualizar_status()
        else:
            self.status.value = "Categoria inválida. Tente novamente."
            self.page.update()

    def processar_letra(self, e):
        entrada = self.letra_input.value.lower().strip()
        if len(entrada) == 1 and entrada.isalpha():
            if entrada in self.palavra_escolhida:
                for i, letra in enumerate(self.palavra_escolhida):
                    if letra == entrada:
                        self.letras_descobertas[i] = letra
            else:
                self.chances -= 1
                self.letras_erradas.append(entrada)

            if "_" not in self.letras_descobertas:
                self.status.value = f"Parabéns! Você ganhou. A palavra era '{self.palavra_escolhida}'."
            elif self.chances == 0:
                self.status.value = f"Você perdeu! A palavra era '{self.palavra_escolhida}'."
            else:
                self.atualizar_status()
        else:
            self.status.value = "Entrada inválida. Digite uma letra."
        self.page.update()

    def atualizar_status(self):
        self.status.value = (
            f"Categoria: {self.categoria}\n"
            f"Palavra: {' '.join(self.letras_descobertas)}\n"
            f"Chances restantes: {self.chances}\n"
            f"Letras erradas: {', '.join(self.letras_erradas)}"
        )

def main(page: ft.Page):
    Jogo_da_forca(page)

ft.app(target=main)
