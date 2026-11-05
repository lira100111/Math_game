##############      Desenvolvido por Eduarda, Ramom e João Vítor Lira      ###############
##############      Apresentamos o nosso jogo ...      ##################################
##############          Math_Game            #############################################
from multiprocessing.resource_sharer import stop
import jogo_iniciar


def menu():
    print(" Seja bem-vindo(a) ao Math_Game! ")
    escolha = input("Pressione (S/s) para iniciar o jogo: ")

    while escolha not in ("S", "s", "N", "n"):
        print("Resposta incorreta! Tente novamente...")
        escolha = input("Pressione (S/s) para iniciar o jogo: ")

    return escolha

def escolha_jogador():
    escolha = menu()
    if escolha == "S" or escolha == "s":
        jogo_iniciar.jogo_iniciar()

escolha_jogador()
jogo_iniciar.jogo_iniciar()