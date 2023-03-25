class Pokemon:
    def __init__(self, tipo, nome): # toda vez que instanciar um objeto essa metodo vai ser usada/construtor
        self.tipo = tipo
        self.nome = nome
    
    def __str__(self):
        return f"Tipo: {self.tipo}\nEspecie: {self.nome}"
    
    def atacar(self, pokemon):
        print(f"o pokemon {self.nome} atacou {pokemon.nome}!")

meu_pokemon = Pokemon("fogo","charmander")
pokemon_do_joao_erik = Pokemon("eletrico","pikachu")

pokemon_do_joao_erik.atacar(meu_pokemon)