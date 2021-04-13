from prettytable import PrettyTable

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

def userstory23(individuals):
    anyErrors = False
    individualSet = set()
    for individual in individuals:
        if (individual.name, individual.b_date) in individualSet:
            anyErrors = True
            print("WARNING: Individual " + str(individual.id) + " has the same name and birthday.")
        else:
            individualSet.add((individual.name, individual.b_date))

    return anyErrors

def userstory24(families):
    anyErrors = False
    familySet = set()
    for family in families:
        if (family.husband.name, family.wife.name, family.mar_date) in familySet:
            anyErrors = True
            print("WARNING: Family " + str(family.id) + " has the same spouses name and marriage date.")
        else:
            familySet.add((family.husband.name, family.wife.name, family.mar_date))

    return anyErrors

def userstory25(individuals, families):
    anyErrors = False

    childIndividualDict = {}
    for individual in individuals:
        childIndividualDict[individual.id] = individual

    for family in families:
        childSet = set()
        
        for child in family.children:
            if child not in childIndividualDict:
                print("WARNING: Child Individual ID " + str(child) + " not in individuals")
                continue

            childIndividual = childIndividualDict[child]
            if (childIndividual.name, childIndividual.b_date) in childSet:
                anyErrors = True
                print("WARNING: Child " + str(childIndividual.id) + " has the same name and birthday.")
            else:
                childSet.add((childIndividual.name, childIndividual.b_date))
            
    return anyErrors

def userstory30(families):
    livingMarriedList = []
    for family in families:
        if family.div_date == "NA":
            if family.husband.alive:
                livingMarriedList.append(family.husband)
            if family.wife.alive:
                livingMarriedList.append(family.wife)

    table = PrettyTable()
    table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for i in livingMarriedList:
        table.add_row([i.id, i.name, i.gender, i.b_date, i.age, i.alive, i.d_date, i.child_id, i.spouse_id])
    print(table)

    return livingMarriedList

