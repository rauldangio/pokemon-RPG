from pokemon import *
import random

NOMES = ["joao","raul","cre","RRR","gary"]

class Pessoa():
    def __init__(self,nome="Anonimo",pokemons=[]):
        self.nome = nome
        self.pokemons = pokemons
    def __str__(self):
        return f"{self.nome}"

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f"{self} tem os seguintes pokemons:")
            for pokemon in self.pokemons:
                print(f"-->{pokemon}")
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

class nimigo(Pessoa):
    tipo = "inimigo"
  
    

eu = Player("Raul")
eu.mostrar_pokemons()
eu.capturar(PokemonFogo("charmander"))
eu.mostrar_pokemons()
