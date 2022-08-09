#Rodrigo Pineda
#Condiciones Compuestas (Notas)
#CondicionesCompuestas.py

Nombre=input("Ingrese Nombre")
Curso=input("Ingrese El nombre del curso")
print("")
datoUno=int(input("Ingrese dato uno"))
datoDos=int(input("Ingrese dato dos"))
datoTres=int(input("Ingrese dato tres"))
datoCuatro=int(input("Ingrese dato cuatro"))

print("")
print("")

NotaTotal=(datoUno+datoDos+datoTres+datoCuatro)/4
if NotaTotal >= 60:
    print("Curso:", Curso)
    print("Nombre:", Nombre)
    print("Total:", NotaTotal)
    print("**EL ALUMNO APROBO**")
else:
    print("Curso:", curso)
    print("Nombre:", Nombre)
    print("Total:", NotaTotal)
    print("**EL ALUMNO REPROBO**")
    
print("Gracias por usar nuetro porograma")




