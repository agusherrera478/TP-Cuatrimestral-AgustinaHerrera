from abc import ABC, abstractmethod

class Material(ABC):

    def __init__(self, titulo, editorial, ano):
        self.titulo = titulo
        self.editorial = editorial
        self.ano = ano
        self.disponible = True
    def __str__(self):
        return f"Titulo: {self.titulo}, Editorial: {self.editorial}, Ano: {self.ano}"        
