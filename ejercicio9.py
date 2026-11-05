materias = {"Matematicas": 3.8, "Espanol": 4.2, "Ingles": 4.5, "Fisica": 3.0, "Historia": 3.5}

suma_notas = sum(materias.values())
promedio_materias = suma_notas / len(materias)

print("El promedio de las materias es:", promedio_materias)