#Marco Antonio Moreno Miranda
#Viernes, 25 de noviembre del 2016
#Ejercicio 1 tarea 2
import math

def hipotenusa(cat1, cat2):
    sumcat= (cat1**2) + (cat2**2)
    raiz= math.sqrt(sumcat)
    return raiz

cat1= int (input("cateto 1 "))
cat2= int (input("cateto 2 "))
hipotenusa= hipotenusa(cat1, cat2)
print "La hipotenusa es: ", hipotenusa
