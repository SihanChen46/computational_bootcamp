#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Useful items to model a Point in Euclidean space.
https://en.wikipedia.org/wiki/Point_(geometry)#Points_in_Euclidean_geometry
"""

import math

class Point:
    "Model a point in euclidean space."

    def __init__(self, x=0, y=0):
        "Create a new point at x, y"
        self.x = x
        self.y = y
        self.len = math.hypot(self.x, self.y) 

def cityblock_distance(p, q): 
    "City block distance between two points."
    return abs(p.x - q.x) + abs(p.y - q.y) 

def euclidean_distance(p, q): 
    "Euclidean (hypotenuse) distance between two points"
    return math.hypot(p.x - q.x, p.y - q.y)

origin = Point(x=0, y=0) 
