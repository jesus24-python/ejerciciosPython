'''
calcular el pago de 3 productos en una factura incluyendo el IVA.
SE DEBE MOSTRAR EL NOMBRE DE CADA PRODUCTO, EL PRECIO DE CADA UNO Y EL PAGO TOTAL EN LA FACTURA
'''
# primer producto
print("ingresar el primer producto")
p1 = input()
print("cantidad comprada de ",p1)
p1_cant = int(input())
print("valor unidad de ",p1)
p1_vu = int(input())

# segundo producto
print ("segundo producto: ")
p2 = input()
print("cantidad compra de ",p2)
p2_cant = int(input())
print("valor unidad de ",p2)
p2_vu = int(input())

#tercer producto
print("tercer primer producto: ")
p3 = input()
print("cantidad compra de ",p3)
p3_cant = int(input())
print("valor unidad de ",p3)
p3_vu = int(input())

#calcular los subtotales
# subtotal del primer producto
p1_st = p1_cant * p1_vu
# segundo producto
p2_st = p2_cant * p2_vu
# tercer producto
p3_st = p3_cant * p3_vu

# obtener subtotal
st_total = p1_st + p2_st + p3_st
IVA = st_total * 0.13
total = st_total + IVA

# imprimir resultados
print("el total a pagar por",p1, "es: ",p1_st)
print("el total a pagar" ,p2,"es: ",p2_st)
print("el valor total a pagar por ",p3, "es:",p3_st)
print("el subtotal total es:",st_total)
print("IVA:",IVA)
print("total a pagar con IVA es:",total)

