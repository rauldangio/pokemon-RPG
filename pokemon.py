class Pokemon:
    def __init__(self, tipo, especie, level=1, nome=None, ): # toda vez que instanciar um objeto essa metodo vai ser usada/construtor
        self.tipo = tipo
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
    def atacar(self,pokemon):
        print(f"{self} usou choque do trovao em {pokemon}!") # sobreescrevendo o metodo atacar (overwrite)

    def dar_choque(self):
        print(f"{self} deu choque")

pokemon = PokemonEletrico("eletrico","pikachu")
pokemon_do_joao_erik = Pokemon("fogo","charmander")

pokemon.atacar(pokemon_do_joao_erik)
pokemon_do_joao_erik.atacar(pokemon)

pokemon.dar_choque()
