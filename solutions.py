import math
import turtle
PI = math.pi

#a
t = int(input("What is the number that you want the absolute value of it? "))
if t>=0:
    print("Absolute =",t)
else:
    print("Absolute =",-1*t)


#b
num1 = int(input("number 1: "))
num2 = int(input("number 2: "))
num3 = int(input("number 3: "))

minimum = num1

if num2<num1 and num2<num3:
    minimum = num2
if num3<num1 and num3<num2:
    minimum = num3



print("Minimum of all three is",minimum)

#c
num_of_lectures = int(input("How many lecture did you take? "))
gpa = int(input("What is your gpa? "))

if gpa>= 2.0:
    if num_of_lectures>=47:
        print("GRADUATED!!!")
    else:
        print("Not enough number of lectures.")
else:
    if num_of_lectures >= 47:
        print("Not enough GPA.")
    else:
        print("Not enough GPA or number of lectures.")

#d
age = int(input("What is you age? "))
if(age<6 or age>60):
    print("Your ticket is free ")
elif(6<=age<=18):
    print("Your ticket is %50 discounted which is 1,5 TL")
else:
    print("Your ticket is 3 TL")

#e
print("Give the a,b,c of ax2+bx+c = 0 equality")
a = int(input("What is a? "))
b = int(input("What is b? "))
c = int(input("What is c? "))

delta = b**2 - 4*a*c

if delta > 0 :
    root1 = (-b-math.sqrt(delta))/2*a
    root2 = (-b+math.sqrt(delta))/2*a
    print("There are 2 real roots which is:",root1,"and",root2)
elif  delta == 0 :
    root = (-b-math.sqrt(delta))/2*a
    print("There are 1 real root which is:",root)
else:
    print("There are not eny real roots.")

#f
size = int(input("What is the size?"))
radius = math.sqrt(size/PI)
side = math.sqrt(size)

if size <= 40 :
    turtle.circle(radius)
else :
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)