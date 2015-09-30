#http://www.codeskulptor.org/#user40_pvAn6U8qWt_21.py
import math

#question 1
"An if statement can have at most how many else parts?"
print "\nQuestion 1"
print "one else"

#question 2
print "\nQuestion 2"
def question_2(p, q):
    print(not (p or not q))
    return None

question_2(True, True)
question_2(True, False)
question_2(False, True)
question_2(False, False)

#question 3
print "\nQuestion 3"
def do_stuff():
    print "Hello world"
    return "Is it over yet?"
    print "Goodbye cruel world!"
    
print do_stuff()

#question 4
print "\nQuestion 4"
def tens_value(n):
    print(n % 10) / 10
    print((n - n % 10) / 10) % 10
    print(n // 10) % 10
    return None

tens_value(123)

#question 5:
print "\nQuestion 5"
print "Answer = 10. randint(min, max) can show any value from min to max inclusive randrange(min, max) shows numbers equal or greater than min, less than max "

#Question 6: code a function for f(x) = -5 x^5 + 69 x^2 - 47 and find maximum value from where x = 0 1, 2, 3
print "\nQuestion 6"
def question_6(x):
    return (-5*x**5) + (69*x**2) - 47

for x in range(0,4):
    print question_6(x)
    
#question 7
print "\nQuestion 7"
def question_7(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    total = present_value*(1+rate_per_period)**periods
    return total

print "$1000 at 2% compounded daily for 3 years yields $", question_7(1000, .02, 365, 3)
print question_7(500, .04, 10, 10), "Should == 745.317442824 if math is correct"

#question 8
#make a function that finds ¼ n s^2 / tan(π/n).
print "\nQuestion 8"
def question_8(n, s):
    return (1.00 / 4.00 * n * (s**2)) / (math.tan(math.pi / n))

print question_8(5, 7), " should be 84.3033926289"
print "Q8 Answer is: ", question_8(7, 3)

#question 9
print "\nQuestion 9"
print "Incorrect Indentation"
def question_8(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
#original line
#return question_8(a, question_8(b, c))
    #fixed line, indented
    return question_8(a, question_8(b, c))

#question 10
print "\nQuestion 10"
def question_10(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
question_10(2, 7, 4)