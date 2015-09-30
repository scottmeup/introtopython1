#http://www.codeskulptor.org/#user40_pM2byAIPwV_42.py
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
width = 600
height = 400       
ball_radius = 20
pad_width = 8
pad_height = 80
half_pad_width = pad_width / 2
half_pad_height = pad_height / 2
left = False
right = True
ball_pos = [width/2, height/2]
ball_vel = [0, 0]
score1 = 0
score2 = 0
left_pad_pos = 0
right_pad_pos = 0
left_pad_vel = 0
right_pad_vel = 0
pad_velocity = 4

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [width/2, height/2]
    #Vertical spawn speed, negative for up positive for down
    ball_vel[1] = random.randrange(-4, -1)
    #ball_vel[1] = random.randrange(1, 4)
    #Horizontal spawn speed
    #sigh... horrible variable names here. true is probably right.
    if direction:
        ball_vel[0] = random.randrange(2, 5)
    else:
        ball_vel[0] = random.randrange(-5, -2)


# define event handlers
def new_game():
    global left_pad_pos, right_pad_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    left_pad_pos = (height - pad_height) / 2
    right_pad_pos = (height - pad_height) / 2
    spawn_ball(right)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, left_pad_pos, right_pad_pos, left_pad_vel, right_pad_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([width / 2, 0],[width / 2, height], 1, "White")
    canvas.draw_line([pad_width, 0],[pad_width, height], 1, "White")
    canvas.draw_line([width - pad_width, 0],[width - pad_width, height], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if (ball_pos[1]-ball_radius <= 0) or (ball_pos[1]+ball_radius >= height):
        ball_vel[1] *= -1
            
    # draw ball
    canvas.draw_circle((ball_pos[0], ball_pos[1]), ball_radius, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    # pos is top of paddle, check if next move will take it offscreen
    if (left_pad_pos + left_pad_vel >= 0) and (left_pad_pos + pad_height + left_pad_vel <= height):
        left_pad_pos += left_pad_vel
        #print left_pad_pos, left_pad_vel
    else:
        #print left_pad_pos, left_pad_vel
        pass
    if (right_pad_pos + right_pad_vel >= 0) and (right_pad_pos + pad_height + right_pad_vel <= height):
        right_pad_pos += right_pad_vel
        #print right_pad_pos, right_pad_vel
    else:
        #print right_pad_pos, right_pad_vel
        pass
    
    # draw paddles
    canvas.draw_line((0+half_pad_width, left_pad_pos), (0+half_pad_width, left_pad_pos + pad_height), pad_width, "Green" )
    canvas.draw_line((width-half_pad_width, right_pad_pos), (width-half_pad_width, right_pad_pos + pad_height), pad_width, "Red" )
    
    # determine whether paddle and ball collide
    #impact left side
    if ball_pos[0] <= 0 + pad_width + ball_radius:
        #hit paddle
        if (ball_pos[1] > left_pad_pos) and (ball_pos[1] < left_pad_pos + pad_height):
            ball_vel[0] *= -1.1
        else:
            #miss left paddle
            score2 += 1
            spawn_ball(right)
            print "Score ", score1, ":", score2
    #impact right side
    if ball_pos[0] >= width - pad_width - ball_radius:
        if (ball_pos[1] > right_pad_pos) and (ball_pos[1] < right_pad_pos + pad_height):
            ball_vel[0] *= -1.1
        else:
            #miss right paddle
            score1 += 1
            spawn_ball(left)
            print "Score ", score1, ":", score2
    
    # draw scores
    score_height = 48
    canvas.draw_text(str(score1) + " : "  + str(score2), ((width/2 - score_height), score_height + 10), score_height, "White")
    
def keydown(key):
    global left_pad_vel, right_pad_vel
    if key == simplegui.KEY_MAP["up"]:
        right_pad_vel = -pad_velocity
    if key == simplegui.KEY_MAP["down"]:
        right_pad_vel = pad_velocity
    if key == simplegui.KEY_MAP["w"]:
        left_pad_vel = -pad_velocity
    if key == simplegui.KEY_MAP["s"]:
        left_pad_vel = pad_velocity
   
def keyup(key):
    global left_pad_vel, right_pad_vel
    if key == simplegui.KEY_MAP["up"]:
        right_pad_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        right_pad_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        left_pad_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        left_pad_vel = 0
        
def reset():
    new_game()


# create frame
frame = simplegui.create_frame("Pong", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", reset, 100)


# start frame
new_game()
frame.start()
