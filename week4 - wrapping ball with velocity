# control the position of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
velocity = [0,0]

# define event handlers
def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    if ball_pos[0] == 0:
        ball_pos[0] += velocity[0]
        print "Width=0"
    else:
        ball_pos[0] = (ball_pos[0] + velocity[0]) % WIDTH
    if ball_pos[1] == 0:
        print "Height=0"
        ball_pos[1] += velocity[1]
    else:
        ball_pos[1] = (ball_pos[1] + velocity[1]) % HEIGHT
    
def keydown(key):
    if key == simplegui.KEY_MAP["left"]:
        velocity[0] -= 1
    elif key == simplegui.KEY_MAP["right"]:
        velocity[0] += 1
    elif key == simplegui.KEY_MAP["down"]:
        velocity[1] += 1
    elif key == simplegui.KEY_MAP["up"]:
        velocity[1] -= 1
    print velocity
    
# create frame 
frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
