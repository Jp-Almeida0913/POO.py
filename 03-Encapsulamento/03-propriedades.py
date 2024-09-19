class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("João Pedro Almeida Moreira", 2004)
print(f"\tNome: {pessoa.nome} \n\tIdade: {pessoa.idade}")