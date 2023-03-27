import random
from time import sleep
from pokemon import *


NOMES = ["joao","raul","cre","RRR","gary"]



class Pessoa():
    def __init__(self,nome = None,pokemons=[], dinheiro = 0):
        if nome:
            self.nome = nome
        else:
            self.nome = NOMES[random.randint(0,len(NOMES)-1)]
        self.pokemons = pokemons
        self.dinheiro = dinheiro


    def __str__(self):
        return f"{self.nome}"

    def pokemon_atual(self):
        for c,pokemon in enumerate(self.pokemons):
            if c == 0:
                return pokemon


    def ganhar_dinheiro(self,quantidade):
        pass


    def mostrar_pokemons(self):
        if self.pokemons:
            print(f"{self} tem os seguintes pokemons:")
            for pokemon in self.pokemons:
                print(f"\t{pokemon} {pokemon.especie} Vida: {pokemon.vida}")
        else:
            print(f"{self} Nao tem pokemon!")


    def mudar_pokemon(self):
        if len(self.pokemons) != 1: 
            for c,pokemon in enumerate(self.pokemons):
                print(f"{c} --> {pokemon}")
            poke_change = int(input("Qual pokemon deseja trocar:"))
            poke_copy = self.pokemons.copy()
            poke_que_sera_trocado = poke_copy[0]
            poke_que_vai_ser_o_primeiro = poke_copy[poke_change]
            self.pokemons[0] = poke_que_vai_ser_o_primeiro
            self.pokemons[poke_change] = poke_que_sera_trocado
            print(f"O {self.pokemons[poke_change]} foi trocado por {self.pokemons[0]}")



    def batalhar(self, inimigo):
        menu = '''
############# MENU ##############
####  1. ATACAR | 3. TROCAR  ####
####  2. FUGIR  |            ####
#################################
        '''
        print(inimigo.pokemon_atual())

        print(f"Você esta desafiando {inimigo}")
        sleep(0.2)
        print(f"Seu {self.pokemon_atual()} Vai lutar!")
        sleep(0.2)
        print()
        while True:
            meu_pokemon = self.pokemons[0]
            inimigo_pokemon = inimigo.pokemons[0]

            print(f"Pokemon Adversario: {inimigo_pokemon} Vida: {inimigo_pokemon.vida}")
            sleep(0.5)
            print(f"Pokemon Atual: {meu_pokemon} Vida: {meu_pokemon.vida}")
            sleep(0.5)
            print(menu)
            op = input("\nOque deseja fazer? ") 
            if op == 2 or op == 'fugir':
                if "Inimigo" in type(inimigo):
                    print("Você esta em batalha! Nao pode sair!")
                else:
                    print("Voce conseguiu fugir!")
                    break
            elif op == '3' or op == 'trocar':
                self.mudar_pokemon()
                meu_pokemon = self.pokemons[0]
            elif op == '1' or op == 'atacar':
                meu_pokemon.atacar(inimigo_pokemon)
                if inimigo_pokemon.vida <= 0:
                    print(f"Você Ganhou! {inimigo} perdeu!")
                    break
                
                if meu_pokemon.vida <= 0:
                    print(f"Você Perdeu! {inimigo} ganhou!")
                    break

            inimigo.escolher_acao(meu_pokemon)
            if meu_pokemon.vida <= 0:
                print(f"Você Perdeu! {inimigo} ganhou!")
                break
            print("#"*60)
            sleep(0.5)



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

    def escolher_acao(self,pokemon):
        escolha = random.randint(1,2)
        if escolha == 1:
            if len(self.pokemons) > 1:
                self.mudar_pokemon()
            else:
                escolha = 2
        if escolha == 2:
            self.pokemons[0].atacar(pokemon)
            
