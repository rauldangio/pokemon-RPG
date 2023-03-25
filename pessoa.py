from pokemon import *

class Pessoa():
    def __init__(self,nome="Anonimo",pokemons=[]):
        self.nome = nome
        self.pokemons = pokemons
    def __str__(self):
        return f"{self.nome}"

    def mostrar_pokemons(self):
        for pokemon in self.pokemons:
            print(pokemon.__str__())


class Player(Pessoa):
    tipo = "player"


class nimigo(Pessoa):
    tipo = "inimigo"
  
    
pokemon_do_raul = PokemonGrama("Bulbassauro",level=5)
eu = Player("Raul",[pokemon_do_raul])
print(eu)
eu.mostrar_pokemons()