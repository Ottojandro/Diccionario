class libro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    def __str__(self):
        if self.disponible: 
            self.estado = "Disponible"
        else: 
            self.estado = "Prestado"
        return f"{self.codigo}{self.titulo}{self.autor}{self.estado}"
    
            
        
class usuario:
    def __init__(self, nombre, identificacion, libros_prestados):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []
    
class biblioteca:
    def __init__(self, coleccion_de_libros, usuarios):
        self.coleccion_de_libros = []
        self.usuarios = []
        
