

class Material(object):

        def __init__(self, titulo, autor, editorial):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.disponible = True

   
        def _str_(self):
        return f"{self.titulo} - {self.autor}"

