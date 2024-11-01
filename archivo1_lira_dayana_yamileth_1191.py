print (" ")#espacio
print ("Lira Hernandez Dayana Yamileth 1191 3W")#datos del realizador
print (" ")#espacio
materias = ["Matematicas", "Español", "Ecosistemas", "Quimica", "Historia", "Ingles" ] # dando valores a la lista
calif = {} # diccionario vacío
for materias in materias: #Hace algo con cada valor de la lista
    calificacion = input(f"¿Que calificacion sacaste en {materias}? ") #Solicita la calificacion de la materia
    calif[materias] = calif #da calificacion

print(" ") #espacio

x = min(calif) # dando minimo
y = max(calif) # dando maximo

if calif: #verifica si la condicion es verdadera
    print(f"Debes recursar la materia de {x}") # print imprime la materia que debe recursar

print(" ")#espacio