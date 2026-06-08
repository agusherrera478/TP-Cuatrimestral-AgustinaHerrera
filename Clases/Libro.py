from clases.material import Material

class Libro(Material):
    def __init__(self, titulo, editorial, ano, autor, genero, id_libro):
        super().__init__(titulo, editorial, ano)
        self.autor = autor
        self.genero = genero
        self.id = id_libro