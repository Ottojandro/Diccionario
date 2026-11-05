estudiantes = [
    {"nombre": "Ana", "promedio": 4.4},
    {"nombre": "Luis", "promedio": 2.8},
    {"nombre": "Maria", "promedio": 3.9},
    {"nombre": "Carlos", "promedio": 2.5},
    {"nombre": "Sofia", "promedio": 3.2}
]

print("Estudiantes con promedio mayor o igual a 3.0:")

for estudiante in estudiantes:
    if estudiante["promedio"] >= 3.0:
        print(estudiante["nombre"], "- Promedio:", estudiante["promedio"])