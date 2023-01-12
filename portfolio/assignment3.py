import doctest

SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
KILO = 1000

DISC_TEN_MOD = 0.9
DISC_TWENTY_MOD = 0.8

GST = 0.05
PST = 0.07
SHIPPING_COST = 4.50

def get_smallest(a: int, b: int, c: int) -> int:
    '''
    takes three integer values and returns the smallest value.
    >>> get_smallest(6, 3, 1)
    1
    >>> get_smallest(2, 1, 4)
    1
    >>> get_smallest(4, 53245326, 4123908)
    4
    >>> get_smallest(-5, -1, 0)
    -5
    >>> get_smallest(4, 4, 5)
    4
    '''

    if (a < b) and (a < c):
        return(a)
    elif (b < a) and (b < c):
        return(b)
    elif (c < a) and (c < b):
        return(c)
    elif (a == b) or (a == c):
        return(a)
    elif (b == a) or (b == c):
        return(b)
    
def get_time_in_seconds(days: int, hours: int, minutes: int, seconds: int) -> int:
    '''
    takes days, hours, minutes and seconds and converts all values into seconds and then returns the total.
    >>> get_time_in_seconds(1, 1, 1, 1)
    90061
    >>> get_time_in_seconds(0, 0, 0, 0)
    0
    '''
    
    return(days * SECONDS_PER_DAY) + (hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE) + seconds


def get_average_speed(kilometers: float, days: int, hours: int, minutes: int, seconds: int) -> float:
    '''
    takes distance travelled in kilometers as well as days, hours, minutes, and seconds and returns the average speed in meters per second.
    >>> get_average_speed(170863.9, 1, 1, 1, 1)
    1897.2018964923775
    >>> get_average_speed(1, 5, 2, 6, 4)
    0.0022749815726492615
    >>> get_average_speed(65, 0, 0, 0, 30)
    2166.6666666666665
    >>> get_average_speed(-0.0001, 0, 0, 0, 1)
    -0.1
    '''
    
    return(kilometers * KILO) / get_time_in_seconds(days, hours, minutes, seconds)

def get_box_charge(num_boxes: int, price_per_box: float) -> float:
    '''
    takes the number of boxes being purchased and the price per box and returns the total cost.
    Also applies discounts after 10 boxes, and again after 20 boxes.
    >>> get_box_charge(10, 10)
    90.0
    >>> get_box_charge(25, 10)
    200.0
    >>> get_box_charge(1, 5.5)
    5.5
    >>> get_box_charge(4, 5.5)
    22.0
    >>> get_box_charge(15, 12.5)
    168.75
    >>> get_box_charge(25, 12.5)
    250.0
    >>> get_box_charge(0, 0)
    0
    '''

    total = num_boxes * price_per_box

    if num_boxes >= 20:
        return total * DISC_TWENTY_MOD
    elif num_boxes >= 10:
        return total * DISC_TEN_MOD
    else: return total


def get_order_charge(new_customer: bool, num_boxes_1: int, price_box_1: float, num_boxes_2: int, price_box_2: float) -> float:
    '''
    Takes a boolean representing whether or not the customer is new, then takes the number of prescription 1 boxes and their individual price, and then the number of prescription 2 boxes and their individual price, and returns an order total. 
    - if more than 10 boxes of a single prescription are purchesed, they get the same discount as is detailed in the above function
    - New customers get a 10% discount
    - PST and GST are applied to the total
    - shipping costs $4.50 for orders under $100
    >>> get_order_charge(False, 1, 12.5, 2, 9.5)
    39.78
    >>> get_order_charge(False, 0, 0, 0, 0)
    0.0
    >>> get_order_charge(True, 0, 0, 0, 0)
    0.0
    >>> get_order_charge(True, 1, 2, 4, 1)
    10.548
    '''
    
    presc1_total = get_box_charge(num_boxes_1, price_box_1)
    presc2_total = get_box_charge(num_boxes_2, price_box_2)
    
    total_before_tax = (presc1_total + presc2_total)

    if new_customer == True:
        total_before_tax *= DISC_TEN_MOD
    
    order_gst = total_before_tax * GST
    order_pst = total_before_tax * PST
    
    total_with_tax = (total_before_tax + order_gst + order_pst)
    
    if total_with_tax >= 100 or total_with_tax <= 0:
        return total_with_tax
    else: return total_with_tax + SHIPPING_COST
    
def place_order(funds: float, new_customer: bool, num_boxes_1: int, price_box_1: float, num_boxes_2: int, price_box_2: float) -> bool:
    '''
    takes budget, whether or not the customer is new, the number of prescription 1 boxes and their cost, and the number of prescription 2 boxes and their cost, and finally determines whether or not the customer can afford the order.
    place_order(40.50, False, 1, 12.5, 2, 9.5)
    True
    place_order(0, True, 1, 4, 2, 3)
    False
    place_order(-1, True, -6, 1, 0, 0)
    True
    place_order(1, False, 60, 300, 69, 69)
    False
    '''
    
    return get_order_charge(new_customer, num_boxes_1, price_box_1, num_boxes_2, price_box_2) <= funds

def get_middle(string: str) -> str:
    '''
    returns the middle letter or letters of a given string
    >>> get_middle('gniro')
    'i'
    >>> get_middle('fjofwoej')
    'fw'
    >>> get_middle('')
    ''
    >>> get_middle('123')
    '2'
    >>> get_middle('1234')
    '23'
    '''
    if string == (''):
        return('')

    middle = len(string)//2
    if len(string)%2 == 0:
        return(string[middle-1] + string[middle])

    return(string[middle])