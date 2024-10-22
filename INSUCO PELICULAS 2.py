def validar_genero(genero): 
    generos_validos = ["Acción", "Romance", "Terror","Comedia","Infantil"]
    return genero in generos_validos

def validar_año(año):
    return 2000 <= año <= 2024

# Crear las películas
peliculas = [
    {                
        "nombre": "Blue Lock: Episodio Nagi",
        "protagonista": "Nagi Seishiro",
        "antagonista": "Isagi Yoichi",
        "director": "Shunsuke Ishikawa",
        "genero": "Acción",
        "año": 2024,
        "visualizaciones": 3000000
    },
    {                
        "nombre": "The Batman",
        "protagonista": "Bruce wayne",
        "antagonista": "riddler",
        "director": "Matt Reeves",
        "genero": "Acción",
        "año": 2022,
        "visualizaciones": 30000000
    },
        {                
        "nombre": "Iron Man: el hombre de hierro",
        "protagonista": "Tony Stark",
        "antagonista": "Iron Monger",
        "director": "Jon Favreau",
        "genero": "Acción",
        "año": 2008,
        "visualizaciones": 40000000
    },
    {
        "nombre": "Cómo perder a un hombre en 10 días",
        "protagonista": "Andie Anderson",
        "antagonista": "Benjamin Barry",
        "director": "Donald Petrie",
        "genero": "Romance",
        "año": 2003,
        "visualizaciones": 10000000
    },
        {
        "nombre": "Diario de una pasión",
        "protagonista": "Noah Jr",
        "antagonista": "Allie Hamilton",
        "director": "Nick Cassavetes",
        "genero": "Romance",
        "año": 2004,
        "visualizaciones": 20000000
    },
        {
        "nombre": "bajo la misma estrella",
        "protagonista": "Hazel Grace Lancaster",
        "antagonista": "Augustus Waters",
        "director": "Josh Boone",
        "genero": "Romance",
        "año": 2014,
        "visualizaciones": 25000000
    },

    {
        "nombre": "La cabaña",
        "protagonista": "Mack Phillips",
        "antagonista": "Sarayu",
        "director": "Stuart Hazeldine",
        "genero": "Terror",
        "año": 2017,
        "visualizaciones": 12000000
    },

        {
        "nombre": "Evil Dead: El Despertar",
        "protagonista": "Ellie",
        "antagonista": "Mr. Fonda",
        "director": "Lee Cronin",
        "genero": "Terror",
        "año": 2023,
        "visualizaciones": 32000000
    },
    {
        "nombre": "Payaso siniestro",
        "protagonista": "El Payaso",
        "antagonista": "Sarah",
        "director": "Damien Leone",
        "genero": "Terror",
        "año": 2013,
        "visualizaciones": 38000000
    },
    {
        "nombre": "Supercool",
        "protagonista": "McLovin",
        "antagonista": "Evan",
        "director": "Greg Mottola",
        "genero": "Comedia",
        "año": 2007,
        "visualizaciones": 50000000
    },
     {
        "nombre": "¿Qué pasó ayer?",
        "protagonista": "Alan Garner",
        "antagonista": "Leslie Chow",
        "director": "Todd Phillips",
        "genero": "Comedia",
        "año": 2009,
        "visualizaciones": 35000000
    },
    {
        "nombre": "Damas en guerra",
        "protagonista": "Megan",
        "antagonista": "Helen Harris III",
        "director": "Paul Feig",
        "genero": "Comedia",
        "año": 2011,
        "visualizaciones": 37000000
    },
     {
        "nombre": "Cars",
        "protagonista": "Rayo McQueen",
        "antagonista": "Chick Hicks",
        "director": "John Lasseter",
        "genero": "Infantil",
        "año": 2006,
        "visualizaciones": 60000000
    },
        {
        "nombre": "Cars 2",
        "protagonista": "Rayo McQueen",
        "antagonista": "Finn McMissile",
        "director": "John Lasseter",
        "genero": "Infantil",
        "año": 2011,
        "visualizaciones": 50000000
    },
        {
        "nombre": "Cars 3",
        "protagonista": "Rayo McQueen",
        "antagonista": "Jackson Storm",
        "director": "John Lasseter",
        "genero": "Infantil",
        "año": 2017,
        "visualizaciones": 580000000
    },
    
]

# Preguntar por el género deseado
genero_deseado = input("¿Qué género deseas ver? (Romance, Acción, Terror, Comedia, Infantil): ")

if not validar_genero(genero_deseado):
    print("Género no válido. Por favor, elige entre Romance, Acción o Terror.")
else:
    # Variables para calcular visitas
    total_visitas = 0
    max_visitas = 0
    min_visitas = float('inf')
    pelicula_max = None
    pelicula_min = None

    # Validar y mostrar información de las películas del género deseado
    for pelicula in peliculas:
        if pelicula["genero"] == genero_deseado and validar_año(pelicula["año"]):
            print(f"Nombre: {pelicula['nombre']}, Protagonista: {pelicula['protagonista']}, "
                  f"Antagonista: {pelicula['antagonista']}, Director: {pelicula['director']}, "
                  f"Género: {pelicula['genero']}, Año: {pelicula['año']}, "
                  f"Visualizaciones: {pelicula['visualizaciones']}")

            # Calcular total de visitas
            total_visitas += pelicula["visualizaciones"]

            # Determinar película con más y menos visitas
            if pelicula["visualizaciones"] > max_visitas:
                max_visitas = pelicula["visualizaciones"]
                pelicula_max = pelicula

            if pelicula["visualizaciones"] < min_visitas:
                min_visitas = pelicula["visualizaciones"]
                pelicula_min = pelicula

    # Mostrar película con más y menos visitas
    if pelicula_max and pelicula_min:
        print(f"\nPelícula con más visitas: {pelicula_max['nombre']} ({pelicula_max['visualizaciones']} vistas)")
        print(f"Película con menos visitas: {pelicula_min['nombre']} ({pelicula_min['visualizaciones']} vistas)")

    # Calcular y mostrar promedio de visitas
    if total_visitas > 0:
        promedio_visitas = total_visitas / (1 if pelicula_max is None else 2) 
        print(f"Promedio de visualizaciones: {promedio_visitas:.2f}")
    else:
        print("No hay películas para mostrar en este género.")
