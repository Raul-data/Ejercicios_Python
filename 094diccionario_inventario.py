# Crea un diccionario con productos y su stock inicial. Después, pide operaciones del tipo: "producto cantidad" con signo (+5, -3, etc.) para entrada o salida de mercancía. Actualiza el diccionario. Al final, muestra los productos con , y .


stock = {
    "pan" : 10,
    "leche" : 4,
    "arroz" : 7
}

operacion = ""

while operacion != "fin":
    operacion = input("Introduce operacion (producto cantidad) o  fin: ")
    
    if operacion != "fin":
        partes = operacion.split()
        producto = partes[0]
        cantidad = int(partes[1])
        
        if producto in stock:
            stock[producto] += cantidad
        else:
            print("Producto no existe")
            
print(stock)
    
    