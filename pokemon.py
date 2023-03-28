import random
from time import sleep
class Pokemon:
    def __init__(self,especie, nome=None, level = None): # toda vez que instanciar um objeto essa metodo vai ser usada/construtor
        self.especie = especie
        if nome:
            self.nome = nome
        else:
            self.nome = especie
        
        if level:
            self.level = level
        else:    
            self.level = random.randint(4,5)

        self.vida = self.level * 4
        self.dano = int(self.vida / 3.4)
        self.vivo = True
    
    def __str__(self):
        return f"{self.nome}({self.level})"
    

    def atacar(self, pokemon, bonus = 1):
        dano = int(random.randint(self.dano - 2, self.dano + 1) * bonus)
        rng = random.randint(0,1) 
        sleep(1)
        sleep(0.5)
        if rng == 5:
            dano = dano * 2
            print(f"{self} Critou!")
        elif rng == 0:
            dano = 0
            print(f'{self} ERROU!!!!')
        print(f"{self} causou {dano} de dano!")
        pokemon.vida -= dano 
    
        if pokemon.vida <= 0:
            pokemon.vida = 0
            pokemon.vivo = False
        print(f"{pokemon} esta com {pokemon.vida} de vida!")
        sleep(0.5)
      


class PokemonEletrico(Pokemon): # classe filha do Pokemon
    tipo = "eletrico"

    def atacar(self,pokemon):
        print(f"{self} usou choque do trovao em {pokemon}!") # sobreescrevendo o metodo atacar (overwrite)
        super().atacar(pokemon)


    def dar_choque(self):
        print(f"{self} deu choque")


class PokemonFogo(Pokemon): # classe filha do Pokemon
    tipo = "fogo"
    
    def atacar(self,pokemon):
        print(f"{self} usou firethrower em {pokemon}!") # sobreescrevendo o metodo atacar (overwrite)
        if pokemon.tipo == "grama":
            super().atacar(pokemon,bonus=1.1)
            print("EFETIVO FOGO >>> GRAMA")
        else:
            super().atacar(pokemon)

    def fogoPelaBoca(self):
        print(f"{self} Soltou fogo pela boca")


class PokemonAgua(Pokemon): # classe filha do Pokemon
    tipo = "agua"
    
    def atacar(self,pokemon):
        print(f"{self} usou watergun em {pokemon}!") # sobreescrevendo o metodo atacar (overwrite)
        if pokemon.tipo == "fogo":
            super().atacar(pokemon,bonus=1.1)
            print("EFETIVO AGUA >>> FOGO")
        else:
            super().atacar(pokemon)

    def cuspiu(self):
        print(f"{self} cuspiu!")


class PokemonGrama(Pokemon): # classe filha do Pokemon
    tipo = "grama"
    
    def atacar(self,pokemon):
        print(f"{self} usou lifeseed em {pokemon}!") # sobreescrevendo o metodo atacar (overwrite)
        if pokemon.tipo == "agua":
            super().atacar(pokemon,bonus=1.1)
            print("EFETIVO GRAMA >>> AGUA")
        else:
            super().atacar(pokemon)



    def plantouTrigo(self):
        print(f"{self} plantou trigo")




