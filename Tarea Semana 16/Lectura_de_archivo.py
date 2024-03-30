#Abrir el archivo
archivo=open("my_notes.txt","r")
#Metodo readline para leer las lineas
Linea1= archivo.readline()
Linea2= archivo.readline()
Linea3= archivo.readline()
#Mostrar cada linea
print(Linea1)
print(Linea2)
print(Linea3)
archivo.close()
#Metodo write para escribir en el archivo
archivo=open("my_notes.txt","a") #Utilizamos "a" para agregar al archivo, ya que al utilizar "w" como ya existe eliminaria y remplazaria por lo nuevo que se va a escribir
archivo.write("\nTelefono:993543513")#La nueva linea se puede visualizar en el archivo
archivo.close()






