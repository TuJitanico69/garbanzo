fichero = input("Introduce la ruta del fichero: ")


archivo = open (fichero, "r")
salida = open ("c:\\salida.txt", "w")
while 1:
    linea = archivo.readline()
    salida.write(linea)
    if linea == "":
        break
    print (linea)
archivo.close()
salida.close()   


     
