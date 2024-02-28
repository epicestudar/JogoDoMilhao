import random
import perguntas

respostas = []
dinheiro = 0
numero_questoesFaceis = 0
numero_questoesMedias = 0
numero_questoesDificeis = 0

for questao_facil in perguntas.questoes_faceis:
    print("=========================================================")
    print(questao_facil)
    for alternativa_facil in perguntas.alternativas_faceis[numero_questoesFaceis]:
        print(alternativa_facil)

resposta = input("Digite (A, B, C ou D): ").upper()
respostas.append(resposta)
numero_questoesFaceis += 1

if resposta == perguntas.respostas_faceis[numero_questoesFaceis]:
    dinheiro = dinheiro + 66.666
    print("Resposta Correta!")
else:
    print("Resposta Incorreta!")
    numero_questoesFaceis += 1