import math

Momentum is the quantity of motion in a body. To find the momentum, you will have to know the mass and the velocity of an object. 

def mul(m,v):
	x = m*v
	return x

def output(name, x, m, v, x):
	return momentum = """
Hey {}!
The momentum of the ball is {}
To find the momentum, you times the mass by its' volume :{} * {} = {}
""".format(name, x, m, v, x)

def main():
	name= raw_input ("What is you name?:")
	m = raw_input("Type in the mass of the ball: ")
	v = raw_input("Type in the velocity of the ball: ")
	x = mul(int(m), int(v))
	print output(name, x, m, v, x)

main()
