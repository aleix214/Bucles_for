#coding: utf­8

num1 = int(input("Escribe un número entero: "))
num2 = int(input("Escribe un número entero mayor o igual que el anterior: "))

if num2 < num1:
    print("¡Te he pedido un número que sea mayor o igual que el anterior!")
else:
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print("El número {i} es par")
        else:
            print("El número {i} es impar")
