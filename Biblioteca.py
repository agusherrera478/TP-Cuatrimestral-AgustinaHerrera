class Material(ABC):

    def __init__(self, titulo, autor, editorial):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.disponible = True

