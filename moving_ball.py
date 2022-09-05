# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, Safari, and Edge.

import simplegui

position = [150,100]
velocity = 5

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_circle(position, 20, 40, 'Green')

def keydown(key):
    if key == simplegui.KEY_MAP['down']:
        position[1] = position[1] + velocity
    elif key == simplegui.KEY_MAP['up']:
        position[1] = position[1] - velocity
    elif key == simplegui.KEY_MAP['right']:
        position[0] = position[0] + velocity
    elif key == simplegui.KEY_MAP['left']:
        position[0] = position[0] - velocity
    
frame = simplegui.create_frame("Home", 300, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# Start the frame animation
frame.start()
