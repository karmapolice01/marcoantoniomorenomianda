#Marco Antonio Moreno Miranda
dias = int (input ("Inserte dias de viaje "))
horas = int (input ("Inserte horas de viaje "))
minutos= int (input ("Inserte minutos de viaje "))
segundos= int (input ("Inserte segundos de viaje "))
tvs= (dias * 86400) + (horas * 3600) + (minutos * 60) + (segundos)
print tvs
