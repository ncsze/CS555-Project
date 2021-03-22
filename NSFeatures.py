from classes import *
from datetime import date

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

def us29_print(indivs):
    '''Prints the list of all deceased individuals.'''
    result = userstory29(indivs)
    print("Deceased Individuals:")
    if result == []:
        print ("None")
    for entry in result:
        print(entry.name, "ID:", entry.id, "Death Date:", entry.d_date)

def us36_print(indivs):
    '''Prints the list of all recently deceased individuals.'''
    result = userstory36(indivs)
    print("Recently Deceased Individuals:")
    if result == []:
        print ("None")
    for entry in result:
        print(entry.name, "ID:", entry.id, "Death Date:", entry.d_date)
