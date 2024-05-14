"""Python program that uses recursion to create the "Pythagorean Tree" fractal."""

import turtle
import math


def draw_pythagorean_tree(t, length, depth):
    """
    Draws a Pythagorean tree with given length and depth.

    Args:
        t: The turtle object to use for drawing.
        length: The length of the current branch.
        depth: The remaining depth of the recursion.
    """
    if depth == 0:
        return
    t.forward(length)
    t.left(45)
    draw_pythagorean_tree(t, length * (1 / math.sqrt(2)), depth - 1)
    t.right(90)
    draw_pythagorean_tree(t, length * (1 / math.sqrt(2)), depth - 1)
    t.left(45)
    t.backward(length)


def main():
    """
    Gets user input for recursion level, sets up the turtle,
    and calls the drawing function.
    """
    while True:
        try:
            depth = int(input("Enter desired recursion level (positive integer): "))
            if depth <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    t = turtle.Turtle()
    t.speed(10)  # Set turtle speed to fastest
    t.left(90)
    t.penup()
    t.goto(0, -100)
    t.pendown()
    draw_pythagorean_tree(t, 150, depth)  # You can adjust initial length here
    window = turtle.Screen()
    window.exitonclick()


if __name__ == "__main__":
    main()
