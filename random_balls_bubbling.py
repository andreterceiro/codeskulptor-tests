import simplegui
import random

colors = ["Aqua", "Black", "Blue", "Fuchsia", "Gray", "Green", "Lime", "Maroon", "Navy", "Olive", "Orange", "Purple", "Red", "Silver", "Teal", "White", "Yellow"]

def draw(canvas):
    canvas.draw_circle([random.randint(0, 800), random.randint(0, 800)] , 5, 10, colors[random.randint(0, 16)])
    
frame = simplegui.create_frame("Home", 800, 600)
frame.set_draw_handler(draw)

frame.start()
