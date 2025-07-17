# -------------------------------------------------
# Realizado por Erick Moreno
# -------------------------------------------------
# Historial de Navegacion 
# -------------------------------------------------

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None  # Apunta al nodo anterior
        self.siguiente = None # Apunta al nodo siguiente

class HistorialNavegador:
    def __init__(self):
        self.actual = None  # Nodo donde estas actualmente

    def visitar_pagina(self, url):
        # Visita una nueva pagina, elimina las futuras si existen
        nuevo = NodoDoble(url)
        if not self.actual:
            self.actual = nuevo
        else:
            self.actual.siguiente = None  # Borra paginas futuras
            nuevo.anterior = self.actual
            self.actual.siguiente = nuevo
            self.actual = nuevo
        print(f"Visitando: {url}")

    def atras(self):
        # Retrocede si existe pagina anterior
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"Retrocediendo a: {self.actual.dato}")
        else:
            print("No hay pagina anterior.")

    def adelante(self):
        # Avanza si existe pagina siguiente
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"Avanzando a: {self.actual.dato}")
        else:
            print("No hay pagina siguiente.")

    def mostrar_historial(self):
        # Muestra todo el historial desde el principio
        inicio = self.actual
        while inicio and inicio.anterior:
            inicio = inicio.anterior

        if not inicio:
            print("Historial vacio.")
            return

        print("Historial de navegacion:")
        while inicio:
            indicador = "<-- Actual" if inicio == self.actual else ""
            print(f"- {inicio.dato} {indicador}")
            inicio = inicio.siguiente

    def pagina_actual(self):
        # Muestra la pagina donde estas
        if self.actual:
            print(f"Pagina actual: {self.actual.dato}")
        else:
            print("No hay paginas en el historial.")


# -------------------------------
# Simulacion
# -------------------------------

historial = HistorialNavegador()

historial.visitar_pagina("google.com")
historial.visitar_pagina("youtube.com")
historial.visitar_pagina("github.com")
historial.mostrar_historial()
historial.pagina_actual()

historial.atras()
historial.pagina_actual()

historial.atras()
historial.pagina_actual()

historial.adelante()
historial.pagina_actual()

historial.visitar_pagina("stackoverflow.com")  # Al visitar nueva, borra las futuras
historial.mostrar_historial()
