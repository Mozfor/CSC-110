import doctest

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR, 
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2


# column numbers of data within input csv file
INPUT_TITLE      = 2
INPUT_CAST       = 4
INPUT_DATE       = 6
INPUT_CATEGORIES = 10

#day quantities so I can calculate total days from a date.
DAYS_IN_YEAR   = 365
DAYS_IN_FEB = 28
DAYS_IN_APR = 30

#gonna need this again
def create_date(dateraw: str) -> tuple:
    '''
    takes a date string in which day and year values are both represented by 2-digit integers, and month is a 3-letter string. Then returns a tuple representing the date.
    >>> create_date('9-Feb-20')
    (2020, 2, 9)
    '''
    datelist = dateraw.split('-')
    day = datelist[0]
    monthstr = str(datelist[1])
    year = int(datelist[2])
    monthint = 0
    
    if monthstr == 'Jan':
        monthint = 1
    elif monthstr == 'Feb':
        monthint = 2
    elif monthstr == 'Mar':
        monthint = 3
    elif monthstr == 'Apr':
        monthint = 4
    elif monthstr == 'May':
        monthint = 5
    elif monthstr == 'Jun':
        monthint = 6
    elif monthstr == 'Jul':
        monthint = 7
    elif monthstr == 'Aug':
        monthint = 8
    elif monthstr == 'Sep':
        monthint = 9
    elif monthstr == 'Oct':
        monthint = 10
    elif monthstr == 'Nov':
        monthint = 11
    elif monthstr == 'Dec':
        monthint = 12
    

    year += 2000
    day = int(day)
    
    date = (year, monthint, day)
    return date


def categorize(title_to_category: dict[str, list[str]]) -> (dict[str, list[str]]):
    '''
    basically it just converts a category by title dictionary to a title by category dictionary because it would be a bad idea to work this whole thing into my function
    '''
    
    title_list = []
    category_list = []
    category_to_title = {}
    
    for title in title_to_category:
        title_list.append(title_to_category[title])
        
        for category in title_to_category[title]:
            
            if not category in category_list:
                category_list.append(category)
    
     #because I can't figure out dictionary appending.
    for category in category_list:
        titles_current_category = []
        for title in title_to_category:
            if category in title_to_category[title]:
                
                titles_current_category.append(title)
                
        category_to_title[category] = titles_current_category
        
        
    
    return category_to_title
    
    
    #this is probably the worst code I've ever written
    
    
    
def date_to_days(date: Date) -> int:
    '''
    converts a date tuple to a number of days.
    >>> date_to_days((2019, 4, 4))
    6969
    '''
    #I did this because it's funny.
    total = 0
    if date[MONTH] == 2:
        total += DAYS_IN_FEB
    elif date[MONTH] in [4, 6, 9, 11]:
        total += DAYS_IN_APR
    else: total += 31
    
    total += DAYS_IN_YEAR * (date[YEAR] - START_YEAR)
    total += date[DAY]
    
    return total


def is_older(date1: Date, date2: Date) -> bool:
    '''
    determines if date1 is less recent than date2.
    >>> is_older((2003, 2, 2), (2004, 2, 2))
    True
    >>> is_older((2003, 2, 2), (2003, 2, 1))
    False
    '''

    return (date_to_days(date1) < date_to_days(date2))    

def read_file(filename: str) -> (dict[str, Date],
                                 dict[str, list[str]],
                                 dict[str, list[str]]):
    '''
    Populates and returns a tuple with the following 3 dictionaries
    with data from valid filename.
    
    3 dictionaries returned as a tuple:
    - dict[show title: date added to Netflix]
    - dict[show title: list of actor names]
    - dict[category: list of show titles]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added 
    to the dictionary dict[show title: list of actor names]
    
    Precondition: filename is csv with data in expected columns 
        and contains a header row with column titles.
        NOTE: csv = comma separated values where commas delineate columns
        Show titles are considered unique.
        
    >>> read_file('0lines_data.csv')
    ({}, {}, {})
    
    >>> read_file('11lines_data.csv')
    ({'SunGanges': (2019, 11, 15), \
'PK': (2018, 9, 6), \
'Phobia 2': (2018, 9, 5), \
'Super Monsters Save Halloween': (2018, 10, 5), \
'First and Last': (2018, 9, 7), \
'Out of Thin Air': (2017, 9, 29), \
'Shutter': (2018, 9, 5), \
'Long Shot': (2017, 9, 29), \
'FIGHTWORLD': (2018, 10, 12), \
"Monty Python's Almost the Truth": (2018, 10, 2), \
'3 Idiots': (2019, 8, 1)}, \
\
{'SunGanges': ['Naseeruddin Shah'], \
'PK': ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], \
'Phobia 2': ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], \
'Super Monsters Save Halloween': ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], \
'Shutter': ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], \
'FIGHTWORLD': ['Frank Grillo'], "Monty Python's Almost the Truth": ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Gilliam', 'Terry Jones'], \
'3 Idiots': ['Aamir Khan', 'Kareena Kapoor', 'Madhavan', 'Sharman Joshi', 'Omi Vaidya', 'Boman Irani', 'Mona Singh', 'Javed Jaffrey']}, \
\
{'Documentaries': ['SunGanges', 'Out of Thin Air', 'Long Shot'], \
'International Movies': ['SunGanges', 'PK', 'Phobia 2', 'Out of Thin Air', 'Shutter', '3 Idiots'], \
'Comedies': ['PK', '3 Idiots'], \
'Dramas': ['PK', '3 Idiots'], 'Horror Movies': ['Phobia 2', 'Shutter'], \
'Children & Family Movies': ['Super Monsters Save Halloween'], \
'Docuseries': ['First and Last', 'FIGHTWORLD', "Monty Python's Almost the Truth"], \
'British TV Shows': ["Monty Python's Almost the Truth"]})
    '''
    # TODO: complete this function according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    
    #fuck
    
    title_to_date = {}
    title_to_cast = {}

    title_to_category = {}
    category_list = []
    
    file_handle = open(filename, 'r', encoding = "utf8")
    
    #need to skip the first line
    
    file_handle.readline()
    
    for line in file_handle:
        line = line.split(',')
        
        title = line[INPUT_TITLE]
        date = line[INPUT_DATE]
        cast = line[INPUT_CAST]
        categories = line[INPUT_CATEGORIES]
        
        if date != '':
            date = create_date(date)
            title_to_date[title] = date
        if cast != '':
            cast = cast.split(':')
            title_to_cast[title] = cast
        if categories != '':
            categories = categories.split(':')
            title_to_category[title] = categories
        #I think this works.
        
        
        
        
    category_to_titles = categorize(title_to_category)
    
    
    file_handle.close()
    return (title_to_date, title_to_cast, category_to_titles)
    #I can't believe that worked


def query(filename: str, category: str, date: Date, actors: list[str]
          ) -> list[str]:
    '''
    returns a list of sorted show titles of only shows that:
    - are of the given category
    - have at least one of the actor names in actors in the cast
    - were added to Netflix before the given date
    
    Precondition: category and actor names must match case exactly. 
    For example:
    'Comedies' doesn't match 'comedies', 'Aamir Khan' doesn't match 'aamir khan'
    
    You MUST call read_file and use look ups in the returned dictionaries 
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.
    
    >>> query('0lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), [])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'PK', 'Shutter']
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 8, 1), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['PK', 'Shutter']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['not found', 'not found either'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['Aamir Khan', 'not found', 'not found either'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['not found', 'Aamir Khan', 'not found either'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
    ['not found', 'not found either', 'Aamir Khan'])
    ['3 Idiots', 'PK']
    
    >>> query('large_data.csv', 'Comedies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'PK']
    
    >>> query('large_data.csv', 'Comedies', (2020, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'Dil Chahta Hai', 'Dil Dhadakne Do', 'PK', 'Zed Plus']
    
    >>> query('large_data.csv', 'International Movies', (2020, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'Dangal', 'Dhobi Ghat (Mumbai Diaries)', \
'Dil Chahta Hai', 'Dil Dhadakne Do', 'Lagaan', 'Madness in the Desert', 'PK', \
'Raja Hindustani', 'Rang De Basanti', 'Secret Superstar', 'Shutter', \
'Taare Zameen Par', 'Talaash', 'Zed Plus']
    '''
    # TODO: complete this function according to the documentation
    
    file_handle = open(filename, 'r', encoding="utf8")
    
    result = []
    
    file_handle.readline()
    
    category_bool = bool
    actor_bool = bool
    date_bool = bool
    
    for line in file_handle:
        
        line = line.split(',')
        

        
        this_title = line[INPUT_TITLE]
        this_date = create_date(line[INPUT_DATE])
        this_cast = line[INPUT_CAST]
        this_categories = line[INPUT_CATEGORIES]        
        
        actor_index = 0
        
        actor_bool = 0
        for actor in actors:
            
            if actors[actor_index] in this_cast:
                
                actor_bool = 1
            
            actor_index +=1
        
        if is_older(this_date, date) and (category in this_categories) and actor_bool == 1:

            result.append(this_title)
                
            for i in line:
                
                if i == '':
                    
                    #I couldn't find anything wrong with a few titles that kept adding except that they contained an empty space.
                    result.remove(this_title)
                    
                
    

    file_handle.close()
    result.sort()
    return result