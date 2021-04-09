# Author: Nicholas Szegheo 10440343
import sys
from datetime import date
from classes import *
from prettytable import PrettyTable
from EYFeatures import *
from MPFeatures import *
from JYFeatures import *
from NSFeatures import *
from utilities import *


TAGS = ["NAME","SEX","BIRT","DEAT","FAMC","FAMS","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]

ALT_TAGS = ["INDI","FAM"]    

def readgedcom(gedfile, printflag):
    '''Iterates through a GEDCOM file contents in array gedfile, returning formatted output
    showing various information, including if the tag is valid.
    Returns (indivs, fams), indivs being a list of the individuals in the GEDCOM and fams 
    being a list of the families in the file, each in the types laid out in classes.py.
    '''
    indivi_objs = []
    fam_objs = []
    

    def printgedline(lvl, tag, arg):
        '''Helper: Print in the doc-specified desired format of:
        "<-- <level>|<tag>|<valid?> : Y or N|<arguments>"
        '''
        valid = "Y" if (tag in TAGS or tag in ALT_TAGS) else "N"
        
        print("<-- "+lvl+"|"+tag+"|"+valid+"|"+arg)

    #Assume properly formatted gedcom file.
    c = 0
    while c < len(gedfile):
        line = gedfile[c]
        if printflag:
            print("-->",line.rstrip())
        list_line = line.split(" ", 2)
        list_line[-1] = list_line[-1].rstrip()
        
        
        if len(list_line) > 2 and list_line[2] in ALT_TAGS:
            # If line has 3 details and the third part is in 
            
            if list_line[2] == "INDI":
                
                i = Individual()
                iIDNum = int(list_line[1][2:-1])
                i.id = iIDNum
                # loop through until we hit next INDI/FAM
                j = c + 1
                while j < len(gedfile):
                    nextline = gedfile[j]
                    next_list_line = nextline.split(" ", 2)
                    next_list_line[-1] = next_list_line[-1].rstrip()
                    if next_list_line[1] == "NAME":
                        i.name = next_list_line[2]
                    if next_list_line[1] == "SEX":
                        i.gender = next_list_line[2]
                    if next_list_line[1] == "BIRT": ## check next line to get bday
                        line2 = gedfile[j+1]
                        stuff = line2.split(" ", 2)
                        i.b_date = stuff[2]
                        
                        i.age = calc_age(stuff[2])
                    if next_list_line[1] == "DEAT":
                        i.alive = False
                        line2 = gedfile[j+1]
                        stuff = line2.split(" ", 2)
                        i.d_date = stuff[2]
                    if next_list_line[1] == "FAMC":
                        i.child_id = next_list_line[2][1:-1]
                    if next_list_line[1] == "FAMS":
                        i.spouse_id = next_list_line[2][1:-1] ## this only leads us to the family id. need to pull the spouse name from there
                    if (len(next_list_line) >= 3) and (next_list_line[2] == "INDI" or next_list_line[2] == "FAM"):
                        break
                    j+=1
                        
                indivi_objs.append(i)
            if list_line[2] == "FAM":
                f = Family()
                fIDNum = int(list_line[1][2:-1])
                f.id = fIDNum
                # loop through until we hit next INDI/FAM
                k = c + 1
                list_chil = []
                while k < len(gedfile):
                    nextline = gedfile[k]
                    next_list_line = nextline.split(" ", 2)
                    next_list_line[-1] = next_list_line[-1].rstrip()
                    if next_list_line[1] == "HUSB":
                        f.husband = int(next_list_line[2][2:-1])
                    if next_list_line[1] == "WIFE":
                        f.wife = int(next_list_line[2][2:-1])
                    if next_list_line[1] == "CHIL":
                        list_chil.append(int(next_list_line[2][2:-1]))
                        f.children = list_chil
                    if next_list_line[1] == "MARR": ## check next line to get marr day
                        line2 = gedfile[k+1]
                        stuff = line2.split(" ", 2)
                        f.mar_date = stuff[2]
                    if next_list_line[1] == "DIV": ## check next line to get marr day
                        line2 = gedfile[k+1]
                        stuff = line2.split(" ", 2)
                        f.div_date = stuff[2]
                    if (len(next_list_line) >= 3) and (next_list_line[2] == "INDI" or next_list_line[2] == "FAM"):
                        break
                    k+=1
                    
                fam_objs.append(f)
            if printflag:
                printgedline(list_line[0],list_line[2],list_line[1])
        elif printflag:
            if len(list_line) > 2:
                # Case of full line
                           
                printgedline(list_line[0],list_line[1],list_line[2])
            else:
                # Case of no args
                printgedline(list_line[0],list_line[1],"")
        c+=1
    # After while loop: Populate families with individuals

    for i in range(len(fam_objs)):
        fam = fam_objs[i]
        #Find husband
        for indiv in indivi_objs:
            # Check husband 
            if indiv.id == fam.husband:
                fam.husband = indiv
            if indiv.id == fam.wife:
                fam.wife = indiv
    


    return indivi_objs, fam_objs
           

def tableIndi(individuals):
    '''Create a PrettyTable of the individuals and print it.'''
    individuals.sort(key=lambda x: x.id)
    table = PrettyTable()
    table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for i in individuals:
        table.add_row([i.id, i.name, i.gender, i.b_date, i.age, i.alive, i.d_date, i.child_id, i.spouse_id])
    print(table)

def tableFamily(families):
    '''Create a PrettyTable of the families and print it.'''
    families.sort(key=lambda x: x.id)
    table = PrettyTable()
    table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    for f in families:
        table.add_row([f.id, f.mar_date, f.div_date, f.husband.id, f.husband.name, f.wife.id, f.wife.name, f.children])
    print(table)

def main():
    '''Run and deliver all the features of the gedparse program.'''
    filename = input("Specify GEDCOM file: ")
    printfile = input("Print lines of file? (Y/N):")
    printflag = True if (printfile == "Y" or printfile == "y") else False

    content = []
    with open(filename) as f: 
        content = f.readlines()
    content = [x.strip() for x in content]
    indivi_objs, fam_objs = readgedcom(content, printflag)
    
    tableIndi(indivi_objs)
    tableFamily(fam_objs)

    #Jerry
    us1_ind = userstory1_indivi(indivi_objs)
    us1_fam = userstory1_fam(fam_objs)
    us42_ind = userstory42_indivi(indivi_objs)
    us42_fam = userstory42_fam(fam_objs)

    us2 = userstory2(fam_objs)
    us3 = userstory3(indivi_objs)
    
    #Mark
    us10 = userstory10(fam_objs, indivi_objs)
    us11 = userstory11(fam_objs)
    us12 = userstory12(fam_objs, indivi_objs)
    us13 = userstory13(fam_objs, indivi_objs)
    
    #Nick
    us29_print(indivi_objs)
    #recent_death = Individual(i_id = 0, name = "Recent Death Testval", gender = "M", b_date = "NA", age = 0, alive = False, d_date = "15 MAR 2021", child = "NA", spouse = "NA")
    #us36_print(indivi_objs + [recent_death])
    us36_print(indivi_objs)
    us38_print(indivi_objs) # Upcoming birthdays
    us35_print(indivi_objs) # Recent births

    #Edward
    us21 = userstory21(fam_objs)
    us22_ind = userstory22_indivi(indivi_objs)
    us22_fam = userstory22_fam(fam_objs)
    us23 = userstory23(indivi_objs)
    us24 = userstory24(fam_objs)
    
    

if __name__ == "__main__":
    main() 