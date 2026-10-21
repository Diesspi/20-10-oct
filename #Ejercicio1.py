#Ejercicio1
#Diego Espinosa Galarza
#Imprima los valores de la lista con un bucle cuando sean pares o impares

lista = [10,21,4,45,66,93,11]
for i in lista:
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")