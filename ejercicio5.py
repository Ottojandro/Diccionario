estudiante = {"nombre": "Carlos", "contacto": {"correo": "carlos@ecci.edu.co",
"telefono": "3001234567"},"promedio": 3.5}
print(estudiante["contacto"]["correo"])
def mostrar_estudiante(estudiante):
    print("nombre:", estudiante["nombre"])
    print("promedio:", estudiante["promedio"])
    
    
def aprobo(estudiante):
    return estudiante["promedio"] >= 3.0

mostrar_estudiante(estudiante)
print("aprobo:",aprobo(estudiante))