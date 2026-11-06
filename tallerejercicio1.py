nombre_completo=input("Escribe tu nombre completo:")
edad=int(input("Escribe tu edad"))
estatura=float(input("Escribe tu altura en cm (Ejemplo: 1.76 cm)"))
ciudad=input("Escribe en la ciudad en que tu vives")

caracteres=len(nombre_completo)

if edad <= 18:
    print("Es menor de edad")
elif 18 >= edad <=30:
    print("Es adulta")
else:
    print("Es adulto mayor")

if edad % 2 == 0:
    print("La edad par")
else:
    print("La edad es impar")
    
print(f"Tu nombre es: {nombre_completo.upper()} la cantidad de caracteres que tiene tu nombre es:{caracteres} la ciudad es:{ciudad}")

#punto 2#

cantidad = 0

while cantidad < 1:
    cantidad = int(input("¿Cuántos números deseas ingresar? (Debe ser mayor o igual a 1): "))
    if cantidad < 1:
        print("¡Error! La cantidad debe ser al menos 1. Inténtalo de nuevo.")
        
numeros=[]
for i in range(cantidad):
    nu=int(input("Escribe los numeros"))
    numeros.append(nu)
    

