import turtle
import math

turtle.setworldcoordinates(-400, 0 ,400, 800)

szerokosc_domu = 600
wysokosc_sciany = 200
szerokosc_drzwi = 50
wysokosc_drzwi = 90
bok_dachu = 600/math.sqrt(2)

zolw = turtle.Pen()
zolw.speed(5)

zolw.left(90)
zolw.forward(90)
zolw.right(90)
zolw.forward(50)
zolw.right(90)
zolw.forward(90)
zolw.right(90)
zolw.forward(325)
zolw.right(90)
zolw.forward(200)
zolw.right(90)
zolw.forward(600)
zolw.right(90)
zolw.forward(200)
zolw.right(90)
zolw.forward(275)
zolw.right(180)
zolw.forward(275)
zolw.left(90)
zolw.forward(200)
zolw.left(45)
zolw.forward(bok_dachu)
zolw.left(90)
zolw.forward(bok_dachu)

turtle.done()
