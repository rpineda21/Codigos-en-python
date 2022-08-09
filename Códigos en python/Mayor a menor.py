#Rodrigo Pineda
#Mayor a menor
#MayorAMenor.py

x = int(input("Escriba el primer numero: "))
y = int(input("Escriba el segundo numero: "))
z = int(input("Escriba el tercer numero: "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

# 1, 2, 3
# a = 1
# c = 3
# b =(1 + 2 + 3) - 1 - 3
# b = 6 - 1 - 3 = 2

print("los numeros ordenados son: {}, {} y {}".format(a, b, c))
