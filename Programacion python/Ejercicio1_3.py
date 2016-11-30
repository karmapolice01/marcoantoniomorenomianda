#Marco Antonio Moreno Miranda
#Martes, 29 de noviembre del 2016
import numpy as r
import math

lat1= input("Introduce la latitud 1: ")
lat2= input("Introduce latitud 2: ")
long1= input("introduce la longitud 1: ")
long2= input("Introduce la longitud 2: ")

def func(lat1, lat2, long3, long2):

    x1= (lat1*180/3.1416)
    x2= (lat2*180/3.1416)
    x3= (long1*180/3.1416)
    x4= (long2*180/3.1416)

    distancia= 6371.01*math.acos(math.sin(x1)*math.sin(x2) + math.cos(x1)*math.cos(x2)*math.cos(x3-x4))
    print distancia

print func(lat1, lat2, long1, long2)
