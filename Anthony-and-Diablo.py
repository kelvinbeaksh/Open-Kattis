'''
Square area = circle area = (pi)(R^2). Square perimeter = 4(R)sqrt(pi). 
Ratio of Sq perimeter/Circle perimeter = (2)/(sqrt(pi)) = 1.1238. Thus the square has the greater perimeter.

Take the smaller perimeter to construct the cage, pick circle
'''
from math import pi
A, N = map(float, input().split())


if (((A/pi)**0.5)*2*pi) > N:
    print("Need more materials!")
else:
    print("Diablo is happy!")