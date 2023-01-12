import doctest

def is_proper_divisor(n1: int, n2: int) -> bool:
    '''
    takes two non-negative integers and determines whether the first is a proper divisor of the second.
    >>> is_proper_divisor(2, 0)
    True
    >>> is_proper_divisor(0, 0)
    True
    >>> is_proper_divisor(0, 2)
    False
    >>> is_proper_divisor(5, 15)
    True
    >>> is_proper_divisor(2, 15)
    False
    '''

    if n1 == 0:
        if n2 == 0:
            return True
        else: return False

    return (n2 % n1) == 0

def sum_of_proper_divisors(n: int) -> int:
    '''
    returns the sum of all proper divisors of the given non negative integer, minus the integer itself.
    >>> sum_of_proper_divisors(12)
    16
    >>> sum_of_proper_divisors(25)
    6
    >>> sum_of_proper_divisors(1)
    0
    '''

    testnum = 1
    total = 0

    for num in range(n -1):
        if is_proper_divisor(testnum, n) == True:
            total += testnum
        testnum += 1
    return(total)

def get_abundance(n: int) -> int:
    '''
    returns the abundance of a given integer.
    >>> get_abundance(12)
    4
    >>> get_abundance(5)
    0
    >>> get_abundance(1)
    0
    >>> get_abundance(30)
    12
    >>> get_abundance(70)
    4
    >>> get_abundance(100)
    17
    '''

    if (sum_of_proper_divisors(n) > n):
        return(sum_of_proper_divisors(n)-n)
    else: return(0)

def get_multiples(startnum: int, multiple: int, length: int) -> str:
    '''
    takes the minimum value, the number being checked for multiples, and the maximum value and prints a string of all multiples of the second argument, starting at the first argument and with a length of the last argument.
    >>> get_multiples(1, 5, 15)
    '5 10 15 20 25 30 35 40 45 50 55 60 65 70 75'
    >>> get_multiples(0, 0, 0)
    ''
    >>> get_multiples(30, 8, 21)
    '32 40 48 56 64 72 80 88 96 104 112 120 128 136 144 152 160 168 176 184 192'
    >>> get_multiples(10, 5, 1)
    '10'
    >>> get_multiples(7, 5, 3)
    '10 15 20'
    '''

    testnum = startnum
    string = ('')

    for num in range(length * multiple):
        if testnum % multiple == 0:
            string += (str(testnum) + ' ')
        testnum += 1
    return (string[0:len(string)-1])

def print_multiplication_table(startnum_x: int, width: int, startnum_y: int, height: int) -> None:
    '''
    prints a multiplication table. Takes arguments for the number to start the x-axis at, the width of the table, the number to start the y-axis at, and the height of the table, in that order.
    >>> print_multiplication_table(1, 10, 1, 10)
      1 2 3 4 5 6 7 8 9 10 
    1 1 2 3 4 5 6 7 8 9 10
    2 2 4 6 8 10 12 14 16 18 20
    3 3 6 9 12 15 18 21 24 27 30
    4 4 8 12 16 20 24 28 32 36 40
    5 5 10 15 20 25 30 35 40 45 50
    6 6 12 18 24 30 36 42 48 54 60
    7 7 14 21 28 35 42 49 56 63 70
    8 8 16 24 32 40 48 56 64 72 80
    9 9 18 27 36 45 54 63 72 81 90
    10 10 20 30 40 50 60 70 80 90 100
    >>> print_multiplication_table(0, 3, 4, 10)
      0 1 2 
    4 0 4 8
    5 0 5 10
    6 0 6 12
    7 0 7 14
    8 0 8 16
    9 0 9 18
    10 0 10 20
    11 0 11 22
    12 0 12 24
    13 0 13 26
    >>> print_multiplication_table(1, 1, 1, 1)
      1 
    1 1
    '''

    toprow = startnum_x

    print('  ', end='')
    for num in range(width):
        print(toprow, end = ' ')
        toprow += 1
    print('')
    for num in range(height):
        print((startnum_y), get_multiples(startnum_x, startnum_y, width))
        startnum_y += 1