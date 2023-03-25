class Pokemon:
    def __init__(self, tipo, nome): # toda vez que instanciar um objeto essa metodo vai ser usada/construtor
        self.tipo = tipo
        self.nome = nome

meu_pokemon = Pokemon("fogo","charmander")
pokemon_do_joao_erik = Pokemon("eletrico","pikachu")
print(meu_pokemon.tipo)