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
    nu=float(input(f"Ingresa el número {i + 1}: "))
    numeros.append(nu)
    
print("Numeros totales ingresados:", numeros)
    
def calcular_suma_promedio(lista):
    suma = 0 
    for numero in lista:
        suma= suma + numero
    promedio = suma/len(lista)
    return suma, promedio

print("La suma y el promedio de los numeros es ",calcular_suma_promedio(numeros))

def encontrar_mayor_menor(lista):
    mayor= lista[0]
    menor= lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
        elif numero < menor:
            menor = numero
    return mayor,menor
def contar_pares_impares(lista):
    pares = 0 
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares
        
def obtener_positivos(lista):
    positivos = []
    for numero in lista:
        if numero>0:
            positivos.append(numero)
    return positivos
        
def obtener_unicos(lista):
    return set(lista)

mayor, menor = encontrar_mayor_menor(numeros)
print(f"El número mayor es {mayor} y el menor es {menor}")
pares, impares = contar_pares_impares(numeros)
print(f"Cantidad de números pares: {pares}, Impares: {impares}")
print("Los números positivos son:", obtener_positivos(numeros))
print("Los valores únicos (sin repetir) son:", obtener_unicos(numeros))

#punto 3#

def invertir_texto(texto):
    if len(texto) <= 1:
        return texto
    return texto[-1] + invertir_texto(texto[:-1])

palabra = input("pon una palabra")
resultado = invertir_texto(palabra)
print("la palabra invertida es:", resultado)

palabra_limpia = palabra.lower().replace(" ", "")
palabra_invertida = invertir_texto(palabra_limpia)

if palabra_limpia == palabra_invertida:
    print("¡Es un palíndromo!")
else:
    print("No es un palíndromo.")
    
contador_vocales = 0
vocales = "aeiouáéíóú"
for letra in palabra.lower():
    if letra in vocales:
        contador_vocales += 1
print("Cantidad de vocales:", contador_vocales)
datos_finales = (palabra, resultado, contador_vocales)
print("Tupla guardada:", datos_finales)

#Punto 4#

estudiantes = []
def calcular_promedio(lista_notas):
    return sum(lista_notas) / len(lista_notas)
for i in range(3):
    print(f"\n--- Registro del estudiante {i + 1} ---")
    nombre = input("ingrese el nombre: ")
    codigo = input("Ingrese el código: ")
    notas = []
    for j in range(3):
        nota = -1
        while nota < 0.0 or nota > 5.0:
            nota = float(input(f"Ingrese la nota {j + 1} (entre 0.0 y 5.0): "))
            if nota < 0.0 or nota > 5.0:
                print("Error la nota debe ser entre 0.0 y 5.0")
        notas.append(nota)
    promedio = calcular_promedio(notas)
    if promedio >= 3.0:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    estudiante = {"nombre": nombre, "codigo": codigo, "notas": notas, "promedio": promedio, "estado": estado}
    estudiantes.append(estudiante)
    
for est in estudiantes:
    print("Nombre:", est["nombre"])
    print("Código:", est["codigo"])
    print("Notas:", est["notas"])
    print("El promedio es:", est["promedio"])
    print("Estado:", est["estado"])
    print("-------------------")
    
#punto 5#

grupo_python = ["Ana", "Luis", "Carlos", "Sofia", "Mateo"]
grupo_datos = ["Sofia", "Mateo", "Laura", "Ana", "Daniel"]

set_python = set(grupo_python)
set_datos = set(grupo_datos)
ambos_grupos = set_python.intersection(set_datos)
print("Estudiantes en ambos grupos:", ambos_grupos)
solamente_phyton = set_python.difference(set_datos)
print("Los que estan solo en phyton son:", solamente_phyton)
solamente_datos = set_datos.difference(set_python)
print("Los que estan solo en datos son:", solamente_datos)
total = set_python.union(set_datos)
total_estudiantes = len(total)
print("Hay en total", total_estudiantes)
lista_ordenada = sorted(total)
print("La lista alfabeticamente ordenada es:", lista_ordenada)

#punto 6#