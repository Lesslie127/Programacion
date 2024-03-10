#Funcion que calcula la temperatura promedio de una ciudad durante un periodo de tiempo
def temperaturas_promedio(ciudades_temperaturas):
    temperaturas_promedio={}
    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio= sum(temperaturas)/len(temperaturas)
        temperaturas_promedio[ciudad]=promedio
    return temperaturas_promedio
#Datos de temperaturas por Ciudad y semanas
ciudades_temperaturas={
    "Quito":[18,20,14,21,20],
    "Cuenca":[19,22,17,16,18],
    "Guayaquil":[28,30,26,29,20]
}
#Calcular las temperaturas promedio por ciudad
temperaturas_promedio=temperaturas_promedio(ciudades_temperaturas)
#Mostrar los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}:{promedio:.2f}°C")