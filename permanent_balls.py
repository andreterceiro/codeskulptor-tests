import simplegui
import random

colors = ["Aqua", "Black", "Blue", "Fuchsia", "Gray", "Green", "Lime", "Maroon", "Navy", "Olive", "Orange", "Purple", "Red", "Silver", "Teal", "White", "Yellow"]
bubling
balls = []

def draw(canvas):
    ball = [random.randint(0, 800), random.randint(0, 600), colors[random.randint(0, 16)]]
    balls.append(ball)

    for item in balls:
        canvas.draw_circle([item[0], item[1]], 5, 10, item[2])

frame = simplegui.create_frame("Home", 800, 600)
frame.set_draw_handler(draw)

frame.start()
