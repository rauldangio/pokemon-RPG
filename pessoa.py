from pokemon import *
import random

NOMES = ["joao","raul","cre","RRR","gary"]

POKEMONS = [
    PokemonAgua("Squirtle"),
    PokemonGrama("Bulbassauru"),
    PokemonFogo("Charmander")
]

class Pessoa():
    def __init__(self,nome = None,pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = NOMES[random.randint(0,len(NOMES)-1)]
        self.pokemons = pokemons


    def __str__(self):
        return f"{self.nome}"


    def mostrar_pokemons(self):
        if self.pokemons:
            print(f"{self} tem os seguintes pokemons:")
            for pokemon in self.pokemons:
                print(f"-->{pokemon} --> {pokemon.especie}")
        else:
            print(f"{self} Nao tem pokemon!")


class Player(Pessoa):
    tipo = "player"

    def capturar(self,pokemon):
        if (random.randint(1,3) >= 2):
            self.pokemons.append(pokemon)
            print(f"{self} capturou {pokemon}")
        else:
            print(f"{self} não conseguiu capturar o {pokemon}!")


class Inimigo(Pessoa):
    tipo = "inimigo"
    
    def __init__(self, nome=None, pokemons=[]):
        super().__init__(nome, pokemons)   
        if not pokemons:
            for i in range (6):
                self.pokemons.append(random.choice(POKEMONS))
    
gary = Inimigo()
print(gary)
gary.mostrar_pokemons()