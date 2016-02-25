import math

Momentum is the quantity of motion in a body. To find the momentum, you will have to know the mass and the velocity in an object. 

def mul(m,v):
	return m*v

def output(name,v1,p1):
	momentum = """
Hey {}!
The momentum of the ball is {}
{} * {} = {}
""".format(name,v1,p1)
	return momentum

def main():
	
	name= raw_input ("What is you name?:")
	p1 = raw_input ("Momentum of the ball: ")
	m = raw_input("Type in the mass of the ball: ")
	v = raw_input("Type in the velocity of the ball: ")
	
	
	momentum = mul(int(m), int(v))
	out = output(name, x, y, z)
	print out



main()
