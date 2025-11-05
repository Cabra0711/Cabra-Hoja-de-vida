print("Digite los siguientes datos:")
#Le pedimos al usuario que nos brinde la siguiente informacion
nombre = input("Escribe el nombre de tu producto :")
#Le solicitamos al usuario que ingrese el nombre de su producto
precio = float(input("Ingrese el precio :"))
#Hacemos una variable de precio y otra de float (numeros exactos) para que digite el precio y un input para que digite el precio del producto en la consola
#Declaramos las variables para que el usuario digite su precio
while precio <= 0 : 
    precio = float(input("Digite nuevamente el precio :"))
if precio <= 0:
    print("El precio no es valido")
elif precio > 0:
    print("El precio se ha registrado")
#Utilizamos la variable while para que cuando el usuario ingrese un valor menor o igual a 0 se repita constantemente, hasta que este nos de un valor mayor a 0
#If y elif para se usan como condionales para que el usuario ponga hasta el que el valor sea valido
cantidad = int(input("Ingrese la cantidad :"))
#Declaramos las variables para que el usuario digite su cantidad
#int para una cantidad entera y input para que lo digite en la consola
while cantidad <= 0: 
    cantidad = int(input("Registre nuevamente la cantidad :"))
if cantidad <= 0:
    print("La cantidad no es valida")
elif cantidad > 0:
    print("La cantidad se ha registrado")
#Repetimos el mismo proceso que hicimos arriba con el precio pero cambiando sus variables y sus nombres
    print("los Datos se han registrado correctamente")
#Le hacemos saber al usuario que los datos fueron guardados
#Creamos la variable para que le de al usuario al final los datos que se buscan como el costo total de el precio total por la cantidad de productos
costo_total= precio*cantidad
#Usamos el print para que aparezcan en la consola los datos que guardo el usuario usando el f-string para usar las variables anteriores y que el usuario vea toda la informacion de lo que quiere
print(f"Producto:{nombre}", f"Precio:{precio}", f"Cantidad:{cantidad}", f"Total:{costo_total}")

#EL programa tiene la funcion de pedirle los datos sobre un producto al usuario para al que final haga una operacion matematica (multiplicacion) de cuanta plata se necesitaria para llevar la cantidad productos deseada por el usuario
