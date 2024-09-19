class Eletrodomestico:
    def __init__(self, cor, voltagem, preco, estado=False):
        self.cor = cor
        self.voltagem = voltagem
        self.preco = preco
        self.estado = estado

    def ligaOuDesliga(self):
        if self.estado == False:
            self.estado = True
        else:
            self.estado = False

    def stats(self):
        print(f"O aparelho está: {'Ligado' if self.estado else 'Desligado'}")



class Computador(Eletrodomestico):
    def __init__(self, cor, voltagem, preco, processador, placa_mae, ram, memoria, placa_de_video):
        super().__init__(cor, voltagem, preco, estado=False)
        self.processador= processador
        self.placa_mae = placa_mae
        self.ram = ram
        self.memoria = memoria
        self.placa_de_video = placa_de_video

c1 = Computador("Branco", "220", "5500", "i9 14a", "B760M", "16GB", "SSD 1TB", "RTX 4060")
c1.stats()
c1.ligaOuDesliga()
c1.stats()