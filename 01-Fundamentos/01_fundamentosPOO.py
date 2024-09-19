class Pessoa:
    def __init__ (self, nome, nacionalidade, idade, vivo=True):
        print("Inicializando classe...")
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.idade = idade
        self.vivo = vivo
    
    def dizer_nome(self):
        print(f"Oi, meu nome é {self.nome}")
    
    def estado(self):
        print(f"{'Estou Vivo' if self.vivo else 'Estou morto'}")

    def morre(self):
        self.vivo = False


p1 = Pessoa("João Pedro", "Brasileiro", 20)
p1.dizer_nome()
p1.morre()
p1.estado()


p2 = Pessoa("Eduardo Carvalho", "Brasileiro", 19)
p2.dizer_nome()
p2.estado()