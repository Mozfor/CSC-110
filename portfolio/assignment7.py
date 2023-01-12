import doctest

date = tuple[int, int, int]
'''
represents a date (yyyy, mm, dd)
'''

showInfo = tuple[str, str, list[str], list[str], date]
'''
provides information about a netflix(c) show:
genre, title, directors, actors, date)
'''

def multiply_by(list1: list[None], list2: list[int]) -> None:
    '''
    takes two lists. multiplies every element in the first list by every element in the corresponding position in the second list.
    >>> multiply_by([3,5,6], [2,1,6])

    '''
    counter = 0
    for i in range(len(list1)):
        list1[counter] *= list2[counter]
        counter +=1

def create_date(dateraw: str) -> tuple:
    '''
    takes a date string in which day and year values are both represented by 2-digit integers, and month is a 3-letter string. Then returns a tuple representing the date.
    >>> create_date('9-Feb-20')
    (2018, 2, 9)
    '''
    datelist = dateraw.split('-')
    day = datelist[0]
    monthstr = datelist[1].lower()
    year = int(datelist[2])
    
    if monthstr == 'jan':
        monthint = 1
    elif monthstr == 'feb':
        monthint = 2
    elif monthstr == 'mar':
        monthint = 3
    elif monthstr == 'apr':
        monthint = 4
    elif monthstr == 'may':
        monthint = 5
    elif monthstr == 'jun':
        monthint = 6
    elif monthstr == 'jul':
        monthint = 7
    elif monthstr == 'aug':
        monthint = 8
    elif monthstr == 'sep':
        monthint = 9
    elif monthstr == 'oct':
        monthint = 10
    elif monthstr == 'nov':
        monthint = 11
    elif monthstr == 'dec':
        monthint = 12
    else: print('wrong format')
    
    year += 2000
    day = int(day)
    
    date = (year, monthint, day)
    return date

def create_show(type_: str, title: str, directors: str, actors: str, date:str) -> showInfo:
    '''
    oh no. takes 5 strings: genre, title, directors (separated by ':'), actors (separated same way), and the date (see "create_date" function above)
    Then it returns all that info in the show_info format described at the top.
    >>> create_show('movie', 'hell', 'sidney bibbarts:olmen stchell', 'michael:the old guy:stolitch veldentenmaus', '22-sep-99')
    ('movie', 'hell', ['sidney bibbarts', 'olmen stchell'], ['michael', 'the old guy', 'stolitch veldentenmaus'], (2099, 9, 22))
    >>> create_show('', '', ':', '', '50-sep-99')
    ('', '', ['', ''], [''], (2099, 9, 50))
    '''
    date = create_date(date)
    actors = actors.split(':')
    directors = directors.split(':')

    show_info = (type_, title, directors, actors, date)
    return(show_info)

def get_titles(shows: list[showInfo]) -> list:
    '''
    Takes a list of show info and returns a list of titles.
    >>> get_titles([('movie', 'hell', 'sidney bibbarts:olmen stchell', 'michael:the old guy:stolitch veldentenmaus', '22-sep-2099'), ('movie', 'the grand fight', 'dolmen stradd', 'halden shart:pronti dvelton:potor begersnam', '72-aug-3042')])
    ['hell', 'the grand fight']
    '''
    result = []
    counter = 0
    for show in shows:
        result.append(shows[counter][1])
        counter +=1

    return result

def is_actor_in_show(show: str(showInfo), actor:str) ->bool:
    '''
    takes show info and a name and determines if they are an actor in the show.
    I omitted irrelevant values in the docstring tests because I'm tired
    >>> is_actor_in_show(('','','',['tru', 'fwe', 'sdf', 'fdg', 'sd'],''),'tru')
    True
    >>> is_actor_in_show(('','','',['trU','fwe','sdf','fdg','sd'],''),'Tru')
    True
    >>> is_actor_in_show(('','','',['fwe','sdf','fdg','sd'],''),'tru')
    False
    >>> is_actor_in_show(('','','','',''),'tru')
    False
    >>> is_actor_in_show(('','','',['tru','fwe','sdf','fdg','sd'],''),'')
    False
    '''
    actor = actor.lower()
    actors = show[3]
    count = 0
    for i in actors:
        actors[count] = actors[count].lower()
        count +=1
    return actor in actors

def count_shows_before_date(shows: list(str(showInfo)), date) -> int:
    '''
    takes a list of shows formatted according to showInfo alias and a date formatted according to the date alias and then counts the number of shows before the given date.
    >>> count_shows_before_date([('','','','',(2021, 1, 1)), ('','','','',(2019, 1, 1)), ('','','','',(2020,2,1))], (2020, 1, 1))
    1
    >>> count_shows_before_date([('','','','',(2021, 1, 1)), ('','','','',(2019, 1, 1)), ('','','','',(2020,1,2))], (2020, 1, 3))
    2
    >>> count_shows_before_date([('','','','',(2021, 1, 1)), ('','','','',(2019, 1, 1)), ('','','','',(2020,2,1))], (2022, 1, 1))
    3
    >>> count_shows_before_date([('','','','',(2021, 1, 1)), ('','','','',(2019, 1, 1)), ('','','','',(2020,2,1))], (1, 1, 1))
    0
    '''
    counter = 0
    total = 0
    target_year = date[0]
    target_month = date[1]
    target_day = date[2]
    for i in shows:

        test_year = shows[counter][4][0]
        test_month = shows[counter][4][1]
        test_day = shows[counter][4][2]
        
        if test_year < target_year:
            total +=1
        elif (test_year == target_year):
            if (test_month < target_month):
                total +=1
            elif (test_month == target_month):
                if (test_day < target_day):
                    total +=1

        counter +=1
    return total

def get_shows_with_actor(shows: list(str(showInfo)), actor: str) -> list[showInfo]:
    '''
    takes a list of showInfo and an actor name and returns a list containing only showInfos that contain the actor's name.
    >>> get_shows_with_actor([('','','',['oo3', 'poiu', 'ihh'], ()), ('','','', ['dfe', 'oo3', 'opeiw'], ())], 'oo3')
    [('', '', '', ['oo3', 'poiu', 'ihh'], ()), ('', '', '', ['dfe', 'oo3', 'opeiw'], ())]
    >>> get_shows_with_actor([('','','',['oo3', 'poiu', 'ihh'], ()), ('','','', ['dfe', 'oO3', 'opeiw'], ())], 'Oo3')
    [('', '', '', ['oo3', 'poiu', 'ihh'], ()), ('', '', '', ['dfe', 'oo3', 'opeiw'], ())]
    >>> get_shows_with_actor([('','','',['oo3', 'poiu', 'ihh'], ()), ('','','', ['dfe', 'eee', 'opeiw'], ())], 'oo3')
    [('', '', '', ['oo3', 'poiu', 'ihh'], ())]
    '''

    counter = 0
    result = []

    for i in shows:
        if is_actor_in_show(shows[counter], actor):
            result.append(shows[counter])
        counter +=1
    return result