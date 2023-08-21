class moto:
    marca=""
    modelo=""
    patente=""
    kilometraje=int(0)
    patentado=1950
    color=""
    litros=0
    
    def __init__(self, marca, modelo, patente, kilometraje, patentado, color, litros):

        self.marca=marca
        self.modelo=modelo
        self.patente=patente
        self.kilometraje=kilometraje
        self.patentado=patentado
        self.color=color
        self.litros=litros

    def get_marca(self):
        return self.marca
    
    def set_marca(self,marca):
        self.marca=marca
    
    def get_modelo(self):
        return self.modelo
    
    def set_modelo(self,modelo):
        self.modelo=modelo

    def get_patente(self,patente):
        return self.patente
    
    def set_patente(self,patente):
        self.patente=patente

    def get_kilometraje(self):
        return self.kilometraje
    
    def set_kilometraje(self,kilometraje):
        self.kilometraje=kilometraje

    def get_patentado(self):
        return self.patentado
    
    def set_patentado(self,patentado):
        self.patentado=patentado

    def get_color(self):
        return self.color    
    
    def set_color(self,color):
        self.color=color

    def get_litros(self):
        return self.litros

    def set_litros(self,litros):
        self.litros=litros    

    def __str__(self):
        return f"La rarca de la motos es {self.marca}, y su dodelo es {self.modelo}, . La patente es {self.patente}, y tiene {self.kilometraje} Kilómetros. El color es {self.color} y se le pueden cargar {self.litros} litros "
        
        
    @staticmethod
    def MotosConMenosDe1000km(lista_de_motos):
        motos_menos_de_1000km = [moto for moto in lista_de_motos if moto.kilometraje < 1000]
        return motos_menos_de_1000km

    @staticmethod
    def Patentes2021(lista_de_motos):
        patentes_2021 = [moto for moto in lista_de_motos if moto.patentado == 2021]
        return patentes_2021