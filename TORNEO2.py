class Participante:
    def __init__(self, nombre, nickname, edad, ranking, genero, pais):
        self.nombre = nombre
        self.nickname = nickname
        self.edad = edad
        self.ranking = ranking
        self.genero = genero
        self.pais = pais

    def __str__(self):
        return f"Nombre: {self.nombre}, Nickname: {self.nickname}, Edad: {self.edad}, Ranking: {self.ranking}, Género: {self.genero}, País: {self.pais}"

def ingresar_participantes(num_participantes):
    participantes = []
    for i in range(num_participantes):
        print(f"\nIngrese los datos del participante {i + 1}:")
        nombre = input("Nombre: ")
        nickname = input("Nickname: ")
        edad = int(input("Edad: "))
        ranking = input("Ranking: ")
        genero = input("Género: ")
        pais = input("País: ")
        
        participante = Participante(nombre, nickname, edad, ranking, genero, pais)
        participantes.append(participante)
    
    return participantes

def mostrar_participantes(participantes):
    print("\nLista de Participantes:")
    for participante in participantes:
        print(participante)

# Ingresar participantes
num_participantes = 10  # Puedes ajustar este número según tus necesidades
participantes = ingresar_participantes(num_participantes)

# Preguntar si son LOCAL o VISITA
local_nicknames = []
visita_nicknames = []

for participante in participantes:
    rol = input(f"\n¿Es el participante '{participante.nickname}' LOCAL o VISITA? (L/V): ").strip().upper()
    if rol == 'L':
        local_nicknames.append(participante.nickname)
    elif rol == 'V':
        visita_nicknames.append(participante.nickname)
    else:
        print("Selección no válida. Por favor, ingresa 'L' para LOCAL o 'V' para VISITA.")

# Mostrar los nicknames de los participantes LOCAL y VISITA
print("\nParticipantes LOCAL:")
for nickname in local_nicknames:
    print(nickname)

print("\nParticipantes VISITA:")
for nickname in visita_nicknames:
    print(nickname)

# Seleccionar torneo
print("\nSeleccione el torneo que desea jugar:")
print("1. MORTAL KOMBAT 11")
print("2. FIFA 2025")
print("3. STREET FIGHTER 6")

# Obtener la selección del usuario
torneo_seleccionado = input("Ingrese el número del torneo: ")

torneos = {
    "1": "MORTAL KOMBAT 11",
    "2": "FIFA 2025",
    "3": "STREET FIGHTER 6"
}

if torneo_seleccionado in torneos:
    print(f"\nHas seleccionado el torneo: {torneos[torneo_seleccionado]}")
else:
    print("\nSelección no válida. Por favor, ingresa un número del 1 al 3.")

