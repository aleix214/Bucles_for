#coding: utf­8

valor=int(input("¿Cuántos valores va a introducir?: "))
cuenta=0

if valor < 0:
 print "¡Imposible!"

num=int(input("Escriba un número: "))

for n in range (1,valor+1):
  num2=int(input("Escriba un número más grande que el anterior: "))
  if num2 < num:
    print "No es mayor que el anterior"
