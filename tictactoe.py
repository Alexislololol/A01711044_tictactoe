"""Tres en raya

Ejercicios

1. Dale a la X y a la O un color y un grosor diferentes.
2. ¿Qué pasa cuando alguien toca una casilla ya ocupada?
3. ¿Cómo detectarías cuando alguien ha ganado?
4. ¿Cómo podrías crear un jugador controlado por la computadora?
"""

from turtle import *

from freegames import line


def grid():
    """Dibuja la cuadrícula del tres en raya."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja la X."""
    color("blue") #usa la función color() para definir el color de las X a azul
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Dibuja la O."""
    color("red") #usa la función color() para definir el color de las O a rojo
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    """Redondea el valor hacia abajo a la cuadrícula con un tamaño de cuadrado de 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]

# state['ocupado'] guarda las casillas ya visitadas (coordenadas redondeadas) para dibujar dos piezas en la misma posición y no alternamos el turno cuando se hace click ahí
state['ocupado'] = set()



def tap(x, y):
    """Dibuja la X o la O en la casilla tocada.
    """
    x = floor(x)
    y = floor(y)

    if (x, y) in state['ocupado']:
        return

    player = state['player']
    draw = players[player]
    draw(x, y)

    state['ocupado'].add((x, y))

    update()
    state['player'] = not player



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
