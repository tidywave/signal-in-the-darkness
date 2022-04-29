"""
Inspired by:
https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6
"""
import math
import turtle

import svg_turtle

MAX_DEPTH = 2


def translate(
    start_pos: tuple[float, float],
    translation: tuple[float, float],
) -> tuple[float, float]:
    return (start_pos[0] + translation[0], start_pos[1] + translation[1])


def draw_line(
    fractal: turtle.Turtle | svg_turtle.SvgTurtle,
    pos1: tuple[float, float],
    pos2: tuple[float, float],
    depth: float,
):
    fractal.penup()
    fractal.goto(*pos1)
    fractal.pendown()
    fractal.goto(*pos2)


def operate(
    fractal: turtle.Turtle | svg_turtle.SvgTurtle,
    start_pos: tuple[float, float],
    current: tuple[float, float],
    towards: tuple[float, float],
    new_short_leg: float,
    depth: float,
):
    build_fractal(
        fractal,
        translate((current[0] / 2, current[1] / 2), start_pos),
        short_leg=new_short_leg,
        depth=depth + 1,
    )
    draw_line(
        fractal,
        translate(start_pos, current),
        translate(start_pos, towards),
        depth,
    )


def build_fractal(
    fractal: turtle.Turtle | svg_turtle.SvgTurtle,
    start_pos: tuple[float, float],
    short_leg: float,
    depth: int = 0,
):
    golden_ratio = (1 + 5 ** 0.5) / 2
    new_start_pos = golden_ratio * start_pos[0], (golden_ratio * start_pos[0]) ** 2
    if depth <= MAX_DEPTH:
        fractal.color((0, 0, 255 - round(255 / MAX_DEPTH * depth)))
        fractal.dot(10 / MAX_DEPTH * depth)
        new_short_leg = short_leg / 2
        operate(
            fractal,
            new_start_pos,
            (0, 0),
            (short_leg * math.sqrt(3), short_leg),
            new_short_leg,
            depth,
        )
        operate(
            fractal,
            new_start_pos,
            (short_leg * math.sqrt(3), short_leg),
            (2 * short_leg * math.sqrt(3), 0),
            new_short_leg,
            depth,
        )
        operate(
            fractal,
            new_start_pos,
            (2 * short_leg * math.sqrt(3), 0),
            (short_leg * math.sqrt(3), -short_leg),
            new_short_leg,
            depth,
        )
        operate(
            fractal,
            new_start_pos,
            (short_leg * math.sqrt(3), -short_leg),
            (0, 0),
            new_short_leg,
            depth,
        )


def main(is_svg: bool):
    turtle.colormode(255)
    fractal = svg_turtle.SvgTurtle() if is_svg else turtle.Turtle()
    fractal.hideturtle()
    # fractal.setheading(90)

    build_fractal(fractal, (0, 0), 50)
    turtle.mainloop()


if __name__ == "__main__":
    main(is_svg=False)
