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

def is_multiple_of(n1: int, n2: int) -> None:
    '''
    takes two integers and determines whether the first argument is a multiple of the second argument.
    >>> is_multiple_of(12, 3)
    True
    >>> is_multiple_of(10, 3)
    False
    >>> is_multiple_of(0, 0)
    True
    >>> is_multiple_of(2, 0)
    False
    >>> is_multiple_of(0, 2)
    True
    '''
    if n2 != 0:
        return (n1 % n2 == 0)
    elif n1 == 0: return True
    else: return False
    
def is_end(word: str, end: str) -> bool:
    '''
    checks if the word ends with the given end.
    >>> is_end('how', 'ow')
    True
    >>> is_end('njown', 'ow')
    False
    >>> is_end('84t2', 'ow')
    False
    '''
    return (end) == (word[-len(end):])


def multiply_by(numbers: list[int], multiple: int) -> list[int]:
    '''
    takes a list of numbers and a multiple and returns a new list containing the values multiplied by the multiple.
    >>> multiply_by([4,5,6], 2)
    [8, 10, 12]
    >>> multiply_by([3,5,7], 0)
    [0, 0, 0]
    >>> multiply_by([2,3,4], 1)
    [2, 3, 4]
    >>> multiply_by([2,42,2], -1)
    [-2, -42, -2]
    '''

    counter = 0
    multiplied = numbers
    for num in numbers:
        multiplied[counter] *=multiple
        counter +=1
    return multiplied

def remove_multiples(numbers: list[int], multiple: int) -> list[int]:
    '''
    takes a list of integers and an additional integer argument and returns a new list containing only the values in the old list that are not multiples of the additional integer.
    >>> remove_multiples([1,2,3,4,5,6,7,8,9,10], 3)
    [1, 2, 4, 5, 7, 8, 10]
    >>> remove_multiples([1,2,3,4], 1)
    []
    >>> remove_multiples([1,3,5654, 0], 0)
    [1, 3, 5654]
    '''

    counter = 0
    scrubbed = []
    for num in numbers:
        if not is_multiple_of(numbers[counter], multiple):
            scrubbed.append(numbers[counter])
        counter +=1
    return scrubbed

def remove_ends_with(strings: list[str], end: str) -> list[str]:
    '''
    takes a list of strings and an additional string argument and returns a new list containing only the strings in the old list that do not end with the additional string.
    >>> remove_ends_with(['ruighlo','vrenlo','ilompror','lott', 'lo'], 'lo')
    ['ilompror', 'lott']
    >>> remove_ends_with(['wuh'], '')
    ['wuh']
    >>> remove_ends_with(['  '], ' ')
    []
    '''
    counter = 0
    scrubbed = []
    for num in strings:
        if not(is_end((strings[counter].lower()), end)):
            scrubbed.append(strings[counter])
        counter +=1
    return scrubbed

def get_index_of_largest(numbers: list[int]) -> int:
    '''
    returns the largest number in a list
    >>> get_index_of_largest([3,0,-35,33,1,100,-200,9999, -4])
    9999
    '''
    largest = 0
    counter = 0
    for num in numbers:
        if numbers[counter] > largest:
            largest = numbers[counter]
        counter +=1
    return largest

def does_contain_proper_divisor(numbers: list[int], divisee: int) -> bool:
    '''
    takes a list of integers and another integer and determines if the list contains any proper divisors of the other integer.
    >>> does_contain_proper_divisor([2, 33, 51], 10)
    True
    >>> does_contain_proper_divisor([4, 25, 19], 3)
    False
    '''
    
    counter = 0
    for num in numbers:
        if is_proper_divisor(numbers[counter], divisee) == True:
            return True
        counter += 1
    return False

def are_all_less_than_threshold(numbers: list[int], threshold) -> bool:
    '''
    takes a list of integers and a threshold and determines if all numbers in the list are below the threshold.
    >>> are_all_less_than_threshold([1,2,3,4,5,6,7,8,9], 5)
    False
    >>> are_all_less_than_threshold([-6,-5,-4,-3,-2,-1,0,1,2,3,4], 5)
    True
    '''
    
    counter = 0
    for num in numbers:
        if numbers[counter] >= threshold:
            return False
        counter +=1
    return True