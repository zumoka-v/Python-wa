def validar_nota():
    nota = 0
    while ((nota < 1) or (nota > 7)):
        try:
            sueldo = float(input("Ingrese sueldo del artista: "))
            if nota < 1:
                print("Nota muy pequeña, debe ser mayor o igual que 1.0 Intente nuevamente")
            if nota > 7:
                print("Nota muy grande, debe ser menor o igual a 7.0 Intente nuevamente")
        except ValueError:
            print("Debe escribir la nota como numero decimal")
        print("")
    return nota

n1 = validar_nota
print(f"La nota es {n1}")

def validar_sueldo():
    sueldo = 0
    while ((sueldo < 1000000) or (sueldo > 17000000)):
        try:
            sueldo = int(input("Ingrese sueldo del artista: "))
            if sueldo < 1000000:
                print("Sueldo muy bajo, debe ser mayor o igual que 1000000 Intente nuevamente")
            if sueldo > 17000000:
                print("Sueldo muy grande, debe ser menor o igual a 17000000 Intente nuevamente")
        except ValueError:
            print("Debe escribir el sueldo como entero")
        print("")
    return sueldo

def validar_dia():
    dias_validos = ["17-09","18-09","19-09","20-09"]
    while True:
        dia = input("Introduce fecha de el show(17-09,18-09,19-09,20-09)")

        if dia in dias_validos:
            print(f"Fecha {dia} valida correctamente ")
            print("")
            return dia
        else:

def validar_positivo(numero):
    if numero > 0:
        return True
    else:
        return False
    
    
print("Bienvenido a la pampilla Insuco")
print("")

n = int(input("Ingrese cantidad de artistas: "))
validar_positivo(n)
    





def menu():
    print("DIAS QUE HABRA SHOW")
    print("1: 17 de septiembre ")
    print("2: 18 de septiembre ")
    print("3: 19 de septiembre ")
    print("4: 20 de septiembre ")


def artista(s):
    while True:
        try:
            n=s
            x=int(input(f"Ingrese un rango de 1 hasta {n}: "))
            if 0<= x or n> x:
                print(f"Invalido debe ser un numero entre el rango de 1 hasta {n}")
            else:
                return x 
        except ValueError:
            print("Opcion Invalida, debe colocar un numero entero")