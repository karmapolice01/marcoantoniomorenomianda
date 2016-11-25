#Marco Antonio Moreno Miranda
#Jueves, 24 de noviembre del 2016
#IMC

peso= input("inserte peso ")
estatura= input("inserte su estatura ")

imc = peso/(estatura*estatura)

if imc < 16:
    print imc, "delgadez severa"
elif imc >16.00 and imc < 16.99:
    print imc, "Delgadez moderada"
elif imc >17.00 and imc < 18.49:
    print "imc", imc, "Delgadez leve"
elif imc >18.5 and imc < 24.99:
    print "imc", imc, "Normal"
elif imc >=25 and imc <30:
    print "imc", imc, "sobrepeso"
elif imc >=30 and imc <40:
    print "imc", imc, "obesidad"
elif imc >=40:
    print "imc", imc, "obesidad morbida"
