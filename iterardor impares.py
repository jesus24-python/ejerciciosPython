#crear un iterardor para los numeros impares

#limite
limite = 10

#crear iterador
num_iterador = iter(range(1,limite+1,2))

#usar iterador
for num in num_iterador:
    print(num)

    #crear un iterardor para los numeros pares

#limite
limite = 10

#crear iterador
num_iterador = iter(range(0,limite+1,2))

#usar iterador
for num in num_iterador:
    print(num)