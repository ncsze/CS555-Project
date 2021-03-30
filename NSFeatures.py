from classes import *
from datetime import date, timedelta

def month_converter(string):
    if string == "JAN":
        return 1
    if string == "FEB":
        return 2
    if string == "MAR":
        return 3
    if string == "APR":
        return 4
    if string == "MAY":
        return 5
    if string == "JUN":
        return 6
    if string == "JUL":
        return 7
    if string == "AUG":
        return 8
    if string == "SEP":
        return 9
    if string == "OCT":
        return 10
    if string == "NOV":
        return 11
    if string == "DEC":
        return 12
    raise TypeError("String did not match any month.")

def to_date(death_date):
    strings = death_date.split(" ")
    if (len(strings) != 3):
        raise TypeError("Death date is in invalid string format.")
    
    try:
        date_form = date( int(strings[2]) , month_converter(strings[1]), int(strings[0]) )
        return date_form
    except:
        # date is invalid
        return None
    

def userstory29(indivs):
    '''
    List deceased: List all deceased individuals in a GEDCOM file.
    Returns a list of individuals.
    '''
    deceased = []

    for indiv in indivs:
        if (type(indiv) is Individual):
            if (not indiv.alive):
                # Add all individuals that aren't alive to the list.
                deceased.append(indiv)
        else:
            raise TypeError('List deceased: Individual list contains non-Individual type.')

    return deceased

def us29_print(indivs):
    '''Prints the list of all deceased individuals.'''
    result = userstory29(indivs)
    print("Deceased Individuals:")
    if result == []:
        print ("None")
    for entry in result:
        print(entry.name, "ID:", entry.id, "Death Date:", entry.d_date)

def userstory36(indivs):
    '''
    List recently deceased: List all people in a GEDCOM file who died in the last 30 days.
    Returns a list of individuals.
    '''
    today = date.today()
    deceased = userstory29(indivs)
    recent_deceased = []
    
    for indiv in deceased:
        death_date = to_date(indiv.d_date)
        if (death_date is not None) and ( (today-death_date).days <= 30 ):
            recent_deceased.append(indiv)
        
    return recent_deceased

def us36_print(indivs):
    '''Prints the list of all recently deceased individuals.'''
    result = userstory36(indivs)
    print("Recently Deceased Individuals:")
    if result == []:
        print ("None")
    for entry in result:
        print(entry.name, "ID:", entry.id, "Death Date:", entry.d_date)

def userstory38(indivs):
    '''
    List all living people in a GEDCOM file whose birthdays occur in the next 30 days.
    Returns a list of individuals.
    '''
    today = date.today()
    birthdays_soon = []
    
    day_threshold = 30

    for indiv in indivs:
        birth_date = to_date(indiv.b_date)
        if (birth_date is not None):

            if (today + timedelta(days=day_threshold)).year != today.year and birth_date.month == 1:
                # If the birthday is in January of next year, make sure the date reflects it by having year + 1.
                birthday = birth_date.replace(year = today.year + 1)
            else:
                #Otherwise, just make sure that the year is the same as today.
                birthday = birth_date.replace(year = today.year)
            
            if ( (indiv.alive) and ( 0 <= (birthday - today).days <= day_threshold) ):
                birthdays_soon.append(indiv)
        
    return birthdays_soon

def us38_print(indivs):
    '''Prints the list of all individuals with upcoming birthdays.'''
    result = userstory38(indivs)
    print("Individuals with Birthdays Soon:")
    if result == []:
        print ("None")
    for entry in result:
        print(entry.name, "ID:", entry.id, "Birthday:", entry.b_date)

def userstory35(indivs):
    '''
    List all people in a GEDCOM file who were born in the last 30 days.
    Returns a list of individuals.
    '''
    today = date.today()
    born_recently = []
    
    for indiv in indivs:
        birth_date = to_date(indiv.b_date)
        if (birth_date is not None):
            if (0 <= (today - birth_date).days <= 30 ):
                born_recently.append(indiv)
        
    return born_recently

def us35_print(indivs):
    '''Prints the list of all individuals born recently.'''
    result = userstory35(indivs)
    print("Recently Born Individuals:")
    if result == []:
        print ("None")
    for entry in result:
        print(entry.name, "ID:", entry.id, "Birthday:", entry.b_date)