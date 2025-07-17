"""
 Atributos de un Carro (propiedades o características)
  Métodos de un Carro (acciones o comportamientos)
  es una forma de escribir programas dividiendolos en objetos que representan cosas del muno
  que es una clase
  una plantilla para crear objetos 
  Los atributos son las propiedades que definen las características de un objeto, mientras que los métodos son las funciones que definen las acciones que un objeto puede realizar.
  
  """

class Carro:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.velocidad_actual = 0
        self.combustible = 100
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("El carro está encendido.")
        else:
            print("El carro ya estaba encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad_actual = 0
            print("El carro está apagado.")
        else:
            print("El carro ya estaba apagado.")

    def acelerar(self, cantidad):
        if self.encendido and self.combustible > 0:
            self.velocidad_actual += cantidad
            self.combustible -= cantidad * 0.1
            print(f"Velocidad actual: {self.velocidad_actual} km/h")
        else:
            print("No puedes acelerar. El carro está apagado o sin combustible.")

    def frenar(self, cantidad):
        self.velocidad_actual = max(0, self.velocidad_actual - cantidad)
        print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def repostar(self, cantidad):
        self.combustible += cantidad
        print(f"Combustible actual: {self.combustible} litros")

    def tocar_bocina(self):
        print("¡Beep beep!")

    def informacion(self):
        return f"{self.marca} {self.modelo} {self.año} - {self.color}"
