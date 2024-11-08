def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multi(a,b):
    return a * b 

def div(a,b):
    return a / b 

def calculadora():
    while True:
        print("selecciones una opcion")
        print("1. suma")
        print("2. resta")
        print("3. multiplicacion")
        print("4. division")
        print("5. salir de la calculadora")

        opcion = input("ingrese una opcion (1,2,3,4,5:)")

        if opcion == "5": 
            print("estas saliendo la calculadora")
            break

        if opcion in ["1","2","3","4"]:
            num1 = float(input("ingrese el primer numero: "))
            num2 = float(input("ingrese el sengundo numero: "))

            if opcion == "1":
                print("la suma es :", suma(num1, num2))

            elif opcion == "2":
                print("la resta es: ", resta(num1, num2))

            elif opcion == "3":
                print("la multiplicacion es: ",multi(num1, num2))

            elif opcion == "4":        
                print("la divicio ews: ", div(num1, num2))

            else:
                print("opcion no validad, por favor intenta de nuevo")
calculadora()
