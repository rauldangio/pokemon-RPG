import random
from pokemon import *

NOMES = ["joao","raul","cre","RRR","gary"]



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
                print(f"\t{pokemon} --> {pokemon.especie}")
        else:
            print(f"{self} Nao tem pokemon!")


class Player(Pessoa):
    tipo = "player"

    def capturar_66(self,pokemon):
        if (random.randint(1,3) >= 2):
            self.pokemons.append(pokemon)
            print(f"{self} capturou {pokemon}")
        else:
            print(f"{self} não conseguiu capturar o {pokemon}!")

    def capturar_100(self,pokemon):
        self.pokemons.append(pokemon)
        print(f"{self} capturou {pokemon}")

class Inimigo(Pessoa):
    tipo = "inimigo"
    
    def __init__(self, nome=None, pokemons=[]):
        super().__init__(nome, pokemons)   
        if not pokemons:
            for i in range (6):
                r = random.randint(1,3)
                if  r== 1:
                    poke = PokemonAgua("Squirtle")
                elif r == 3:
                    poke = PokemonFogo("Charmander")
                elif r == 2:
                    poke = PokemonGrama("Bulbassauro")

                self.pokemons.append(poke)
