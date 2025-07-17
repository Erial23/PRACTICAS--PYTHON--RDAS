# -------------------------------------------------                                                  
# Trabajo: Listas Enlazadas Simples y Dobles
# Realizado por Erick Morenox
# -------------------------------------------------


# Aqui iria el resto del codigo...

# -------------------------------
# Lista Enlazada Simple - Cola
# -------------------------------

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None  # Apunta al siguiente nodo en la cola

class ColaAtencion:
    def __init__(self):
        self.frente = None  # Primero en la cola
        self.final = None   # Ultimo en la cola

    def insertar(self, nombre):
        # Crea una nueva persona y la agrega al final de la cola
        nueva_persona = Persona(nombre)
        if not self.frente:  # Si la cola esta vacia
            self.frente = self.final = nueva_persona
        else:
            self.final.siguiente = nueva_persona
            self.final = nueva_persona

    def eliminar(self):
        # Atiende a la persona del frente (elimina)
        if not self.frente:
            print("La cola esta vacia.")
            return
        eliminado = self.frente.nombre
        self.frente = self.frente.siguiente
        if not self.frente:  # Si quedo vacia
            self.final = None
        print(f"Atendido: {eliminado}")

    def mostrar(self):
        # Muestra las personas en la cola
        actual = self.frente
        if not actual:
            print("La cola esta vacia.")
            return
        print("Cola de atencion:")
        while actual:
            print(f"- {actual.nombre}")
            actual = actual.siguiente


# -------------------------------
# Lista Doblemente Enlazada - Historial
# -------------------------------

class Pagina:
    def __init__(self, url):
        self.url = url
        self.anterior = None  # Apunta a la pagina anterior
        self.siguiente = None # Apunta a la siguiente pagina

class HistorialNavegacion:
    def __init__(self):
        self.actual = None  # Pagina actual

    def insertar(self, url):
        # Visita una nueva pagina, la agrega al historial
        nueva_pagina = Pagina(url)
        if not self.actual:
            self.actual = nueva_pagina
        else:
            nueva_pagina.anterior = self.actual
            self.actual.siguiente = nueva_pagina
            self.actual = nueva_pagina

    def avanzar(self):
        # Ir a la siguiente pagina si existe
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"Pagina actual: {self.actual.url}")
        else:
            print("No hay pagina siguiente.")

    def retroceder(self):
        # Ir a la pagina anterior si existe
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"Pagina actual: {self.actual.url}")
        else:
            print("No hay pagina anterior.")

    def mostrar(self):
        # Muestra el historial completo desde el principio
        inicio = self.actual
        while inicio and inicio.anterior:
            inicio = inicio.anterior  # Va al principio

        if not inicio:
            print("Historial vacio.")
            return

        print("Historial de navegacion:")
        while inicio:
            marcador = "<-- Actual" if inicio == self.actual else ""
            print(f"- {inicio.url} {marcador}")
            inicio = inicio.siguiente


# -------------------------------
# Simulacion
# -------------------------------

print("\n--- Simulacion Cola de Atencion ---")
cola = ColaAtencion()
cola.insertar("Juan")
cola.insertar("Maria")
cola.insertar("Pedro")
cola.insertar("Luisa")
cola.insertar("Carlos")
cola.mostrar()

cola.eliminar()
cola.eliminar()
cola.mostrar()

print("\n--- Simulacion Historial de Navegacion ---")
historial = HistorialNavegacion()
historial.insertar("google.com")
historial.insertar("youtube.com")
historial.insertar("github.com")
historial.insertar("stackoverflow.com")
historial.insertar("chat.openai.com")
historial.mostrar()

historial.retroceder()
historial.retroceder()
historial.mostrar()

historial.avanzar()
historial.mostrar()

