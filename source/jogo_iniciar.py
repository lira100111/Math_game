import time
import json
import random
from pathlib import Path

questoes_nivel = [("Aritmética", "aritmética.json"),
                  ("Equações", "equações.json"),
                  ("Funções", "funções.json"),
                  ("Matrizes", "matrizes.json"),
                  ("Determinantes", "determinantes.json")]

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

    atualizacao = 0
    while atualizacao is not None:
        inc_acerto = 0
        inc_erro = 0

        nome_nivel = questoes_nivel[atualizacao][0]
        arquivo_json = questoes_nivel[atualizacao][1]

        print("Sua questao: {}".format(nome_nivel))
        for q2 in range(3):
            questao = selecionar_questao(arquivo_json)

            try:
                pergunta_q = float(input("{q} - {pergunta} ".format(q = q2+1, pergunta = questao["pergunta"])))


            except ValueError:
                print("Digite uma resposta numérica válida!")
                continue

            if pergunta_q == questao["resposta"]:
                print("Acerto!")
                inc_acerto = inc_acerto + 1

            else:
                print("Erro!")
                inc_erro = inc_erro + 1

            print("Acertos: {}".format(inc_acerto))
            print("Erros: {}".format(inc_erro))

        atualizacao = receber_nivel(atualizacao, inc_acerto)

        if inc_acerto >= 2:
            print("Parabens! Você passou para a fase: {}".format([q2][0]))


def receber_nivel(atualizacao, inc_acerto):

    if inc_acerto >= 2:
        atualizacao = atualizacao + 1

        if atualizacao < len(questoes_nivel):
            print("Avançando para: {}".format(questoes_nivel[atualizacao][0]))
            return atualizacao
        else:
            print("Parabéns!")
            return None

    else:
        print("Você não passou de fase. Voltando ao início...")
        ## Aqui a ideia é fazer a atualização do estado da tupla para que as questões sejam baseadas no nível

def carregar_questoes(arquivo_json):
    caminho = Path(__file__).resolve().parent.parent/ "questões" / arquivo_json

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["questoes"]

def selecionar_questao(arquivo_json):
    questoes = carregar_questoes(arquivo_json)
    questao = random.choice(questoes)

    return questao
