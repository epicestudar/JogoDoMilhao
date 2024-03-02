
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

    print("Bem-vindo ao Quem Quer Ser um Milionário?\n")

    perguntas_embaralhadas = random.sample(perguntas, len(perguntas))

    for pergunta in perguntas_embaralhadas:
        exibir_pergunta(pergunta)
        resposta = input("\nQual é a sua resposta? ").strip()

        if verificar_resposta(pergunta, resposta):
            print("\nResposta correta! Você ganhou dinheiro!\n")
            dinheiro += 66.666
        else:
            print("\nResposta incorreta! Fim de jogo!\n")
            break

    print("Pontuação final: $", dinheiro)

if __name__ == "__main__":
    jogar()
