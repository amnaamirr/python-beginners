"""Write a python program to get the volume of a sphere, take the radius as input from user. V = 4/3 πr3""" 

import math 
radius = float(input("ENTER RADIUS: "))
pi = math.pi
volume = 4/3*(pi)*(radius**3)
print("THE VOLUME OF SPHERE IS",volume)