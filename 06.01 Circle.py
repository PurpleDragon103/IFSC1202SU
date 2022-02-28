from math import pi

def diameter(x):
    d = x * 2
    return d
def circumference(x):
    c = 2 * pi * x
    return c
def area(x):
    a = pi * x ** 2
    return a

#radiusfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.01 Radius.txt", "r")
radiusfile = open("/workspace/IFSC1202SU/06.01 Radius.txt", "r")
x = float(radiusfile.readline())

print("{0:>15}{1:>15}{2:>15}{3:>15}".format("Radius","Diameter","Circumference","Area"))
while x != "":
    print("{0:15.5f}{1:15.5f}{2:15.5f}{3:15.5f}".format(x,diameter(x),circumference(x),area(x)))
    x = float(radiusfile.readline())
radiusfile.close()
