"""Tres en raya

Ejercicios

1. Dale a la X y a la O un color y un grosor diferentes.
2. ¿Qué pasa cuando alguien toca una casilla ya ocupada?
3. ¿Cómo detectarías cuando alguien ha ganado?
4. ¿Cómo podrías crear un jugador controlado por la computadora?
"""

import turtle

from freegames import line


def grid():
    """Dibuja la cuadrícula del tres en raya."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja la X."""
    turtle.color("blue")  # usa color() para definir el color de la X
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Dibuja la O."""
    turtle.color("red")  # usa color() para definir el color de la O
    turtle.up()
    turtle.goto(x + 67, y + 5)
    turtle.down()
    turtle.circle(62)


def floor(value):
    """Redondea hacia abajo a la cuadrícula (paso 133)."""
    return ((value + 200) // 133) * 133 - 200


state = {"player": 0}
players = [drawx, drawo]

# state['ocupado']: casillas redondeadas ya visitadas.
state["ocupado"] = set()


def tap(x, y):
    """Dibuja la X o la O en la casilla tocada."""
    x = floor(x)
    y = floor(y)

    if (x, y) in state["ocupado"]:
        return

    player = state["player"]
    players[player](x, y)

    state["ocupado"].add((x, y))

    turtle.update()
    state["player"] = not player


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)

grid()
turtle.update()
turtle.onscreenclick(tap)
turtle.done()
