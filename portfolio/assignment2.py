import doctest

SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def add_to_cart(price: int, total: int, balance: int) -> None:
    '''
    Mimics a shopping cart.
    Takes the price of the item being added, the total price of all the items in the cart, and the account balance. All values are whole numbers.
    >>> add_to_cart(5, 7, 10)
    not enough funds! you need an additional $ 2
    >>> add_to_cart(5, 7, 14)
    cart balance $ 12
    >>> add_to_cart(4, 5, 0)
    not enough funds! you need an additional $ 9
    '''
    new_total = price + total
    remainder = new_total - balance

    if remainder > 0:
        print('not enough funds! you need an additional $', remainder)
    else: print('cart balance $', new_total)

def print_smallest(a: int, b: int, c: int) -> int:
    '''
    takes three integer values and prints the smallest of the three values
    >>> print_smallest(1, 2, 3)
    1
    >>> print_smallest(878732, 2, 4)
    2
    >>> print_smallest(1, 0, -1)
    -1
    >>> print_smallest(3, 5, -2)
    -2
    >>> print_smallest(3, 5, 3)
    3
    '''
    if (a < b) and (a < c):
        print(a)
    elif (b < a) and (b < c):
        print(b)
    elif (c < a) and (c < b):
        print(c)
    elif (a == b) or (a == c):
        print(a)
    elif (b == a) or (b == c):
        print(b)

def is_multiple_of(n1: int, n2: int) -> None:
    '''
    takes two integers and determines whether the first argument is a multiple of the second argument.
    >>> is_multiple_of(12, 3)
    12 is a multiple of 3
    >>> is_multiple_of(10, 3)
    10 is not a multiple of 3
    >>> is_multiple_of(0, 0)
    0 is a multiple of 0
    >>> is_multiple_of(2, 0)
    2 is not a multiple of 0
    >>> is_multiple_of(0, 2)
    0 is a multiple of 2
    '''

    if  n2 != 0:
        remainder = n1 % n2
        if remainder == 0:
            print(n1, 'is a multiple of', n2)
        else: print(n1, 'is not a multiple of', n2)
    elif n1 == 0 and n2 == 0: print(n1, 'is a multiple of', n2)
    else: print(n1, 'is not a multiple of', n2)

def print_triangle_type(a: int, b: int, c: int) -> None:
    '''
    takes three triangle angles as integers and determines which type of triangle they describe.
    >>> print_triangle_type(30, 60, 90)
    right
    >>> print_triangle_type(30, 50, 100)
    obtuse
    >>> print_triangle_type(40, 60, 80)
    acute
    >>> print_triangle_type(50, 50, 50)
    invalid triangle
    >>> print_triangle_type(0, 90, 90)
    invalid triangle
    '''

    if a + b + c != 180 or a == 0 or b == 0 or c == 0:
        triangle_type = 'invalid triangle'
    elif a < 90 and b < 90 and c < 90:
        triangle_type = 'acute'
    elif a == 90 or b == 90 or c == 90:
        triangle_type = 'right'
    elif a > 90 or b > 90 or c > 90:
        triangle_type = 'obtuse'
    print(triangle_type)

def print_time_in_seconds(days: float, hours: float, minutes: float, seconds: float) -> float:
    '''
    takes numerical values as days, hours, minutes, and seconds, converts them all into seconds, and prints the total.
    >>> print_time_in_seconds(1, 1, 1, 1)
    total time: 90061 seconds
    >>> print_time_in_seconds(0, 0, 0, 0)
    total time: 0 seconds
    >>> print_time_in_seconds(0, 5, -2, 532432)
    invalid time
    '''
    if days >= 0 and hours >= 0 and minutes >= 0 and seconds >= 0:
        total_seconds = (days * SECONDS_PER_DAY) + (hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE) + seconds
        print('total time:', total_seconds, 'seconds')
    else: print('invalid time')