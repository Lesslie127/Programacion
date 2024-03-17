#Programa que calcule el descuento en compras en funcion del monto total de la compra y mostrar el monto final a pagar
#Crear la funcion
def calcular_descuento(monto_total, porcentaje_descuento=35):
    descuento =monto_total*(porcentaje_descuento/100)
    return descuento
#Llamada de la funcion 2 veces
monto_compra_1=127
monto_compra_2=403

descuento_1=calcular_descuento(monto_compra_1)
descuento_2=calcular_descuento(monto_compra_2)
#Salida de los resultados incluye el monto de descuento y monto final a pagar
print(f"Descuento de la compra es de $ {monto_compra_1}: $ {descuento_1} ")
print(f"Descuento de la compra es de $ {monto_compra_2:}: $ {descuento_2}")

