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

# represents a Netflix show as (show type, title, directors, cast, date added)
#  where none of the strings are empty strings
NetflixShow = tuple[str, str, list[str], list[str], Date]
TYPE      = 0
TITLE     = 1
DIRECTORS = 2
CAST      = 3
DATE      = 4

# column numbers of data within input csv file
INPUT_TYPE      = 1
INPUT_TITLE     = 2
INPUT_DIRECTORS = 3
INPUT_CAST      = 4
INPUT_DATE      = 6

#day quantities so I can calculate total days from a date.
DAYS_IN_YEAR   = 365
DAYS_IN_FEB = 28
DAYS_IN_APR = 30

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


def create_show(type_: str, title: str, directors: str, actors: str, date:str) -> NetflixShow:
    '''
    oh no. takes 5 strings: genre, title, directors (separated by ':'), actors (separated same way), and the date (see "create_date" function above)
    Then it returns all that info in the show_info format described at the top.
    >>> create_show('movie', 'hell', 'sidney bibbarts:olmen stchell', 'michael:the old guy:stolitch veldentenmaus', '22-sep-99')
    ('movie', 'hell', ['sidney bibbarts', 'olmen stchell'], ['michael', 'the old guy', 'stolitch veldentenmaus'], (2099, 0, 22))
    >>> create_show('', '', ':', '', '50-sep-99')
    ('', '', ['', ''], [], (2099, 0, 50))
    '''
    date = create_date(date)
    actors = actors.split(':')
    directors = directors.split(':')
    if directors == ['']:
        directors = []
    if actors == ['']:
        actors = []
        
    show_info = (type_, title, directors, actors, date)
    return(show_info)

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


def index_oldest_date(dates: list[Date]) -> int:
    '''
    takes a list of NeflixShows and returns the index of the one with the oldest date_added value.
    '''

    index = 0
    index_oldest = 0
    
    for date in dates:
        oldest_date = dates[index_oldest]
        test_date = dates[index]
        if is_older(test_date, oldest_date) == True: index_oldest = index
        index +=1
    
    return index_oldest



def read_file(filename: str) -> list[NetflixShow]:
    '''
    reads file into list of NetflixShow format.

    Precondition: filename is in csv format with data in expected columns
        and contains a header row with the column titles.
        NOTE: csv = comma separated values where commas delineate columns

    >>> read_file('0lines_data.csv')
    []
    
    >>> read_file('9lines_data.csv')
    [('Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], (2019, 11, 15)), \
('Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], (2018, 9, 6)), \
('Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], (2018, 9, 5)), \
('Movie', 'Super Monsters Save Halloween', [], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)), ('TV Show', 'First and Last', [], [], (2018, 9, 7)), \
('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29)), \
('Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], (2018, 9, 5)), \
('Movie', 'Long Shot', ['Jacob LaMendola'], [], (2017, 9, 29)), ('TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], (2018, 10, 12))]
    '''
    file_handle = open(filename, 'r', encoding="utf8")

    index = 1 #just skip the header row lol
    

    file_as_str = file_handle.read()

    file_list = file_as_str.split('\n')

    output = []
    while not index >= len(file_list):

        current_show = file_list[index].split(',')
        
        show_type = current_show[1]
        title = current_show[2]
        directors = current_show[3]
        cast = current_show[4]
        date = current_show[6]

        
        output.append(create_show(show_type, title, directors, cast, date))
        index +=1

    file_handle.close()
    return output

def get_oldest_titles(show_data: list[NetflixShow]) -> list[str]:
    '''
    returns a list of the titles of NetflixShows in show_data
    with the oldest added date

    >>> shows_unique_dates = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett',\
    'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> shows_duplicate_oldest_date = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina',\
    'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2017, 9, 29)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> get_oldest_titles([])
    []
    >>> get_oldest_titles(shows_unique_dates)
    ['Out of Thin Air']
    >>> get_oldest_titles(shows_duplicate_oldest_date)
    ['Super Monsters Save Halloween', 'Out of Thin Air']
    '''
    
    if show_data == []:
        return []
    
    result_list = []
    dates_list = []
    for show in show_data:
        dates_list.append(show[DATE])

    index_oldest = index_oldest_date(dates_list)

    oldest_date = show_data[index_oldest][DATE]

    index = 0
    for show in show_data:
        if oldest_date == show_data[index][DATE]:
            result_list.append(show_data[index][TITLE])
        index +=1
    return result_list


def get_actors_in_most_shows(shows: list[NetflixShow]) -> list[str]:
    '''
    returns a list of actor names that are found in the casts of the most shows

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]

    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]

    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]

    >>> get_actors_in_most_shows([])
    []

    >>> get_actors_in_most_shows(l_unique_casts)
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers', 'Michael Cera', 'Emma Stone', 'Paresh Rawal']

    >>> get_actors_in_most_shows(one_actor_in_multiple_casts)
    ['Jonah Hill']

    >>> get_actors_in_most_shows(actors_in_multiple_casts)
    ['Om Puri', 'Jonah Hill']
    '''

    index = 0
    actor_index = 0
    previous_record = 0
    result_list = []
    
    
    for show in shows:
        test_show = shows[index]
        actor_index = 0
        
        while actor_index != len(test_show[CAST]):

            test_actor = test_show[CAST][actor_index]
            test_actors_shows = 0
            
            show_checker_index = 0
            
            for show in shows:
                
                if test_actor in shows[show_checker_index][CAST]:
                    test_actors_shows +=1
                show_checker_index +=1 
                
            if test_actors_shows > previous_record:
                result_list = [test_actor]
                previous_record = test_actors_shows
                
            elif (test_actors_shows == previous_record) and not (test_actor in result_list):
                result_list.append(test_actor)
                
            actor_index +=1

        index +=1
        
    return result_list

    

def get_shows_with_search_terms(show_data: list[NetflixShow], terms: list[str]) -> list[NetflixShow]:
    '''
    returns a list of only those NetflixShow elements in show_data
    that contain any of the given terms in the title.
    Matching of terms ignores case ('roAD' is found in 'Road to Sangam') and
    matches on substrings ('Sang' is found in 'Road to Sangam')

    Precondition: the strings in terms are not empty strings

    >>> movies = [\
    ('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)),\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> terms1 = ['House']
    >>> terms1_wrong_case = ['hoUSe']

    >>> terms_subword = ['Sang']

    >>> terms2 = ['House', 'Road', 'Basanti']
    >>> terms2_wrong_case = ['house', 'ROAD', 'bAsanti']

    >>> get_shows_with_search_terms([], [])
    []

    >>> get_shows_with_search_terms(movies, [])
    []

    >>> get_shows_with_search_terms([], terms1)
    []

    >>> get_shows_with_search_terms(movies, terms1)
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms1_wrong_case)
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms_subword)
    [('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2)
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)), ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2_wrong_case)
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)), ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]
    '''

    
    
    terms_index = 0
    shows_index = 0
    result = []
    
    if terms == []:
        return []
    
    if show_data == []:
        return []
    
    
    shows_index = 0

    
    for i in show_data:
        
        current_show = show_data[shows_index]
        current_title = current_show[TITLE]
        current_title = current_title.lower()
        
        current_title = current_title
        terms_index = 0
        
        for i in terms:
            
            
            test_term = terms[terms_index].lower()
            
            
            if test_term in current_title:
                
        
                result.append(current_show)
                
                
            terms_index +=1
            
        shows_index +=1

    return result


def query(show_data: list[NetflixShow]) -> list[str]:
    '''
    Returns a list of only the show titles from show_data
    that are acted in by the 'most popular' actors
    where the 'most popular' is defined as the actors in the most shows.
    The returned list is in sorted order and does not contain duplicate entries.

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]
    
    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]
    
    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]
    
    >>> query([])
    []
    
    >>> query(l_unique_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    
    >>> query(one_actor_in_multiple_casts)
    ['Maniac', 'Superbad']

    >>> query(actors_in_multiple_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    '''
    
    most_popular_actors = get_actors_in_most_shows(show_data)
    
    show_list = []
    title_list = []
    actor_index = 0
    show_index = 0
    index = 0
    

    for actor in most_popular_actors:
        test_actor = most_popular_actors[actor_index]
        
        show_index = 0
        
        for show in show_data:
            
            test_show = show_data[show_index]
            
            if (test_actor in test_show[CAST]) and not (test_show in show_list):
                
                show_list.append(test_show)
                
            show_index +=1
        actor_index +=1
    
    for show in show_list:
        
        title_list.append(show_list[index][TITLE])
        index +=1
    
    title_list.sort()
    return title_list