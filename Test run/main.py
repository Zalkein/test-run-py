from random import *

numero = randint(1, 10)
print(numero)

adivina = int(input("Que numero espare pensando?: "))

while adivina != numero:
    print('Mal Mal Mal')
    adivina = int(input("Que numero espare pensando?: "))
print("Lo lograste!!!!")


from turtle import *
pensize(4)
for i in range(4):
    forward(100)
    left(90)
preg = input("Rapido di que figura es la siguiente: ")
preg.lower()
while preg != 'Cuadrado': 
    print("mal mal mal")
    preg = input("Rapido di que figura es la siguiente: ")
print("bien")
clear()

circle(40)
preg2 = input("Que figura es esta ahora?: ")
while preg2 != 'Circulo':
    print("mal mal mal")
    preg2 = input("Que figura es esta ahora?: ")
print('bien!')
from time import *
print("Vamos a subir la intensidad  ")
sleep(1)
clear()
def incompleto():
    for i in range(3):
        forward(100)
        left(90)

incompleto()
preg3 = input("que hay que poner ahora?: ")

while preg3 != 'forward(100)':
    print("mal mal mal")
    preg3 = input("que hay que poner ahora?: ")
print("oleeeeeeee")
sleep(0.5)
print("ufff como que esto es muy flojito no?")
sleep(0.5)
clear()
t1 = Turtle()
t2 = Turtle()
t1.speed(8)
t2.speed(8)

t1.shape('turtle')
t2.shape('turtle')
t1.penup()
t2.penup()
t1.goto(250, 100)
t2.goto(-50, 100)
t1.pendown()
t2.pendown()
t1.pensize(2)
t2.pensize(2)
t1.color('Yellow')
t2.color('Yellow')
t1.begin_fill()
for i in range(5):
    t1.forward(100)
    t1.left(144)
t1.end_fill()
t2.begin_fill()
for i in range(18):
    t2.forward(150)
    t2.left(100)
t2.end_fill()

preg5 = int(input("cual de estas 2 es una estrella relacionada con la pelicula de 'principito' (1 - la de 5 puntas | 2 - la otra): "))
while preg5 != 1:
    print("Mal mal mal")
    preg5 = int(input("cual de estas 2 es una estrella relacionada con la pelicula de 'principito' (1 - la de 5 puntas | 2 - la otra): "))
print("siuuuuu")
hideturtle()
input("presiona enter para finalizar...")
exit()
Terminator()
pass
