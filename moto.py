class moto:
    marca=""
    modelo=""
    patente=""
    kilometraje=int(0)
    
    def __init__(self, marca, modelo, patente, kilometraje,):

        self.marca=marca
        self.modelo=modelo
        self.patente=patente
        self.kilometraje=kilometraje

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

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Patente: {self.patente}, Kilometraje: {self.kilometraje}"
        
        
