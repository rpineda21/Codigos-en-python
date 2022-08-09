#Rodrigo Pineda
#Operaciones con dos datos
#OperacionesConDosDatos.py

texto = input("Ingrese nombre: ")
print("")

datoUno = int(input("Ingrese primer dato entero: "))
datoDos = int(input("Ingrese segundo dato entero: "))

print("Selecciona la operacion que desee realizar: ")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
n= int(input("¿Cual opcion quieres?: "))
if n==1:
    resultado = datoUno + datoDos
    
    print(resultado)
if n==2:
    resultado = datoUno - datoDos
    
    print(resultado)
if n==3:
    resultado = datoUno * datoDos
    
    print(resultado)
if n==4:
    resultado = datoUno / datoDos
    
    print(resultado)
