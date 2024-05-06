from random import randint
from colorama import Fore, Back, Style

#CRIA UM LISTA VAZIA
lista_npcs = []

#CRIA BIBLIOTECA DO JOGADOR/PLAYER
player = {
  "nome": "NEGODAFAVELA",
  "level": 1,
  "exp": 0,
  "expMax": 2,
  "hp":100,
  "hpMax": 100,
  "dano": 10
}

# AQUI CRIA UMA FUNÇÃO QUIE CRIA UM DOCIONARIO COM OS ATRIBUTOS NOME, LEVEL,DANO,HP
def criar_npc(level):

  #DICIONARIO
  novo_npc = {
    "nome": f"monstro #{level}",
    "level": level,
    "dano": level * 5,
    "hp":100,
    "hpMax": 100,
    "exp": 7 * level
  }
  return novo_npc



def gerar_npc(n_npcs):
  for x in range(n_npcs):
    novo_npc = criar_npc(x + 1)
    lista_npcs.append(novo_npc)

#PARA CADA NPC NA LISTA IREMOS PRINTAR OS DADOS ,NOME, LEVEL, DANO, HP
def exibir_npcs():
     for npc in lista_npcs:
       exibir_npc(npc)
      


  

def exibir_npc(npc):
    print(Fore.GREEN + Back.YELLOW + f"Nome:{npc['nome']} // Level:{npc['level']} // Dano:{npc['dano']} // HP:{npc['hp']} // exp:{npc['exp']} " + Style.RESET_ALL)


def exibir_player():
    
    print( f"Nome:{player['nome']} // Level:{player['level']} // Dano:{player['dano']} // HP:{player['hp']} // exp:{player['hpMax']} // HP:{player['exp']} // exp:{player['expMax']} ")
    print("----"*20)


def reset_player():
  player["hp"] = player["hpMax"] 


def reset_npc(npc):
  npc["hp"] = npc["hpMax"] 


def level_up():
  if player["exp"] >= player["expMax"]:
     player["level"] += 1
     player["exp"] = 0
     player["expMax"] = player["expMax"] * 2
     player["hpMax"] += 20
     print()


def atacar_npc(npc):
  npc["hp"] -= player["dano"]

#ATACAR_PLAYER(NPC) - PLAYER:HP - NPC:DANO
def atacar_player(npc):
  player["hp"] -= npc["dano"]
 

def exibir_info_batalha(npc):
  
   print(f"{player['nome']} HP:{player['hp']} ||| HP :{player['hp']}/{player['hpMax']}")
   print(f"NPC:{npc['nome']}, ||| HP :{npc['hp']}/{npc['hpMax']} \n")

def iniciar_batalha(npcs, npc_selecionado = 0):
    gerar_npc(5)  # Gera 5 NPCs para lutar
    if npc_selecionado < len(npcs):# Verifica se ainda há NPCs na lista
      npc = npcs[npc_selecionado]# Obtém o NPC atual da lista pelo índice
      reset_player()

      while  player['hp'] > 0 and npc['hp'] > 0:
        exibir_player()
        exibir_npc(npc)
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)
        if not menu():
           break

      if player ['hp'] > 0:
        print(f"O {player['nome']} VENCEU E GANHOU {npc['exp']} DE EXP!")
        print("\n")
        player['exp'] += npc['exp']
        reset_player()
        reset_npc(npc)
        npc_selecionado += 1  # Incrementa o índice para selecionar o próximo NPC
        iniciar_batalha(npcs,npc_selecionado)
      
      
      else:
        print(f"O {npc['nome']} venceu")
        exibir_npc(npc)
        
    level_up()
    reset_npc(npc)
    if npc_selecionado < len(npcs):  # Verifica se ainda há NPCs na lista
        iniciar_batalha(npcs, npc_selecionado)  # Inicia a próxima batalha



def menu():
    while True:  # Loop infinito para garantir que o usuário insira uma opção válida
        try:
            ataque = int(input('Digite 1 se deseja atacar: '))  # Solicita ao usuário que insira sua escolha
            if ataque == 1:  # Verifica se a escolha 
               return True
                  
            else:
                print('DIGITE UMA OPÇÃO VÁLIDA')  # Mensagem de erro se a escolha não for válida
        except ValueError:  # Captura exceção se o usuário inserir um valor não numérico
            print('Por favor, digite um número inteiro.')  # Mensagem de er2ro para entrada não numérica
# CHAMADA DA FUNÇÃO PARA GERAR OS NPCs
gerar_npc(5)

# CHAMADA DA FUNÇÃO PARA INICIAR A BATALHA
iniciar_batalha(lista_npcs)

