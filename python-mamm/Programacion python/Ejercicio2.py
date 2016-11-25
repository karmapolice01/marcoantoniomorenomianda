#Marco Antonio Moreno Miranda
#Jueves, 24 de noviembre del 2016
#ejercicio 2
intereses= 0.04

saldoin= int (input("Inserte saldo"))
saldon=0
for i in range (3):
    saldo= saldoin*1.04
    saldon= saldon + saldo
    print saldon
