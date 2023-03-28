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


    def pokemons_vivos(self):
        vivo = True

        for pokemon in self.pokemons:
            if pokemon.vivo:
                vivo = True
            else:
                vivo = False
        
        return vivo


    def mostrar_pokemons(self):
        if self.pokemons:
            print(f"{self} tem os seguintes pokemons:")
            for pokemon in self.pokemons:
                print(f"\t{pokemon} {pokemon.especie} Vida: {pokemon.vida}")
        else:
            print(f"{self} Nao tem pokemon!")

    def total_dinheiro(self):
        return self.dinheiro    


    def ganhar_dinheiro(self,quantidade):
        self.dinheiro += quantidade
        print(f"Você ganhou R${quantidade}!!! Você esta com R${self.dinheiro}")


    def perder_dinheiro(self,quantidade):
        self.dinheiro -= quantidade
        if self.dinheiro < 0:
            self.dinheiro = 0
        print(f"Você perdeu R${quantidade}!!! Você esta com R${self.dinheiro}")
        



    def mudar_pokemon(self,number = 0):
        if len(self.pokemons) != 1: 
            pokemons_vivos = []
            for c,pokemon in enumerate(self.pokemons):
                if pokemon.vivo:
                    print(f"{c} --> {pokemon}")
                    pokemons_vivos.append(pokemon)
                else:
                    print(f"{pokemon} --> Derrotado")
            poke_change = int(input("Qual pokemon deseja trocar:"))
            while True:
                if self.pokemons[poke_change].vivo:
                    break
                else:
                    print("Escolha algo na lista!")
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
        vitoria = 0
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
                    if not inimigo.pokemons_vivos():
                        print(f"A batalha Acabou, a vida de {inimigo_pokemon} acabou!")
                        print(f"Você Ganhou! {inimigo} perdeu!")
                        self.ganhar_dinheiro(inimigo_pokemon.level * 100)
                        break
                

                
                

            inimigo.escolher_acao(meu_pokemon)
            if meu_pokemon.vida <= 0:
                if not self.pokemons_vivos():
                    print(f"Você Perdeu! {inimigo} ganhou!")
                    self.perder_dinheiro(inimigo_pokemon.level * 100)
                    break
                else:
                    print(f"{meu_pokemon} MORREU!")
                    self.mudar_pokemon()
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
        escolha = 1
        if escolha == 1:
            if len(self.pokemons) > 1 and not self.pokemons[0].vivo:
                self.mudar_pokemon()
            else:
                escolha = 2
        if escolha == 2:
            self.pokemons[0].atacar(pokemon)
            
    def mudar_pokemon(self):
        for pokemon in self.pokemons:
            if pokemon.vivo:
                print(f"Volte {self.pokemons[0]}!")
                self.pokemons[0] = pokemon
                print(f"Batalhe {self.pokemons[0]}!")


    
            
             