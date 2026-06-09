from clases.libro import Libro
from clases.revista import Revista 
from clases.socio import Socio
from clases.prestamo import Prestamo
from clases.biblioteca import Biblioteca

a = Libro("La sirenita","Pececitos", "1999", "Cosme fulanito", "infantil", "465468468")
#b = Socio("42123456", "Agustina", "Herrera",3)
#p = Prestamo(1, "07/06/2026", b, a, False)
#R = Revista("Casi angeles", "Ataltida", 2007, 10, " Marzo")
#print(R)

biblioteca = Biblioteca()

def menu():
    while True:
        print("\n===== BIBLIOTECA =====")
        print("1 - Registrar socio")
        print("2 - Registrar material")
        print("3 - Buscar material por título")
        print("4 - Registrar préstamo")
        print("5 - Registrar devolución")
        print("6 - Consultar préstamos activos")
        print("7 - Consultar materiales disponibles")
        print("0 - Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            id_socio = len(biblioteca.socios)+1
            socio = Socio(dni, nombre, apellido, id_socio)
            biblioteca.agregar_socio(socio)
            print(f"Socio agregado: {socio}")
 

        elif opcion == "2":
            tipo = input("Tipo de material (libro/revista): ").lower()
            titulo = input("Título: ")
            editorial = input("Editorial: ")
            ano = input("Año: ")

            if tipo == "libro":
                autor = input("Autor: ")
                genero = input("Género: ")
                id_libro = len([m for m in biblioteca.materiales if isinstance(m, Libro)]) + 1
                libro = Libro(titulo, editorial, ano, autor, genero, id_libro)
                biblioteca.agregar_material(libro)
                print(f"Libro agregado: {libro}")

            elif tipo == "revista":
                numero = input("Número: ")
                fecha = input("Fecha (MM/AAAA): ")
                revista = Revista(titulo, editorial, ano, numero, fecha)
                biblioteca.agregar_material(revista)
                print(f"Revista agregada: {revista}")

            else:
                print("Tipo de material inválido")
            

        elif opcion == "3":
            busqueda = input("Ingrese título o palabra clave: ")
            resultados = biblioteca.buscar_material(busqueda)
            if resultados:
                print("Materiales encontrados:")
                for m in resultados:
                    print(m)
            else:
                print("No se encontraron materiales")

        
        elif opcion == "4":
            id_socio = int(input("ID del socio: "))
            id_material = int(input("ID del material: "))

            socio = next((s for s in biblioteca.socios if s.id == id_socio), None)
            material = next((m for m in biblioteca.materiales if getattr(m, 'id', None) == id_material), None)

            if socio and material:
                prestamo = biblioteca.registrar_prestamo(socio, material, "09/06/2026")
                if prestamo:
                    print(f"Préstamo registrado: {prestamo}")
            else:
                print("Socio o material no encontrado")

        
        elif opcion == "6":
            activos = biblioteca.prestamos_activos()
            if activos:
                print("Préstamos activos:")
                for p in activos:
                    print(p)
            else:
                print("No hay préstamos activos")


        elif opcion == "7":
            disponibles = biblioteca.materiales_disponibles()
            if disponibles:
                print("Materiales disponibles:")
                for m in disponibles:
                    print(m)
            else:
                print("No hay materiales disponibles")


        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()