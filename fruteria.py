
# PRECIOS STANDARS

productos_tienda = {
    1: {'nombre': 'manzana','precio': 10},
    2: {'nombre': 'pera','precio': 5},
    3: {'nombre': 'uva','precio': 25},
}

carrito_compra = []


print("¡Hola!")
print("El menu del dia es:")
print("Precio por Kilo")
print("")
print("Selecciona tu producto, preciona 0 para terminar pedido")
print("")

for producto_id ,  productos_informacion in productos_tienda.items():
    print(f"{producto_id} - {productos_informacion['nombre']}  ${productos_informacion['precio']}")

while True:
    print("")
    print("")
    opcion = input("Seleciona un producto ingrese exit para terminar compra:   ")
    print("")
    
    if(opcion.lower() == 'exit'):
        break
    
    opcion = int(opcion)
    
    if(opcion in productos_tienda):
          carrito_compra.append(productos_tienda[opcion])
          print(f"Producto añadido al carrito: {productos_tienda[opcion]['nombre']}")
    else:
         print("Opción no válida. Por favor, elija una opción válida.")


print("Contenido final del carrito de compras:")


   
total_carrito = 0

for producto in carrito_compra:
     total_carrito += producto['precio']
     print(f"{producto['nombre']} (${producto['precio']})")
     print("")
     print("")
    
print(f"Total del carrito de compras: ${total_carrito}")
  
        
    
    
    
    



