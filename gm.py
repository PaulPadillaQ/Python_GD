import turtle
import winsound

wn= turtle.Screen()
wn.title("PPQ game")
wn.bgcolor("gray")
wn.tracer(0)
wn.setup(width=800, height=600)

#p1
uno=turtle.Turtle()
uno.speed(0)
uno.shape("square")
uno.color("white")
uno.shapesize(stretch_wid=5, stretch_len=1)
uno.penup()
uno.goto(-350,0)

#p2
dos=turtle.Turtle()
dos.speed(0)
dos.shape("square")
dos.color("white")
dos.shapesize(stretch_wid=5, stretch_len=1)
dos.penup()
dos.goto(350,0)

#pelota
bola=turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0,0)
bola.dx=0.2
bola.dy=0.2

#puntake
puntosa=0
puntosb=0

#contador
lapiz=turtle.Turtle()
lapiz.speed(0)
lapiz.color("white")
lapiz.penup()
lapiz.hideturtle()
lapiz.goto(0,260)
lapiz.write("Lado A: 0 Lado B: 0", align="center", font=("Courier", 24, "normal"))

#funciones
def unoUp():
    y =uno.ycor()
    y+=20
    uno.sety(y)
def unoDown():
    y =uno.ycor()
    y+=-20
    uno.sety(y)
def dosUp():
    y =dos.ycor()
    y+=20
    dos.sety(y)
def dosDown():
    y =dos.ycor()
    y+=-20
    dos.sety(y)
    
# Keys
wn.listen()
wn.onkeypress(unoUp, "w")
wn.onkeypress(unoDown, "s")
wn.onkeypress(dosUp, "Up")
wn.onkeypress(dosDown, "Down")

#loop

while True:
    wn.update()
    #mueve bolas
    bola.setx(bola.xcor()+bola.dx)
    bola.sety(bola.ycor()+bola.dy)

    #bordes
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx*=-1
        puntosa+=1
        lapiz.clear()
        lapiz.write("Lado A: {} Lado B: {}".format(puntosa,puntosb), align="center", font=("Courier", 24, "normal"))

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx*=-1
        puntosb+=1
        lapiz.clear()
        lapiz.write("Lado A: {} Lado B: {}".format(puntosa,puntosb), align="center", font=("Courier", 24, "normal"))

    #jugcolisiones
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < dos.ycor() + 50 and bola.ycor() > dos.ycor() -50):
        bola.setx(340)
        bola.dx*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < uno.ycor() + 50 and bola.ycor() > uno.ycor() -50):
        bola.setx(-340)
        bola.dx*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    #ScoreUpdates
    if(bola.xcor() > 390):
        lapiz.write()
