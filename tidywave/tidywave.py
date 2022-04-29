"""
Inspired by:
https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6
"""
import functools
import math
import random
import turtle

import svg_turtle

MAX_DEPTH = 70
SCALE_FACTOR = 1
DEVIATION_FACTOR = 36

# R1 = r = (1/golden_ratio)**(1/golden_ratio)
# r2 = r1**2
# angle1 = math.acos((1+r**2-r**4)/(2*r))
# angle2 = math.acos((1+r**4-r**2)/(2*r**2))


def _gen_fib(below=0):
    prev = 1
    yield prev
    current = 1
    yield current
    while not below or current < below:
        current, prev = prev + current, current
        yield current


FIBS_BELOW_70 = set(i for i in _gen_fib(below=70))


def _is_fib(num):
    return num in FIBS_BELOW_70


def translate(
    start_pos: tuple[float, float],
    translation: tuple[float, float],
) -> tuple[float, float]:
    return (start_pos[0] + translation[0], start_pos[1] + translation[1])


# def operate(
# fractal: turtle.Turtle | svg_turtle.SvgTurtle,
# start_pos: tuple[float, float],
# distance: float,
# depth: float,
# ):
# pass


def dot_at(
    fractal: turtle.Turtle | svg_turtle.SvgTurtle,
    pos: tuple[float, float],
    size: float | None,
):
    current = fractal.pos()
    fractal.penup()
    fractal.goto(pos)
    fractal.pendown()
    fractal.dot(size)
    fractal.penup()
    fractal.goto(current)
    fractal.pendown()


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return f"#{hex(rgb[0])[2:].zfill(2)}{hex(rgb[1])[2:].zfill(2)}{hex(rgb[2])[2:].zfill(2)}"


def build_fractal(
    fractal: turtle.Turtle | svg_turtle.SvgTurtle,
    start_pos: tuple[float, float],
    depth: int = 0,
):
    if depth <= MAX_DEPTH:
        radius = SCALE_FACTOR * (
            1
            + math.log(
                functools.reduce(
                    lambda i, prod: i * prod, (math.sqrt(i) for i in range(1, depth)), 1
                )
            )
        )
        fractal.pencolor(
            rgb_to_hex(
                (
                    round(205 * ((MAX_DEPTH - depth) / MAX_DEPTH)),
                    round(205 * ((MAX_DEPTH - depth) / MAX_DEPTH)),
                    round(255),
                )
            )
        )
        fractal.pensize(round(depth / 10) + 1)
        fractal.penup()
        fractal.goto(translate(start_pos, (0, -radius)))
        fractal.pendown()
        turtle.fillcolor(rgb_to_hex((0, 255, 255)))
        turtle.begin_fill()
        fractal.circle(radius)
        turtle.end_fill()
        next_pos = translate(
            start_pos,
            (
                radius * random.choice((-1, 1)) / DEVIATION_FACTOR,
                radius * random.choice((-1, 1)) / DEVIATION_FACTOR,
            ),
        )
        build_fractal(
            fractal=fractal,
            start_pos=next_pos,
            depth=depth + 1,
        )


def main(is_svg: bool):
    turtle.hideturtle()
    turtle.screensize(100, 100)
    fractal = svg_turtle.SvgTurtle() if is_svg else turtle.Turtle()
    fractal.fillcolor(rgb_to_hex((255, 255, 204)))
    fractal.hideturtle()

    build_fractal(fractal, (0, 0))
    if is_svg:
        fractal.save_as("output.svg")
        print("Saved file as output.svg")
    else:
        turtle.mainloop()


if __name__ == "__main__":
    main(is_svg=True)
