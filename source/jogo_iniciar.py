import time
import json
import random
from pathlib import Path

questoes_nivel = [("Aritmética", "aritmética.json"),
                  ("Equações", "equações.json"),
                  ("Funções", "funções.json"),
                  ("Matrizes", "matrizes.json"),
                  ("Determinantes", "determinantes.json")] #Estruturas de dados global com o nome e os arquivos das questões

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
    atualizacao = 0 #A atualização é uma variável com o valor 0 que será incrementada a cada vez que o usuário passar de fase
    
    while atualizacao is not None: #Enquanto a atualização não receber mais valores, o loop rodará 
        list_quest_repet = [] # Lista para contar as perguntas que já foram feitas
        inc_acerto = 0 #Incrementos de erros e acertos
        inc_erro = 0

        nome_nivel = questoes_nivel[atualizacao][0] #A variável nome_nivel pega o indice 0 referente a linha com o valor atual de atualização que é incremenetado a cada vez (Ex: atualizacao = 0:Aritmetica) da estrutura de dados global questoes_nivel. Ex: [Aritmetica] 
        arquivo_json = questoes_nivel[atualizacao][1]  #A variável arquivos_json pega o indice 1 referente a coluna (aritmetica.json) da estrutura de dados global questoes_nivel com o valor atual da atualizacao (Ex: atualizacao = 0:Aritmetica). Portanto: [Aritmetica][aritmetica.json

        print("Sua questao: {}".format(nome_nivel))
        for q2 in range(5):
            questao = anallise_repet(arquivo_json,list_quest_repet)

            try:
                pergunta_q = float(input("{q} - {pergunta} ".format(q = q2+1, pergunta = questao["pergunta"])))

            except ValueError:
                print("Digite uma resposta numérica válida!")
                continue
            
            list_quest_repet.append(questao["id"])

            if pergunta_q == questao["resposta"]:
                print("Acerto!")
                inc_acerto = inc_acerto + 1

            else:
                print("Erro!")
                inc_erro = inc_erro + 1
                
            print("Acertos: {}".format(inc_acerto))
            print("Erros: {}".format(inc_erro))

        atualizacao = receber_nivel(atualizacao, inc_acerto)

        
        
        if inc_acerto >= 3:
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
        escolha_nova = input("Deseja jogar novamente? (S/N)")
        if escolha_nova == "S" or escolha_nova == "s":
            jogo_iniciar()
        else:
            print("Obrigado por jogar! Até a próxima!")
            exit()

        ## Aqui a ideia é fazer a atualização do estado da tupla para que as questões sejam baseadas no nível

def carregar_questoes(arquivo_json):
    caminho = Path(__file__).resolve().parent.parent/ "questões" / arquivo_json

    with open(caminho, "r", encoding="utf-8") as arquivo: 
        dados = json.load(arquivo)

    return dados["questoes"]

def selecionar_questao(arquivo_json): 
     # Pega-se o arquivo_json da função carregar questões 
    questao = random.choice(arquivo_json) # Gera aleatoriamente uma questão

    return questao #Retorna questão como um valor

def anallise_repet(arquivo_json, list_arq_repet): # Função para o tratamento de questões dentro do código
                                                  # com o objetivo de não repeti-las utilizando o argumento list_arq_repet (do método exec_nivel) 
  
    questoes = carregar_questoes(arquivo_json) # Utiliza o método carregar_questões para verfificar o caminho do arquivo json, carregar os dados e retornar o campo "questões"
    questoes_disp = [] #Verifica as questões disponíveis e coloca dentro da tupla 

    for q in questoes:
        if q["id"] not in list_arq_repet: #Verifica os IDs da lista list_arq_repet, e caso eles não sejam os mesmos... 
            questoes_disp.append(q) # Agrupam eles dentro de questoes_disp por meio da função append()

    if not questoes_disp:
        return None

    questoes_novas = selecionar_questao(questoes_disp) #As questões novas então são geradas pelo método selecionar_questoes() utilizando o argumento questoes_disp 

    return questoes_novas # Retorna o valor de questões novas
