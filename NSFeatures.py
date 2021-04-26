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
    

def list_deceased(indivs):
    '''
    User Story 29
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

def print_deceased(indivs):
    '''Prints the list of all deceased individuals (US29).'''
    result = list_deceased(indivs)
    print("Deceased Individuals:")
    if result == []:
        print ("None")
    for entry in result:
        print(entry.name, "ID:", entry.id, "Death Date:", entry.d_date)

def list_recently_deceased(indivs):
    '''
    User Story 36
    List recently deceased: List all people in a GEDCOM file who died in the last 30 days.
    Returns a list of individuals.
    '''
    today = date.today()
    deceased = list_deceased(indivs)
    recent_deceased = []
    
    for indiv in deceased:
        death_date = to_date(indiv.d_date)
        if (death_date is not None) and ( (today-death_date).days <= 30 ):
            recent_deceased.append(indiv)
        
    return recent_deceased

def print_recently_deceased(indivs):
    '''Prints the list of all recently deceased individuals (US36).'''
    result = list_recently_deceased(indivs)
    print("Recently Deceased Individuals:")
    if result == []:
        print ("None")
    for entry in result:
        print(entry.name, "ID:", entry.id, "Death Date:", entry.d_date)

def list_birthdays_soon(indivs):
    '''
    User Story 38
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

def print_birthdays_soon(indivs):
    '''Prints the list of all individuals with upcoming birthdays (US38).'''
    result = list_birthdays_soon(indivs)
    print("Individuals with Birthdays Soon:")
    if result == []:
        print ("None")
    for entry in result:
        print(entry.name, "ID:", entry.id, "Birthday:", entry.b_date)

def list_recent_births(indivs):
    '''
    User Story 35
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

def print_recent_births(indivs):
    '''Prints the list of all individuals born recently (US35).'''
    result = list_recent_births(indivs)
    print("Recently Born Individuals:")
    if result == []:
        print ("None")
    for entry in result:
        print(entry.name, "ID:", entry.id, "Birthday:", entry.b_date)

def list_orphans(indivs, fams):
    '''
    User Story 33
    List orphans:
    List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file.
    Returns a list of Individual objects.
    '''
    orphan_ids = []
    for fam in fams:
        if not fam.husband.alive and not fam.wife.alive:
            orphan_ids += fam.children
    orphans = []
    # This lookup is rather slow, algorithmically. Our algorithm has faith in the world
    # and doesn't anticipate thousands of orphans in one family tree.
    # But if there were millions of orphans, I'd try to get all the individuals into a dictionary.
    for indiv in indivs:
        if indiv.id in orphan_ids and indiv.age < 18:
            orphans.append(indiv)
    return orphans

def print_orphans(indivs, fams):
    '''Prints a list of all orphans (US33).'''
    orphans = list_orphans(indivs,fams)
    print("Orphaned Children:")
    if orphans == []:
        # The good ending
        print("None")
    for orphan in orphans:
        # The bad ending
        print(orphan.name, "ID:",orphan.id,"Age:",orphan.age)

def list_recent_survivors(indivs, fams):
    '''
    User Story 37
    List recent survivors:
    List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days.
    Returns a list of Individual objects.
    '''
    # We can use the functionality of User Story 36 (recent deaths) to complete this.
    recentdeaths = list_recently_deceased(indivs)

    # Get only the IDs for lookup.
    for i in range(len(recentdeaths)):
        recentdeaths[i] = recentdeaths[i].id

    # Look through families for the deceased IDs.
    survivors = []
    child_ids = []
    for fam in fams: 
        if fam.husband.id in recentdeaths:
            if fam.wife.alive:
                survivors.append(fam.wife)
            child_ids += fam.children
        elif fam.wife.id in recentdeaths:
            if fam.husband.alive:
                survivors.append(fam.husband)
            child_ids += fam.children
    # Look for the children

    for indiv in indivs:
        if indiv.id in child_ids:
            survivors.append(indiv)

    return survivors

def print_recent_survivors(indivs, fams):
    '''Prints a list of all recent survivors (US37).'''
    survivors = list_recent_survivors(indivs,fams)
    print("Recent Survivors:")
    if survivors == []:
        print("None")
    for indiv in survivors:
        print(indiv.name, "ID:",indiv.id, "Age:",indiv.age)


def list_large_age_gaps(fams):
    '''
    User Story 34
    List large age differences:
    List all couples who were married when the older spouse was more than twice as old as the younger spouse
    Returns a list of families.
    '''
    gross_weirdos = []

    for fam in fams:
        if (fam.husband.age >= fam.wife.age * 2) or (fam.wife.age >= fam.husband.age * 2):
            gross_weirdos.append(fam)
    
    return gross_weirdos

def print_large_age_gaps(fams):
    '''Prints the list of all couples with large age gaps (US34).'''
    gross_weirdos = list_large_age_gaps(fams)
    print("Large Age Gaps:")
    if gross_weirdos == []:
        print("None")
    for fam in gross_weirdos:
        print(fam.husband.name + ", " + fam.wife.name + ", " + "Age Gap: " + str(abs(fam.wife.age - fam.husband.age)) )

def list_upcoming_anniversaries(fams):
    '''
    User Story 39
    List upcoming anniversaries:
    List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days
    Returns a list of families.
    '''
    today = date.today()
    anniversaries_soon = []
    day_threshold = 30

    for fam in fams:
        if fam.mar_date != "NA":
            anni_date = to_date(fam.mar_date)
            if  (anni_date is not None) and (fam.husband.alive and fam.wife.alive) and \
            (0 <= (anni_date - today).days <= day_threshold ):
                anniversaries_soon.append(fam)
        else:
            continue
        
    return anniversaries_soon

def print_upcoming_anniversaries(fams):
    '''Prints the list of couples with an anniversary soon (US39).'''
    anniversaries_soon = list_upcoming_anniversaries(fams)
    print("Upcoming Anniversaries:")
    if anniversaries_soon == []:
        print("None")
    for fam in anniversaries_soon:
        print(fam.husband.name + ", " + fam.wife.name + ", " + "Anniversary: " + fam.mar_date)