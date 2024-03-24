#Diccionario que contiene informacion ficticia sobre una persona

informacion_personal={
    "Nombre": "Eric",
    "Edad":23,
    "Ciudad":"Los Angeles",
    "Profesion":"Cantante"
}
#Acceder al valor asociado (con clave "ciudad") y modificarlo con otra ciudad
informacion_personal["Ciudad"]="Seoul"
#Agregar un nuevo-valor que represente "profesion" y modificarlo
informacion_personal["Profesion"]="Bailarin"

#Verificar si la clave "telefono" existe en el diccionario
#Si no existe agregar un numero ficticio
informacion_personal["Telefono"]="822403022212"

#Eliminar la clave "edad", no es necesaria
del informacion_personal["Edad"]

#Imprimir el diccionario final
print(informacion_personal)

