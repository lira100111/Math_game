import time
import json
import random
from pathlib import Path

def jogo_iniciar():
    print(" Vamos ao desafio matemático " )
    print("### Consistirá em 5 níveis de atividades que serão realizadas. ###")
    print("Os níveis são: ")

    print("1 - Aritmética")
    print("2 - Equações")
    print("3 - Funções")
    print("4 - Matrizes")
    print("5 - Determinantes")

    print("Inciando...")
    time.sleep(1)
    exec_nivel()

def exec_nivel(): # Função que executa a logica do código
    inc_acerto = 0
    inc_erro = 0
    questoes_nivel = ["Aritmética", "Equações", "Funções", "Matrizes", "Determinantes"]


    for q1 in questoes_nivel:
        print("Sua questao: {}".format(q1))
        for q2 in range(3):
            questao = selecionar_questao()
            pergunta_q = float(input("{q} - {pergunta} ".format(q = q2+1, pergunta = questao["pergunta"])))

            if pergunta_q == questao["resposta"]:
                print("Acerto!")
                inc_acerto = inc_acerto + 1

            else:
                print("Erro!")
                inc_erro =+ 1

def carregar_questoes():
    caminho = Path(__file__).parent/ "questões" / "aritmética.json"
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados["questoes"]

def selecionar_questao():
    questoes = carregar_questoes()
    questao = random.choice(questoes)

    return questao
