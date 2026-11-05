##############      Desenvolvido por Eduarda, Ramom e João Vítor Lira      ###############
##############      Apresentamos o nosso jogo ...      ##################################
##############          Math_Game            #############################################
from multiprocessing.resource_sharer import stop
import jogo_iniciar


def menu():
    print(" Seja bem-vindo(a) ao Math_Game! ")
    escolha = input("Você deseja participar do jogo? (S/n): ")

    while escolha not in ("S", "s", "N", "n"):
        print("Resposta incorreta! Tente novamente...")
        escolha = input("Você deseja participar do jogo? (S/n): ")

    return escolha

def escolha_jogador():
    escolha = menu()
    if escolha == "S" or escolha == "s":
        jogo_iniciar.jogo_iniciar()

    elif escolha == "N" or escolha == "n":
        print("Saindo...")


escolha_jogador()