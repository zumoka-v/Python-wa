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
    x = i%4
    if (x == 1):
        dias_validos = ["17-09","18-09","19-09","20-09"]
        while True:
         dia = input("Introduce fecha de el show(17-09,18-09,19-09,20-09)")

         if dia in dias_validos:
            print(f"Fecha {dia} valida correctamente ")
            print("")
            if(dia == "17-09"):
                c17 = c17 + 1
            if(dia == "18-09"):
                c18 = c18 + 1
            if(dia == "19-09"):
                c19= c19 + 1
            if(dia == "20-09"):
                c20 = c20 + 1
            return dia
         else: 
                print("Fecha no valida, Intentelo nuevamente")
    if(x == 2):
        
def validar_positivo(numero):
    while True:
        try:
            numero = int(input("Introduce cantidad de artista: "))
            if numero > 0:
                print(f"La cantidad {numero} es positiva")
                return numero
            else: 
                print("La cantidad no es positiva, Intentelo nuevamente")
        except ValueError:
            print("Entrada no valida; porfavor Introcude numero")

def control_prosupusto(a,b):
    pres_actual: 0
    pres_actual = a - b
    return pres_actual

def control_dia(n):
    for i in range(n):
        x = n%4
        if (x == 1):
            print("")
        
        if (x == 2):
            print("")

        if (x == 3):
            print("")

        if (x == 4):
            print("")

nombre =[]
apellido = []
apodo = []
dia = []
sueldo = []    

pres = 17000000
    
print("Bienvenido a la pampilla Insuco")
print("")

n = validar_positivo()
print("")
print(f"Prosupuesto inicial es {pres}")

for i in range (n):
    print ("ARTISTA ", i+1)
    nombre.append (input(("Ingrese nombre del artista: ")))
    apellido.append (input(("Ingrese apellido del artista: ")))
    apodo.append (input(("Ingrese el apodo del artista: ")))






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