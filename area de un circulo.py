#calcular el area de un circulo 
#a = pi * (r * r)

import math #nos permite utilizar ciertas funcionalidades matematicas que estan disponibles en python

print("ingrese el raio del circulo:")
r = float(input())
pi = math.pi
print("el balor de pi es:",pi)
a = pi * (r * r)

#print("el area del circulo con radio de:",r, "es: ",a)

print("el area del circulo con radio de: ",r,"es: ",round (a,4))