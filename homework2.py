import turtle



def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60 ,0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=700):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    koch_curve(t, order, size)
    window.mainloop()


user_input = input("Як багато рівнів: ")
order = int(user_input)
draw_koch_curve(order)