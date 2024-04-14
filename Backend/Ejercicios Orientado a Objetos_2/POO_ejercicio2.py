class Pelicula:
    def __init__(self, titulo, director, genero, duracion):
        self.titulo = titulo
        self.director = director
        self.genero = genero
        self.duracion = duracion
    
    def __str__(self):
        return f"Título: {self.titulo}\nDirector: {self.director}\nGénero: {self.genero}\nDuración: {self.duracion} minutos"

# Función para crear instancias de Pelicula
def crear_pelicula():
    titulo = input("Introduce el título de la película: ")
    director = input("Introduce el nombre del director: ")
    genero = input("Introduce el género de la película: ")
    duracion = int(input("Introduce la duración de la película en minutos: "))
    return Pelicula(titulo, director, genero, duracion)

# Crear una lista para almacenar las películas
lista_peliculas = []

# Solicitar al usuario la información de al menos cinco películas y agregarlas a la lista
print("Introduce la información de al menos cinco películas:")
for _ in range(5):
    pelicula = crear_pelicula()
    lista_peliculas.append(pelicula)

# Mostrar las películas en pantalla
print("\nInformación detallada de las películas:")
for i, pelicula in enumerate(lista_peliculas, 1):
    print(f"\nPelícula {i}:")
    print(pelicula)
