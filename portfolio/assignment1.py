import math
def print_cat():
    '''
    prints a vague ASCII rendition of a domestic cat's face and hands
    '''
    print(' /\\____/\\\n(  o  o  )\n-\- UU -/-\n  |````|\n{\'\'}  {\'\'}')
    
def print_fish():
    '''
    prints a vague ASCII rendition of a fish
    '''
    print('           _____\n  ________//////__// \n / o     ___    __{\n>\"__))_/    \  /  \\\ \n             \\\\\\ \n              `` ')

def print_spacer():
    '''
    prints a spacer line to separate ASCII art
    '''
    print('/~~~~~~~~\\')

def print_logo():
    '''
    prints the cat and fish ASCII twice with a spacer between them
    '''
    for x in range(2):
        print_spacer()
        print_cat()
        print_spacer()
        print_fish()
    print_spacer()
    
def calculate_surface_area(height: float, diameter: float):
    '''
    Takes numerical values for height and diameter and calculates 
    the surface area of a right cylinder, rounded to one decimal place.
    >>> calculate_surface_area(6.64, 5.643)
    167.7
    >>> calculate_surface_area(-2, -4)
    50.3
    '''
    radius = diameter/2
    pi = (math.pi)
    surface_area_top = 2 * pi * radius ** 2
    surface_area_sides = 2 * pi * radius * height
    surface_area = surface_area_top + surface_area_sides
    print("{0:.1f}".format(surface_area))