import doctest
import random

MIN_DIE = 1
MAX_DIE = 6

def roll_one_die() -> int:
    """ 
    simulates the roll of a single dice between MIN_DIE and MAX_DIE inclusive 
    and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    #generates a random number between MIN_DIE and MAX_DIE inclusive
    die = random.randint(MIN_DIE, MAX_DIE)
    
    #for testing to allow you to enter the dice roll you want at the keyboard
    #comment out the line above and uncomment this line:
    #die = int(input('enter a simulated dice roll\n'))
    
    return die


def get_sum_of_digits(n: int) -> int:
    '''
    takes an integer and returns the sum of its digits
    >>> get_sum_of_digits(555)
    15
    >>> get_sum_of_digits(-333)
    9
    >>> get_sum_of_digits(10001)
    2
    >>> get_sum_of_digits(0000)
    0
    '''
    length = len(str(n))
    n = abs(n)

    current = n
    total = 0
    while not length == 0:
        
        total += (current % 10)
        current //= 10
        
        length -=1
    return total 

def is_harshad_number(n: int) -> bool:
    '''
    takes integer and determines whether it is a harshad number.
    >>> is_harshad_number(432)
    True
    >>> is_harshad_number(433)
    False
    '''
    
    return (n != 0 and ((n % get_sum_of_digits(n)) == 0))

def get_first_n_harshad_numbers(n: int) -> str:
    '''
    returns a string of harshad numbers from 0 to n
    >>> get_first_n_harshad_numbers(0)
    ''
    >>> get_first_n_harshad_numbers(1)
    '1'
    >>> get_first_n_harshad_numbers(20)
    '1,2,3,4,5,6,7,8,9,10,12,18,20,21,24,27,30,36,40,42'
    '''
    sequence = []
    total_harshads = 0
    total_tests = 0
    counting_variable = 1
    
    while (total_harshads != n):
        if is_harshad_number(counting_variable):
            sequence.append(counting_variable)
            total_harshads += 1
        counting_variable += 1


    
    list_string = (','.join([str(i) for i in sequence]))
    
    return(list_string)

def play(guess1: int, guess2: int, bet: int) -> None:
    
    roll1 = roll_one_die()
    roll2 = roll_one_die()
    roll_list = [roll1, roll2]
    guess_list = [guess1, guess2]
    
    print('you guessed:', guess1,'and', guess2, 'and bet', bet)
    print('you rolled:', roll1,'and', roll2)
    
    if (roll1 in guess_list) and (roll2 in guess_list):
        
        print('both right!')
        print('your total:', (bet*3), '$')
        
    elif (roll1 in guess_list) or (roll2 in guess_list):
        
        if guess1 in roll_list:
            
            correct_guess = guess1
            wrong_guess = guess2
            
        elif guess2 in roll_list:
            
            correct_guess = guess2
            wrong_guess = guess1
        
        print('you got half right')
        losing_target = roll1 + roll2
        print('losing target:', losing_target)
        print('rolling a second chance...')
        
        roll1 = roll_one_die()
        roll2 = roll_one_die()
        roll_list = [roll1, roll2]
        print('you rolled:', roll1,'and', roll2)
        
        
        if (((roll1 + roll2) != losing_target) and (wrong_guess in roll_list)):
            
            print('You got the other half correct!')
            print('Your total:', (bet*3), '$')
            
        else: print('you lose for real')
        
    else: print('you lost:', bet, '$')