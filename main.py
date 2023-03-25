from pessoa import *
from time import sleep

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
    print("Sinta-se livre para capturar seu primeiro pokemon")
    
    while True:
        print("1 --> Bulbassauro\n2 --> Charmander\n3 --> Squirtle")
        pokemon_inicial = int(input("Digite qual pokemon você deseja: "))
        if pokemon_inicial == 1:
            player.capturar_100(PokemonGrama("Bulbassauro"))
            break
        elif pokemon_inicial == 2:
            player.capturar_100(PokemonFogo("Charmander"))
            break
        elif pokemon_inicial == 3:
            player.capturar_100(PokemonAgua("Squirtle"))
            break
        else:
            print("****por favor escolha do numero de 1 a tres****\n")
    

escolher_pokemon_inicial(Player(escolhendo_nome_jogador()))