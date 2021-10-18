import pygame as py
import random
from pygame import time as pytime
from  screen.Cursor import Cursor
from screen.Button import Button

def questions():
    question1 = ["¿Cuántos litros de sangre tiene una persona adulta?", "A: Tiene entre 2 y 4 litros", "B: Tiene entre 4 y 6 litros", "C: Tiene 10 litros", "D: Tiene 7 litros", 2]
    question2 = ["¿Quién es el autor de la frase *Pienso, luego existo*?", "A: Platón", "B: Galileo Galilei", "C: Descartes", "D: Sócrates",
                 3]
    question3 = ["¿Cuál es el país más grande y el más pequeño del mundo?", "A: Rusia y Vaticano", "B: China y Nauru",
                 "C: Canadá y Mónaco", "D: Estados Unidos y Malta", 1]
    question4 = ["Cual es el simbolo quimico del aluminio", "A: Ao", "B: Am", "C: Lm", "D: Al", 4]
    question5 = ["¿Cuál es el grupo de palabras escritas correctamente?", "A: Metamorfosis, extranjero, diversidac, equilivrio", "B: Metaformosis, estranjero, diversidad, ekilibrio", "C: Metamorfosis, extrangero, dibersidad, equilibrio",
                 "D: Metamorfosis, extranjero, diversidad, equilibrio", 4]
    question6 = ["¿Cuál es el libro más vendido en el mundo después de la Biblia?", "A: El Señor de los Anillos", "B: Don Quijote de la Mancha", "C: El Principito",
                 "D: Cien años de Soledad", 2]
    question7 = ["La sal común está formada por dos elementos, ¿cuáles son?", "A: Sodio y potasio", "B: Sodio y cloro", "C: Sodio y carbono", "D: Potasio y cloro", 2]
    question8 = ["¿Quién pintó la obra *Guernica*?", "A: Paul Cézanne", "B: Pablo Picasso", "C: Diego Rivera", "D: Salvador Dalí", 2]
    question9 = ["¿Cuánto tiempo tarda la luz del Sol en llegar a la Tierra?", "A: 12 minutos", "B: 1 día", "C: 12 horas", "D: 8 minutos", 4]
    question10 = ["¿En qué orden se presentaron los modelos atómicos?", "A: Thomson, Dalton, Rutherford, Bohr",
                  "B: Dalton, Thomson, Rutherford, cuántico", "C: Bohr, Rutherford, cuántico, Einstein", "D: Dalton, Einstein, cuántico, Sheldon Cooper", 2]
    question11 = ["El protagonita de este espectaculo tiene un abuelo llamado Lou", "A: Los padrinos magicos",
                  "B: Doug", "C: Rugrats", "D: Clarissa lo explica todo", 3]
    question12 = ["Cual es el continente mas grande del mundo", "A: Asia", "B: Europa", "C: Africa", "D: America", 1]
    question13 = ["¿En qué periodo de la prehistoria fue descubierto el fuego?", "A: Neolítico", "B: Paleolítico",
                  "C: Edad de los metales", "D: Edad de piedra", 2]
    question14 = ["Cual es el oceano en el que llega el caudal del rio amazonas", "A: El Artico", "B: El indio",
                  "C: El Atlantico", "D: El Pacifico", 3]
    question15 = ["¿Cuál es la montaña más alta del continente americano?", "A: Monte Everest",
                  "B: Aconcagua", "C: Pico Neblina", "D: Pico Bolívar", 2]
    question16 = ["Cuantos jugadores conforman un equipo de voleibol en la cancha", "A: 10", "B: 5", "C: 6", "D: 4", 3]
    question17 = ["En matematicas, diez milimetros son...", "A: Un poquito", "B: Un metro", "C: Un decimetro",
                  "D: Un centimetro", 4]
    question18 = ["Cuantos segundos tiene un minuto y medio", "A: 45", "B: 90", "C: 60", "D: 75", 2]
    question19 = ["Los delfines son animales de sangre...", "A: Caliente", "B: Fria", "C: Azul", "D: Gris", 1]
    list = [question1, question2, question3, question4, question5, question6, question7, question8, question9,
             question10, question11, question12, question13, question14, question15, question16, question17, question18,
             question19]
    return list


def point():
    list = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
    return list


def play(screen, cursor1):
    reloj1 = py.time.Clock()
    watch = 20
    score2 = 0
    cont1 = 0
    score = ""
    po = point()
    background = py.image.load("images/background.png")
    parche = py.image.load("images/hide.gif")
    screen.blit(background, (0, 0))
    font2 = py.font.SysFont("Comic Sans MS", 16, True, False)
    white = (255, 255, 255)
    valueOne = py.image.load("images/remarked.gif")
    valueTwo = py.image.load("images/remarkedBlack.gif")
    list = questions()
    temp = 19
    font1 = py.font.SysFont("Comic Sans MS", 34, True, False)
    jboton1 = Button(valueOne, valueTwo, 46, 421)
    jboton2 = Button(valueOne, valueTwo, 422, 421)
    jboton3 = Button(valueOne, valueTwo, 46, 496)
    jboton4 = Button(valueOne, valueTwo, 424, 496)
    reloj1.tick(20)
    exit = False

    while exit != True:

        for event in py.event.get():
            if event.type == py.QUIT:
                exit = True
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    exit = True
        if temp == 1:
            exit = True

        ran = random.choice(range(temp))
        temp = temp - 1
        ques = list.pop(ran)
        cursor1.update()
        screen.blit(background, (0, 0))
        screen.blit(parche, (115, 280))
        Atext = font2.render(ques[0], 1, white)
        Atext1 = font2.render(ques[1], 1, white)
        Atext2 = font2.render(ques[2], 1, white)
        Atext3 = font2.render(ques[3], 1, white)
        Atext4 = font2.render(ques[4], 1, white)
        score = "Score: " + str(score2)
        score_cont = font1.render(score, 1, white)
        screen.blit(score_cont, (400, 40))
        screen.blit(Atext, (80, 300))
        jboton1.update(screen, cursor1, Atext1, 65, 430, "1")
        jboton2.update(screen, cursor1, Atext2, 450, 430, "1")
        jboton3.update(screen, cursor1, Atext3, 65, 508, "1")
        jboton4.update(screen, cursor1, Atext4, 450, 508, "1")
        py.display.update()
        exit2 = False
        resp = False
        py.time.set_timer(1, 0)

        while exit2 != True:
            for event2 in py.event.get():
                if event2.type == py.QUIT:
                    exit2 = True
                    py.mixer.stop()
                if event2.type == py.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(jboton1.rect):
                        exit2 = True
                        py.mixer.stop()
                        if ques[5] == 1:
                            resp = True
                            pytime.wait(1000)
                        else:
                            resp = False
                    if cursor1.colliderect(jboton2.rect):
                        exit2 = True
                        py.mixer.stop()
                        if ques[5] == 2:
                            resp = True
                            pytime.wait(1000)
                        else:
                            resp = False
                    if cursor1.colliderect(jboton3.rect):
                        exit2 = True
                        py.mixer.stop()
                        if ques[5] == 3:
                            resp = True
                            pytime.wait(1000)
                        else:
                            resp = False
                    if cursor1.colliderect(jboton4.rect):
                        exit2 = True
                        py.mixer.stop()
                        if ques[5] == 4:
                            resp = True
                            pytime.wait(1000)
                        else:
                            resp = False

            cursor1.update()
            screen.blit(background, (0, 0))
            screen.blit(score_cont, (530, 40))
            screen.blit(Atext, (80, 300))
            jboton1.update(screen, cursor1, Atext1, 65, 430, "1")
            jboton2.update(screen, cursor1, Atext2, 450, 430, "1")
            jboton3.update(screen, cursor1, Atext3, 65, 508, "1")
            jboton4.update(screen, cursor1, Atext4, 450, 508, "1")
            watch = (py.time.get_ticks() / 1000)
            watch = str(watch)
            count = font1.render("Time: " + watch, 1, white)
            screen.blit(count, (40, 40))
            py.display.update()
        if resp == True:
            cont1 = cont1 + 1
            score2 = po[cont1]
        else:
            exit = True


py.init()
pytime.wait(500)
val = "0"
screen = py.display.set_mode((833, 559))
py.display.set_caption("Quien quiere ser millonario")
background = py.image.load("images/background.png")
value1 = py.image.load("images/remarked.gif")
value2 = py.image.load("images/remarkedBlack.gif")
button1 = Button(value1, value2, 28, 250)
button2 = Button(value1, value2, 444, 250)
cursor1 = Cursor()
font1 = py.font.SysFont("Comic Sans MS", 34, True, False)
white = (255, 255, 255)
text1 = font1.render("         Play", 1, white)
text2 = font1.render("         Exit", 1, white)
exit = False

while exit != True:

    screen.blit(background, (0, 0))
    cursor1.update()
    button1.update(screen, cursor1, text1, 28, 252, "1")
    button2.update(screen, cursor1, text2, 444, 252, "3")
    py.display.update()

    for event in py.event.get():

        if event.type == py.QUIT:
            exit = True
            py.mixer.stop()
        if event.type == py.MOUSEBUTTONDOWN:
            if cursor1.colliderect(button2.rect):
                py.mixer.stop()
                py.quit()
        if event.type == py.MOUSEBUTTONDOWN:
            if cursor1.colliderect(button1.rect):
                py.mixer.stop()
                play(screen, cursor1)
    if val == "0":
        val = "1"
py.quit()
