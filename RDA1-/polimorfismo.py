
class Pajaro:
    def sonido(self):
        return "Pío pío"
class Gato:
    def sonido(self):
        return "Miau"
def hacer_sonido(animal):
    print(animal.sonido())
pajaro = Pajaro()
gato = Gato()
hacer_sonido(pajaro) 
hacer_sonido(gato)    
