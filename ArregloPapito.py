def promedio_curso(n1,n2,n3,n4,n5):
    prom = 0
    prom = (n1+n2+n3+n4+n5)/5
    return prom

def promedio_notas(n1,n2,n3,p1,p2,p3):
    prom = 0
    prom = (p1*n1+p2*n2+p3*n3)/100
    return prom

notas = [0,0,0]
alumnos = [0,0,0,0,0]
apellidos = [0,0,0,0,0]
p = [20,30,50]

print("Bienvenido Papito al INSUCO")
print("")

for i in range (0,5,1):
    print(f"ALUMNO {i+1}")
    alumnos[i] = (input("Ingrese nombre del alumno: "))
    apellidos[i] = (input("Ingrese apellido del alumno: "))
    notas[0] = float(input("Ingrese primera nota: "))
    notas[1] = float(input("Ingrese segunda nota: "))
    notas[2] = float(input("Ingrese tercera nota: "))

    prom = promedio_notas(notas[0],notas[1],notas[2],p[0],p[1],p[2])
    print(f"El promedio del alumno es {prom}")


