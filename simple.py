name= raw_input ("What's your name?: ")
x= raw_input(" type a number:")
y= raw_input ("Type another:")
z= int(x) + int(y)

print "Hey " + name + "!"
print " Did you know?:"
print x + "+" + y + "=" + str(z)

print """Who are you?"""

output= """
Hey {}!
Did you know:
{}+{}={}
""". format (name, x, y, z)

print output
