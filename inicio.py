print("----- Calcular Definitiva -----")

nombre = input("Nombre estudiante: ")

n1=float(input("Nota 1: "))
n2=float(input("Nota 2: "))
n3=float(input("Nota 3: "))

defnt = (n1+n2+n3)/3

if defnt>=3:
    print("Aprueba el curso")
else:
    print("Reprueba el curso")
    
    
# Verificar si alguna de las notas es negativa
if n1 < 0 or n2 < 0 or n3 < 0:
    print("Error: Las notas no pueden ser negativas")
elif n1 > 5 or n2 > 5 or n3 > 5:
    print("Error: Las notas no pueden ser mayores que 5")
else:
    print(nombre + " Su nota definitiva es: ", defnt)
    
if defnt<=2:
    print("Problemas de atención")
elif defnt < 3 and defnt >= 2:
    print("puede Recuperar")
elif defnt < 4 and defnt >= 3:
    print("Muy bien, aprobó")
elif defnt < 4.6 and defnt >= 4:
    print("Eres Genial")
elif defnt>4.6:
    print("You are the best")
    
    
    
    
    