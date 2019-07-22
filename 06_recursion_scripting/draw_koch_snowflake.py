"Example Python script to draw Koch snowflake" 

from turtle import *

def koch(size=300, order=3):
    "Draw a Koch section"
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(size/3, order-1)
            left(t)
    else:
        forward(size)

def n_koch_curves(n):
    "Draw n Koch curves"
    for _ in range(n):
        koch()
        right(120)

def main():
    "Primary logic"
    pensize(3)
    n_koch_curves(n=3)
    exitonclick()

if __name__ == '__main__':  # Code to execute if called from command-line. If imported, don't run
    main()    