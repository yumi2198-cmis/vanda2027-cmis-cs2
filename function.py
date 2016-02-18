def add(a,b):
	return a+b

def sub (x,y):
	return x-y

def mul(e,f):
	return e*f

def div (j,k):
	return (j/k)

def hours_from_seconds (a):
    return a / 3600

import math
def circle_area (a):
    return math.pi * (a**2)

def sphere_volume (a):
    return 1.33333333333 * 3.14159265359 * (a**3)

def avg_volume (a, b):
   
    return ((1.0/6 * math.pi * a**3) + (1.0/6 * math.pi * b**3)) /2

def area (a,b,c):
    return math.sqrt(2.75*(2.75-a)*(2.75-b)*(2.75-c))

def right_align (word):
    return (80-len(word))*(" ") + word

def center (word):
    return (40-len(word))*(" ")+word

def msg_box (word):
    return "+" + ((len(word)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (word)+ (2*" ") + "|" + "\n" + "+" + ((len(word)+4)*"-") + "+"

c1= add (3,4)
print c1 
c2= add (5,6)
print c2 
z1= sub (5,3)
print z1
z2= sub (4,8)
print z2
g1= mul (4,4)
print g1
g2= mul (9,4)
print g2
L1= div (2.0,3)
print L1
L2= div (1.0,3)
print L2
I1= hours_from_seconds (86400)
print I1
I2= hours_from_seconds (56900)
print I2
a1= circle_area (5)
print a1
a2= circle_area (9)
print a2
b1= sphere_volume (5)
print b1
b2= sphere_volume (7)
print b2
d1 = avg_volume (10,20)
print d1
d2 = avg_volume (20,21)
print d2
f1= area (1,2,3.5)
print f1
f2= area (1,2,2.5)
print f2
e1= right_align ("Waddup")
print e1
e2= right_align ("Hello")
print e2
g1= center ("Hello")
print g1
g2= center ("It's me")
print g2 
h=  msg_box ("Hello")
print h
h=  msg_box ("I love you!")
print h
k= msg_box ("I eat cats!")
print k 
k= msg_box ("I eat dogs!")
print k 
print msg_box (str())
