import turtle
import time
import random


posponer = 0.1

#marcador

score = 0
high_score = 0



#ventana

wn = turtle.Screen()
wn.title("snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#cabeza

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = 'stop'
cabeza.color('blue')


#cuerpo

segmentos = []

#texto

texto = turtle.Turtle()
texto.speed(0)
texto.color("purple")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0      High score: 0", align = "center", font = ("courier", 24, "normal"))



#comida

comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.penup()
comida.goto(0,100)
comida.color('red')

#fuciones

def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def derecha():
    cabeza.direction = "right"

def izquierda():
    cabeza.direction = "left"



def mov():

    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

#controles

wn.listen()
wn.onkeypress( arriba, "Up")
wn.onkeypress( abajo, "Down")
wn.onkeypress( derecha, "Right")
wn.onkeypress( izquierda, "Left")


while True:

    wn.update()

    #colicion bordes

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto (0,0)
        cabeza.direction = "stop"

        # Borrar los segmentos.

        for segmento in segmentos:
            segmento.hideturtle()
        segmentos.remove(nuevo_segmento)

        #Limpiar lista de segmentos
        segmentos.clear()

        #resetear marcador

        score = 0
        texto.clear()
        texto.write("Score: {}      High_score: {}".format(score, high_score), align = "center", font = ("courier", 24, "normal"))

    #colicion comida

    if cabeza.distance(comida) <20:

        #pocicion random

        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        #nuevo segmento

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.penup()
        nuevo_segmento.goto(0,0)
        nuevo_segmento.direction = 'stop'
        nuevo_segmento.color('cyan')
        segmentos.append(nuevo_segmento)



        #Aumentar marcador
        score += 10

        if score > high_score:
            high_score = score
           
            #colores
            if score >= 0:
                texto.color("purple")

            if score >= 50:
                texto.color("red")

            if score >= 100:
                texto.color("brown")

            if score >= 200:
                texto.color("gray")

            if score >= 300:
                texto.color("yellow")



        texto.clear()
        texto.write("Score: {}      High_score: {}".format(score, high_score), align = "center", font = ("courier", 24, "normal"))



    #movimiento del cuerpo
    
    totalSeg = len(segmentos)

    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)



    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)



    mov()



    #colision cuerpo



    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:

            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"



            #borrar segmentos

            for segmento in segmentos:
                segmento.hideturtle()
            segmentos.remove(nuevo_segmento)

            #limpiar segmentos
            segmentos.clear()


            #resetear marcador

            score = 0
            texto.clear()
            texto.write("Score: {}      High_score: {}".format(score, high_score), align = "center", font = ("courier", 24, "normal"))


    time.sleep(posponer)