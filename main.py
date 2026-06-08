from clases.libro import Libro
from clases.revista import Revista
from clases.socio import Socio
from clases.prestamo import Prestamo

a = Libro("La sirenita","Pececitos", "1999", "Cosme fulanito", "infantil", "465468468")

b = Socio("42123456", "Agustina", "Herrera",3)

p = Prestamo(1, "07/06/2026", b, a, False)

print(p)