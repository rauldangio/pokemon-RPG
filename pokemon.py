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
        return f"{self.nome} ({self.level})"
    
    def atacar(self, pokemon):
        print(f"o pokemon {self.especie} atacou {pokemon.especie}!")

meu_pokemon = Pokemon("fogo","charmander",level=5)
pokemon_do_joao_erik = Pokemon("eletrico","pikachu")
pokemon_do_joao_erik.atacar(meu_pokemon)
pokemon_do_gabriel = Pokemon("grama","bulbassauro",nome="tonico")

print(meu_pokemon)
print(pokemon_do_gabriel)

