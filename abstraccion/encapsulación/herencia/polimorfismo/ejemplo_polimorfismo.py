class Ave:
    def sonido(self):
        return "Pío"

class Gallo:
    def sonido(self):
        return "Kikirikí"

# Prueba
for animal in [Ave(), Gallo()]:
    print(animal.sonido())

