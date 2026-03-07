
class Calculadora: 
    def __init__(self,valor01,valor02):
        self._valor01=valor01
        self._valor02=valor02
    def soma(self):
        return self._valor01 + self._valor02
    def sub(self):
        return self._valor01 - self._valor02
    def mult(self):
        return self._valor01 * self._valor02
    def div(self):
        return self._valor01 / self._valor02