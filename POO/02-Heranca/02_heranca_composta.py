class Animal:
    def __init__(self, patas, alimentacao):
        self.patas = patas
        self.alimentacao = alimentacao

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    #Kwargs representa chave e argumento: self.patas = patas e self.alimentacao = alimentacao da classe Pai Animal
    def __init__(self, pelos, **kw):
        self.pelos = pelos
        super().__init__(**kw)
    
    def amamentar(self):
        print("Amamentando a cria")


class Ave(Animal):
    #Kwargs representa chave e argumento: self.patas = patas e self.alimentacao = alimentacao da classe Pai Animal
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
    
    def botar_ovos(self):
        print("Botando Ovos")


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, pelos, patas, alimentacao, cor_bico):
        #print(Ornitorrinco.__mro__) #Descomente para entender a ordem de herança desta classe
        super().__init__(pelos=pelos, patas=patas, alimentacao= alimentacao, cor_bico=cor_bico)
    

gato= Gato(pelos="preto", patas=4, alimentacao="Onivoro")
print(gato)
gato.amamentar()

print("\n\n==============================================\n\n")

ornitorrinco = Ornitorrinco(pelos = "cinza", patas = 4, alimentacao = "SEI LA", cor_bico="Amarelo")
print(ornitorrinco)
ornitorrinco.amamentar()
ornitorrinco.botar_ovos()