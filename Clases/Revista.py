class Revista(Material):
    def __init__(self, titulo, editorial, ano, numero, fecha):
        super().__init__(titulo, editorial, ano)
        self.numero = numero
        self.fecha = fecha 
        