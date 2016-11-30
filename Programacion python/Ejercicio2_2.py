#Marco Antonio Moreno Miranda
#Viernes, 25 de noviembre del 2016
#Ejercicio 2 tarea 2
tar1= 8.74
tar2= 1.84
def pago(dist):
    tot=((dist/250)*tar2)+ (tar1)
    return tot

dist= int (input("Ingrese la distancia recorrida "))
pagtot= pago(dist)
print "Su total a pagar es de : ", pagtot
