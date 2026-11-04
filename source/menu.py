##############      Desenvolvido por Eduarda, Ramom e João Vítor Lira      ###############
##############      Apresentamos o nosso jogo ...      ##################################
##############          Math_Game            #############################################
from multiprocessing.resource_sharer import stop
import jogo_iniciar

def menu():
    print(" Seja bem-vindo(a) ao Math_Game! ")
    escolha  = input(" Você deseja participar do jogo? (S/n): ")
    if escolha == "S" or escolha == "s" and escolha == "N" or escolha == "n":
        jogo_iniciar.jogo_iniciar()

    while escolha != "S" or "s" and escolha != "N" or "n":
        escolha_2 = input("Resposta incorreta! Tente novamente.. (S/N):" )

        if escolha_2 == "S" or escolha_2 == "s" and escolha_2 == "N" or escolha_2 == "n":
            jogo_iniciar.jogo_iniciar()
