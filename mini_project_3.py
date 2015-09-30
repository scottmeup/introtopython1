# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
guesses_total = 0
guesses_correct = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(number):
    minutes = str(0)
    tens_seconds = str(0)
    seconds = str(0)
    #print number
    tenths_seconds = str(number)[-1]
    if (number % 600) > 9:
        seconds = str(number % 600)[-2]
        #print "Case 1 " + seconds + "." + tenths_seconds
    if (number % 600) > 99:
        tens_seconds = str(number % 600)[-3]
        #print "Case 2 " + tens_seconds + seconds + "." + tenths_seconds
    if (number / 600) >= 1:
        minutes = str(number/600)
        #print "Case 3 " + minutes + ":" + tens_seconds + seconds + "." + tenths_seconds
    return str(minutes) + ":" + str(tens_seconds) + str(seconds) + "." + str(tenths_seconds)


    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    watch_timer.start()
    pass

def stop():
    global guesses_total
    global guesses_correct
    watch_timer.stop()
    guesses_total += 1
    if (time % 10) == 0:
        guesses_correct += 1
    pass

def reset():
    global time
    global guesses_total
    global guesses_correct
    time = 0
    guesses_total = 0
    guesses_correct = 0
    pass

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1
    pass

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), [200, 100], 48, "Red")
    canvas.draw_text(str(guesses_correct) + "/" + str(guesses_total), [350, 50], 24, "White")

    
# create frame
f = simplegui.create_frame("Guess", 400, 200)
f.add_button("Start", start, 100)
f.add_button("Stop", stop, 100)
f.add_button("Reset", reset, 100)

# register event handlers


# start frame
f.start()
watch_timer = simplegui.create_timer(100, timer_handler)
f.set_draw_handler(draw_handler)

# Please remember to review the grading rubric
