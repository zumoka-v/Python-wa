def validar_edad():
    edad = 0
    while ((edad > 0) or (edad > 100)):
        try:
            edad = int(input("Ingrese edad del alumno: "))
            if edad < 1:
                print("La edad es muy pequeña debe ser un mayor numero")
            if edad > 100:
                print("La edad muy grande debe ser menor o igual")
        except ValueError:
                print("Debe escribir la edad como numero entero")
    return edad



print("Bienvenido al metodo de la burbuja")
print()

n = input("Ingrese dimension del arreglo: ")
edad = [0]*n


for x in range (n):
    edad[x] = validar_edad()


print("Array EDAD")
for x in range (n):
    print(edad[x])

for i in range(0,1,n-1):
    for j in range(0,n-1-i,1):
        aux = edad[j]
        edad[j] = edad[j+1]
        edad[j+1] = aux

print("Array EDAD ordenado")
