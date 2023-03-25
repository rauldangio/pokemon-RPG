from pessoa import *

def escolher_pokemon_inicial(player):
    print(f"Olá {player}, Bem vindo ao mundo de Pokemon")
    print("Sinta-se livre para capturar seu primeiro pokemon")
    print("1 --> Bulbassauro\n2 --> Charmander\n3 --> Squirtle")
    pokemon_inicial = int(input("Digite qual pokemon você deseja: "))
    if pokemon_inicial == 1:
        player.capturar_100(PokemonGrama("Bulbassauro"))
    elif pokemon_inicial == 2:
        player.capturar_100(PokemonFogo("Charmander"))
    elif pokemon_inicial == 3:
        player.capturar_100(PokemonAgua("Squirtle"))

escolher_pokemon_inicial(Player())