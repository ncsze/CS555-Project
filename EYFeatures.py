from prettytable import PrettyTable
from datetime import datetime, timedelta

def correctGender(families):
    anyErrors = False
    for family in families:
        if family.husband.gender != "M":
            anyErrors = True
            print("WARNING: " + family.husband.name + " (Husband) is not male.")
        if family.wife.gender != "F":
            anyErrors = True
            print("WARNING: " + family.wife.name + " (Wife) is not female.")
    
    return anyErrors

def uniqueID_indivi(individuals):
    anyErrors = False
    idSet = set()
    for individual in individuals:
        if individual.id in idSet:
            anyErrors = True
            print("WARNING: Individual ID " + str(individual.id) + " is a duplicate.")
        else:
            idSet.add(individual.id)

    return anyErrors

def uniqueID_fam(families):
    anyErrors = False
    idSet = set()
    for family in families:
        if family.id in idSet:
            anyErrors = True
            print("WARNING: Family ID " + str(family.id) + " is a duplicate.")
        else:
            idSet.add(family.id)

    return anyErrors

def uniqueNameAndBDay(individuals):
    anyErrors = False
    individualSet = set()
    for individual in individuals:
        if (individual.name, individual.b_date) in individualSet:
            anyErrors = True
            print("WARNING: Individual " + str(individual.id) + " has the same name and birthday.")
        else:
            individualSet.add((individual.name, individual.b_date))

    return anyErrors

def uniqueFamilies(families):
    anyErrors = False
    familySet = set()
    for family in families:
        if (family.husband.name, family.wife.name, family.mar_date) in familySet:
            anyErrors = True
            print("WARNING: Family " + str(family.id) + " has the same spouses name and marriage date.")
        else:
            familySet.add((family.husband.name, family.wife.name, family.mar_date))

    return anyErrors

def uniqueFirstName(individuals, families):
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

def livingMarried(families):
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

def livingSingle(individuals, families):
    livingSingleList = []
    for individual in individuals:
        if individual.alive and individual.age > 30 and individual.spouse_id == "NA":
            livingSingleList.append(individual)

    for family in families:
        if family.div_date != "NA":
            if family.husband in livingSingleList:
                livingSingleList.remove(family.husband)
            if family.wife in livingSingleList:
                livingSingleList.remove(family.wife)

    table = PrettyTable()
    table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for i in livingSingleList:
        table.add_row([i.id, i.name, i.gender, i.b_date, i.age, i.alive, i.d_date, i.child_id, i.spouse_id])
    print(table)

    return livingSingleList

def multipleBirths(individuals, families):
    individualDict = {}
    for individual in individuals:
        individualDict[individual.id] = individual

    multipleBirthsList = []
    for family in families:
        if len(family.children) <= 1:
            continue

        childrenList = []
        for child in family.children:
            if child in individualDict:
                childrenList.append(individualDict[child])
        
        childrenList.sort(key=lambda i: datetime.strptime(i.b_date, "%d %b %Y"))

        for childIndex in range(len(childrenList) - 1):
            child1 = datetime.strptime(childrenList[childIndex].b_date, "%d %b %Y")
            child2 = datetime.strptime(childrenList[childIndex+1].b_date, "%d %b %Y")
            if child2 - timedelta(days=2) < child1:
                if childrenList[childIndex] not in multipleBirthsList:                  
                    multipleBirthsList.append(childrenList[childIndex])
                if childrenList[childIndex+1] not in multipleBirthsList:
                    multipleBirthsList.append(childrenList[childIndex+1])

    table = PrettyTable()
    table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for i in multipleBirthsList:
        table.add_row([i.id, i.name, i.gender, i.b_date, i.age, i.alive, i.d_date, i.child_id, i.spouse_id])
    print(table)
    
    return multipleBirthsList


