import math
def polysum(n, s):
    return round((0.25*n*s**2)/math.tan(math.pi/n) + (s*n)**2,4)