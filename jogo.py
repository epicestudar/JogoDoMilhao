# jogo.py

import random
from perguntas import perguntas

def exibir_pergunta(pergunta):
    print(pergunta["pergunta"])
    for opcao in pergunta["opcoes"]:
        print(opcao)

def verificar_resposta(pergunta, resposta):
    return resposta.lower() == pergunta["resposta"]

def jogar():
    dinheiro = 0
    nivel_atual = "facil"

    print("Bem-vindo ao Quem Quer Ser um Milionário?\n")
    

    for nivel in ["facil", "medio", "dificil"]:
        if nivel != nivel_atual:
            continuar = input("Você passou para o nível {}. Até o momento, você acumulou ${}. Deseja continuar? (s/n) ".format(nivel, dinheiro)).lower()

            if continuar != "s":
                print(f"Obrigado por jogar!, o seu prêmio em dinheiro foi de $", dinheiro)
                break
            nivel_atual = nivel

        perguntas_embaralhadas = random.sample(perguntas[nivel], len(perguntas[nivel]))

        for pergunta in perguntas_embaralhadas:
            exibir_pergunta(pergunta)
            resposta = input("\nQual é a sua resposta? ").strip()

            if verificar_resposta(pergunta, resposta):
                print("\nResposta correta! Você ganhou dinheiro!\n")
                dinheiro += 66.666 
            else:
                print("\nResposta incorreta! Fim de jogo!\n")
                return

    print("Parabéns! Você completou todas as perguntas e ganhou o prêmio máximo!\nPontuação final: $", dinheiro)

if __name__ == "__main__":
    jogar()
