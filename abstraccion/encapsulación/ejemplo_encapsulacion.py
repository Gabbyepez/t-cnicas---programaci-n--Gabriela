class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, monto):
        self.__saldo += monto

    def mostrar(self):
        return self.__saldo

# Prueba
c = Cuenta(100)
c.depositar(50)
print(c.mostrar())

