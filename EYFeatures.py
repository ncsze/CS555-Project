def userstory21(families):
    anyErrors = False
    for family in families:
        if family.husband.gender != "M":
            anyErrors = True
            print("WARNING: " + family.husband.name + " (Husband) is not male.")
        if family.wife.gender != "F":
            anyErrors = True
            print("WARNING: " + family.wife.name + " (Wife) is not female.")
    
    return anyErrors

def userstory22_indivi(individuals):
    anyErrors = False
    idSet = set()
    for individual in individuals:
        if individual.id in idSet:
            anyErrors = True
            print("WARNING: Individual ID " + str(individual.id) + " is a duplicate.")
        else:
            idSet.add(individual.id)

    return anyErrors

def userstory22_fam(families):
    anyErrors = False
    idSet = set()
    for family in families:
        if family.id in idSet:
            anyErrors = True
            print("WARNING: Family ID " + str(family.id) + " is a duplicate.")
        else:
            idSet.add(family.id)

    return anyErrors

