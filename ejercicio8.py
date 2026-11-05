inventario={"mouse":"P01","teclado":"P02","pantalla":"P03"}
codigo_buscar=input("Pon el producto que quieres buscar")

if codigo_buscar in inventario:
    print("El producto si existe")
else:
    print("El producto no existe")