# Author: Nicholas Szegheo 10440343
import sys

from classes import *


TAGS = ["NAME","SEX","BIRT","DEAT","FAMC","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]

ALT_TAGS = ["INDI","FAM"]

indivi_objs = []
fam_objs = []

def readgedcom(gedfile):
    '''Iterates through a GEDCOM file gedfile, returning formatted output
    showing various information, including if the tag is valid.'''
    
    def printgedline(lvl, tag, arg):
        '''Helper: Print in the doc-specified desired format of:
        "<-- <level>|<tag>|<valid?> : Y or N|<arguments>"
        '''
        valid = "Y" if (tag in TAGS or tag in ALT_TAGS) else "N"
        
        print("<-- "+lvl+"|"+tag+"|"+valid+"|"+arg)

    #Assume properly formatted gedcom file.
    for line in gedfile:
        print("-->",line.rstrip())
        list_line = line.split(" ", 2)
        list_line[-1] = list_line[-1].rstrip()
        
        
        if len(list_line) > 2 and list_line[2] in ALT_TAGS:
            # If line has 3 details and the third part is in 
            
            if list_line[2] == "INDI":
                i = Individual()
                i.id = list_line[1]
                # loop through until we hit next INDI/FAM
                pos = gedfile.tell()
                while pos < gedfile.length():
                    if list_line[1] == "NAME":
                        i.name = list_line[2]
                    if list_line[1] == "SEX":
                        i.gender = list_line[2]
                    if list_line[1] == "BIRT": ## check next line to get bday
                        i.b_date = 
                    if list_line[1] == "DEAT":
                        i.alive = False
                    if list_line[1] == "FAMC":
                        i.child = list_line[2]
                    if list_line[1] == "MARR": ## check next line to get marr day
                        i. = 
                        
                        
                indivi_objs.append(i)
            if list_line[2] == "FAM":
                f = Family()
                f.id = list_line[1]
                # loop through until we hit next INDI/FAM
                pos = gedfile.tell()
                while pos < gedfile.length():
                    if list_line[1] == "HUSB":
                        f.husband = list_line[2]    
                    if list_line[1] == "WIFE":
                        f.wife = list_line[2]     
                    if list_line[1] == "CHIL":
                        f.children = list_line[2] 
                    
                fam_objs.append(f)

            printgedline(list_line[0],list_line[2],list_line[1])
        else:
            if len(list_line) > 2:
                # Case of full line
                           
                printgedline(list_line[0],list_line[1],list_line[2])
            else:
                # Case of no args
                printgedline(list_line[0],list_line[1],"")
        

def printSortedIndividuals(individuals):
    individuals.sort(key=lambda x: x.id)
    for individual in individuals:
        print("Individual ID: " + str(individual.id))
        print("Individual Name: " + individual.name)
        print("")

def printSortedFamilies(families):
    families.sort(key=lambda x: x.id)
    for family in families:
        print("Family ID: " + str(family.id))
        print("Husband Name: " + family.husband.name)
        print("Wife Name: " + family.wife.name)
        print("")

if __name__ == "__main__":
    try:
        filename = input("Specify GEDCOM file: ")
        readgedcom(open(filename))

        #Testing for sorted individuals
        individuals = []
        individual1 = Individual(1, "Ed", "M", "5/29/00", 20, "Y", "NA", "NA", "NA")
        individual2 = Individual(2, "Mark", "M", "1/24/00", 21, "Y", "NA", "NA", "NA")
        individuals.append(individual2)
        individuals.append(individual1)
        printSortedIndividuals(individuals)

    except:
        for line in sys.exc_info():
            print(line)
    input("Press Enter to continue.")
