print (" ")#espacio
print ("Lira Hernandez Dayana Yamileth 1191 3W")#datos del realizador
print (" ")#espacio

materias = ["Matematicas", "Español", "Ecosistemas", "Quimica", "Historia", "Ingles" ]#da valores
# dando valores a la lista
calificaciones = {} # diccionario vacío

for materias in materias: # Hace algo con cada valor de la lista
    calif = input(f"Ingrese la calificacion de {materias}: ")
    #solicita la calificacion de la materia
    calificaciones[materias] = calif
# almacena la calificación en el diccionario vacio

print(" ") # print imprime un espacio

for materias, calif in calificaciones.items():
    # repite los elementos de el diccionario
    print(f"En {materias} has sacado {calif}.") 
    # print imprime las calificaciones para cada materia.

print(" ")#espacio
