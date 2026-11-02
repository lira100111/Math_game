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

    questao = selecionar_questao()

    print("Sua questao:")
    pergunta_arit = float(input(questao["pergunta"]))

    if pergunta_arit == questao["resposta"]:
        print("Acerto!")

    else:
        print("Erro!")



def carregar_questoes():
    caminho = Path(__file__).parent/ "questões" / "aritmética.json"
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados["questoes"]


def selecionar_questao():
    questoes = carregar_questoes()
    questao = random.choice(questoes)

    return questao

