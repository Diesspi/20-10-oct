#apunte 2
#Diego Espinosa
primos = [2,3,6,7,11,13]
dias = ["lunes","martes","miercoles","jueves","viernes"]
lista = [primos,dias]
peliculas = [ "SP,BN", "El retorno del rey", "2023"]

#imprimir el valor 11 de la lista primos
print(primos[4])

#imprimir lunes de la lista dias
print(dias[0])

#imprimir el 3er elemento de la lista en la posicion 1 de la lista
print(lista[1][2])

#imrpimir el titulo de la primera pelicula
print(peliculas[0])

#acceder a todos los elementos de la lista con un ciclo
print ()
for i in range(6):
 print(primos[i], end=" ")

#Acceder a todos los elementos de la lista con un ciclo
print ()
for i in dias:
    print(i, end=" ")