from clases.material import Material

class Revista(Material):
    def __init__(self, titulo, editorial, ano, numero, fecha):
        super().__init__(titulo, editorial, ano)
        self.numero = numero
        self.fecha = fecha 
    
    def tipo_material(self):
        return "Revista"
    
    def __str__(self):
        return f"{super().__str__()}, Numero: {self.numero}, Fecha: {self.fecha}"