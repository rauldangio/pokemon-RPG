class Pokemon:
    def __init__(self,especie, level=1, nome=None, ): # toda vez que instanciar um objeto essa metodo vai ser usada/construtor
        self.especie = especie
        if nome:
            self.nome = nome
        else:
            self.nome = especie
        self.level =  level
    
    def __str__(self):
        return f"{self.nome}({self.level})"
    
    def atacar(self, pokemon):
        print(f"o pokemon {self} atacou {pokemon}!")


class PokemonEletrico(Pokemon): # classe filha do Pokemon
    tipo = "eletrico"

    def atacar(self,pokemon):
        print(f"{self} usou choque do trovao em {pokemon}!") # sobreescrevendo o metodo atacar (overwrite)

    def dar_choque(self):
        print(f"{self} deu choque")


class PokemonFogo(Pokemon): # classe filha do Pokemon
    tipo = "fogo"
    
    def atacar(self,pokemon):
        print(f"{self} usou firethrower em {pokemon}!") # sobreescrevendo o metodo atacar (overwrite)

    def fogoPelaBoca(self):
        print(f"{self} Soltou fogo pela boca")


class PokemonAgua(Pokemon): # classe filha do Pokemon
    tipo = "agua"
    
    def atacar(self,pokemon):
        print(f"{self} usou watergun em {pokemon}!") # sobreescrevendo o metodo atacar (overwrite)

    def cuspiu(self):
        print(f"{self} cuspiu!")


class PokemonGrama(Pokemon): # classe filha do Pokemon
    tipo = "grama"
    
    def atacar(self,pokemon):
        print(f"{self} usou lifeseed em {pokemon}!") # sobreescrevendo o metodo atacar (overwrite)

    def plantouTrigo(self):
        print(f"{self} plantou trigo")




