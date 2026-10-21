#Ejercicio 2
#Diego Espinosa
#Pedir al usuario ingresar 10 valores a una lista (Numericos, reales o cadenas)
#Luego invertir el orden de la lista y mostrarla en pantalla.

lista = []
for i in range(10):
    dato=input("valor " + str(i+1) + ": ")
    try:
        dato = int(dato)
    except ValueError:
        try:
            dato = float(dato)
        except ValueError:
            pass
    lista.append(dato)
print("Lista original: ", lista)

lista.reverse()
print("Lista invertida: ", lista)   