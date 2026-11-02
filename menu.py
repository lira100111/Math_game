##############      Desenvolvido por Eduarda, Ramom e João Vítor Lira      ###############
##############      Apresentamos o nosso jogo ...      ##################################
##############          Math_Game            #############################################
from multiprocessing.resource_sharer import stop
import jogo_iniciar

def menu():
    print(" Seja bem-vindo(a) ao Math_Game! ")
    escolha  = input(" Você deseja participar do jogo? (S/n): ")

    if escolha == "S" or escolha == "s":
        jogo_iniciar.jogo_iniciar()

    elif escolha == "N" or escolha == "n":
        print("Encerrando...")
