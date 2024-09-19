
class Conta:
    def __init__(self, _saldo=0):
        self._saldo = _saldo

    def deposito(self, valor):
        self._saldo += valor


c1 = Conta()
c1.deposito(500)
print(c1._saldo)