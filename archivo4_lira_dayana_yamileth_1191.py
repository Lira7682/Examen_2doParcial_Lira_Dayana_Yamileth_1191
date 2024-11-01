print (" ")#espacio
print ("Lira Hernandez Dayana Yamileth 1191 3W")#datos del realizador
print (" ")#espacio

nombre = input("ingresa tu nombre")#solicita ingresar nombre
edad = input("ingresa tu edad")#solicita ingresar edad
direccion = input("ingresa tu direccion")#solicita ingresar direccion
telefono = input("ingresa tu numero de telefono")#solicita ingresar telefono

datos = { #abre diccionario
    "nombre": nombre, #da valores
    "edad": edad, #da valores
    "direccion": direccion, #da valores
    "telefono": telefono #da valores
} #cierra diccionario

print(f"{datos['nombre']} tiene {datos['edad']} años,")#imprime mensaje con datos
print(f"vive en {datos['direccion']}")#imprime mensaje con datos
print(f"y su número de teléfono es {datos['telefono']}.")#imprime mensaje con datos

print(" ")#espacio
