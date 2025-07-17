class Vehiculo:
    def moverse(self):
        print("El vehiculo se mueve")
class Auto(Vehiculo):
    def moverse(self):
        print("El auto se mueve")

    
vehiculo=Vehiculo()
vehiculo.moverse()

auto=Auto()
auto.moverse()