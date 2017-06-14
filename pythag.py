import math
def sides(n):
    h=int(input('What is the first length? '))
    i=int(input('What is the second side length? '))
    j=math.sqrt((h ** 2) + (i ** 2))
    print('The remaining hypotenuse length is ', j)
    return

def tant(x):
    t1 = int(input('What is the length of the opposite side? '))
    t2 = int(input('What is the length of the adjacent side? '))
    t3 = math.atan(t1/t2)
    t4 = math.degrees(t3)
    print ('The angle is ', t3, ' radians or ', t4, ' degrees.')
    return

def cosc(x):
    c1 = int(input('What is the length of the hypotenuse? '))
    c2 = int(input('What is the length of the adjacent side? '))
    c3 = math.acos(c2/c1)
    c4 = math.degrees(c3)
    c5 = math.sqrt((c1 ** 2) - (c2 ** 2))
    print('The angle is ', c3, ' radians or ', c4, ' degrees.')
    print('The length of the opposite side is ', c5)
    return

def sins(x):
    s1 = int(input('What is the length of the opposite side? '))
    s2 = int(input('What is the length of the hypotenuse side? '))
    s3 = math.asin(s1/s2)
    s4 = math.degrees(s3)
    s5 = math.sqrt((s2 ** 2) - (s1 ** 2))
    print('The angle is ', s3, ' radians or ', s4, ' degrees.')
    print('The length of the adjacent side is ', s5)
    return

basic = input('Are we solving for angles (Y/N)')
#change this to .upper or .lower for the following choices
if basic == 'n' and 'N':
    sides(basic)
elif basic == 'y' and 'Y':
    angles1 = input('Evaluating for sin(opposite over hypotenuse) cos (adjacent over hypotenuse) or tan (opposite over adjacent)')
    if angles1 == 'sin':
        sins(basic)
    elif angles1 == 'cos':
        cosc(basic)
    elif angles == 'tan':
        tant(basic)
    else:
        print ('Invalid selection, Please try again.')
else:
    print('Invalid selection, Please try again.')
