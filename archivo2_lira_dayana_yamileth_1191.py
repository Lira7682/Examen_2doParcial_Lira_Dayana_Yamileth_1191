print (" ")#espacio
print ("Lira Hernandez Dayana Yamileth 1191 3W")#datos del realizador
print (" ")#espacio

credito1 = 7 #da valores
credito2 = 8 #da valores
credito3 = 9 #da valores
credito4 = 10  #da valores 
credito5 = 9 #da valores
credito6 = 10 #da valores

materias = { #abre diccionario
    "historia :" : 7, #dato almacenado
    "matematicas :" : 8, #dato almacenado
    "ecosistemas :" : 9, #dato almacenado
    "metodologia :" : 10, #dato almacenado
    "humanidades :" : 9, #dato almacenado
    "programacion :" : 10, #dato almacenado
} #cierra diccionario

# funcion que recorre tanto las claves como los valores 
for x, y in materias.items():
    print(x, y)

print(" ") #espacio

suma = credito1 + credito2 + credito3 + credito4 + credito5 + credito6 #operacion

print(f"La suma de los creditos es : {suma}.") #resultado de la operacion

print(" ")#espacio

