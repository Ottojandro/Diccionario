def calcular_valor_inventario(prod):
    return prod["precio"] * prod["stock"]

producto = {
    "codigo": "P01",
    "nombre": "Mouse",
    "precio": 45000,
    "stock": 10
}
valor_total = calcular_valor_inventario(producto)
print("El valor total del inventario es:", valor_total)