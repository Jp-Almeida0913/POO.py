class Exemplo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


exemplo = Exemplo(10)
print(exemplo.x)
del exemplo.x
print(exemplo.x)
exemplo.x = 10
print(exemplo.x)