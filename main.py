from pessoa import *
from time import sleep
'''
def escolhendo_nome_jogador():
    print(f"Olá, Bem vindo ao mundo de Pokemon")
    sleep(1)
    print(f"qual era mesmo o seu nome?")
    sleep(1)

    for i, nome in enumerate(NOMES):
        print(f"{i} --> {nome}")
        sleep(0.2)
    print(f'{len(NOMES)} --> outro')
    nome = int(input("Jogador: Meu nome é "))
    if nome == 0:
        return NOMES[0]
    if nome == 1:
        return NOMES[1]
    if nome == 2:
        return NOMES[2]
    if nome == 3:
        return NOMES[3]
    if nome == 4:
        return NOMES[4]
    if nome == 5:
        nome = input("Digite seu nome:")
        print("Que nome bonito!")
        return nome
    
def escolher_pokemon_inicial(player):
    print(f"então seu nome é {player}")
    sleep(1)
    print("Sinta-se livre para capturar seu primeiro pokemon")
    sleep(1)

    global rival 
    while True:
        print("1 --> Bulbassauro\n2 --> Charmander\n3 --> Squirtle")
        sleep(1)
        pokemon_inicial = int(input("Digite qual pokemon você deseja: "))
        sleep(0.5)
        nome = input("deseja color um nome?[n(não)/s(sim)]")
        while True:
            if nome in "nN":
                nome = None
                break
            elif nome in "sS":
                nome = input("Nome do pokemon:")
                break
            else:
                print("Escreva \"s\" para SIM e \"n\" para NÃO")
            nome = input("deseja color um nome?[n(não)/s(sim)]")
        
        if pokemon_inicial == 1:
            player.capturar_100(PokemonGrama("Bulbassauro",nome=nome))
            rival = Inimigo("Fernando",pokemons=[PokemonFogo("Charmander")])
            break
        elif pokemon_inicial == 2:
            player.capturar_100(PokemonFogo("Charmander",nome=nome))
            rival = Inimigo("Fernando",pokemons=[PokemonAgua("Squirtle")])            
            break
        elif pokemon_inicial == 3:
            player.capturar_100(PokemonAgua("Squirtle",nome=nome))         
            rival = Inimigo("Fernando",pokemons=[PokemonGrama("Bulbassauro")])
            break

        else:
            print("****por favor escolha do numero de 1 a tres****\n")
    
jogador = Player(escolhendo_nome_jogador())
escolher_pokemon_inicial(jogador)
jogador.mostrar_pokemons()
'''

jogador = Player("Raul",[PokemonGrama("Bulbassauro")])
rival = Inimigo("Gary",[PokemonFogo("Charmander")])
def batalha_inicial(rival):
    jogador.batalhar(rival)

batalha_inicial(rival)



