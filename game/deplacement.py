from math import *
import math


def lerp( a, b, t):
    return a * (1 - t) + b * t

def linear(t, b, c, d):
    return c*t / d + b