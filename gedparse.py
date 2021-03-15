# Author: Nicholas Szegheo 10440343
import sys
from datetime import date
from classes import *
from prettytable import PrettyTable
from EYFeatures import *



TAGS = ["NAME","SEX","BIRT","DEAT","FAMC","FAMS","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]

ALT_TAGS = ["INDI","FAM"]

def date_converter(string):
    string = string.split()
    if string[1] == "JAN":
        string[1] = 1
    if string[1] == "FEB":
        string[1] = 2
    if string[1] == "MAR":
        string[1] = 3
    if string[1] == "APR":
        string[1] = 4
    if string[1] == "MAY":
        string[1] = 5
    if string[1] == "JUN":
        string[1] = 6
    if string[1] == "JUL":
        string[1] = 7
    if string[1] == "AUG":
        string[1] = 8
    if string[1] == "SEP":
        string[1] = 9
    if string[1] == "OCT":
        string[1] = 10
    if string[1] == "NOV":
        string[1] = 11
    if string[1] == "DEC":
        string[1] = 12
    return string

def calc_age(string):
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    d = today.split("/")
    string = date_converter(string)
    age = 0
    age += int(d[2]) - int(string[2])
    if int(d[1]) > string[1]:
        age = age - 1
    if int(d[1]) == string[1]:
        if int(d[0]) > int(string[0]):
            age = age -1 
    return age

def userstory1_indivi(indivi_objs):
    any_errors = False
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    d = today.split("/")
    for i in indivi_objs:
        bday = ""
        dday = ""
        if i.b_date != "NA":
            bday = date_converter(i.b_date) 
            if int(d[2]) < int(bday[2]):
                any_errors = True
                print("Invalid birthday year", bday)
            if int(d[2]) == int(bday[2]):
                if int(d[1]) < int(bday[1]):
                    any_errors = True
                    print("Invalid birthday year", bday)
                if int(d[1]) == int(bday[1]):
                    if int(d[0]) < int(bday[0]):
                        any_errors = True
                        print("Invalid birthday year", bday)
        if i.d_date != "NA":
            dday = date_converter(i.d_date)
            if int(d[2]) < int(dday[2]):
                any_errors = True
                print("Invalid death year", dday)
            if int(d[2]) == int(dday[2]):
                if int(d[1]) < int(dday[1]):
                    any_errors = True
                    print("Invalid death year", dday)
                if int(d[1]) == int(dday[1]):
                    if int(d[0]) < int(dday[0]):
                        any_errors = True
                        print("Invalid death year", dday)

    return any_errors


def userstory1_fam(fam_objs):
    any_errors = False
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    d = today.split("/")
    for f in fam_objs:
        mday = ""
        diday = ""
        if f.mar_date != "NA":
            mday = date_converter(f.mar_date) 
            if int(d[2]) < int(mday[2]):
                any_errors = True
                print("Invalid marriage year", mday)
            if int(d[2]) == int(mday[2]):
                if int(d[1]) < int(mday[1]):
                    any_errors = True
                    print("Invalid marriage year", mday)
                if int(d[1]) == int(mday[1]):
                    if int(d[0]) < int(mday[0]):
                        any_errors = True
                        print("Invalid marriage year", mday)
        if f.div_date != "NA":
            diday = date_converter(f.div_date)
            if int(d[2]) < int(diday[2]):
                any_errors = True
                print("Invalid divorce year", diday)
            if int(d[2]) == int(diday[2]):
                if int(d[1]) < int(diday[1]):
                    any_errors = True
                    print("Invalid divorce year", diday)
                if int(d[1]) == int(diday[1]):
                    if int(d[0]) < int(diday[0]):
                        any_errors = True
                        print("Invalid divorce year", diday)

    return any_errors

def date_check(string):
    error = False
    if int(string[0]) <= 0 or int(string[1]) <= 0 or int(string[2]) <= 0:
        error = True

    if int(string[1]) == 1 or int(string[1]) == 3 or int(string[1]) == 5 or int(string[1]) == 7 or int(string[1]) == 8 or int(string[1]) == 10 or int(string[1]) == 12:
        if int(string[0]) > 31:
            error = True

    if int(string[1]) == 4 or int(string[1]) == 6 or int(string[1]) == 9 or int(string[1]) == 11:
        if int(string[0]) > 30:
            error = True
            
    if int(string[1]) == 2 and int(string[2]) % 4 == 0:
        if int(string[0]) > 29:
            error = True
            
    if int(string[1]) == 2 and int(string[2]) % 4 != 0:
        if int(string[0]) > 28:
            error = True

    return error

def userstory42_indivi(indiv_objs):
    any_errors = False
    for i in indiv_objs:
        bday = ""
        dday = ""
        if i.b_date != "NA":
            bday = date_converter(i.b_date)
            if date_check(bday) == True:
                any_errors = True
                print("Invalid birthday date", bday)

        if i.d_date != "NA":
            dday = date_converter(i.d_date)
            if date_check(dday) == True:
                any_errors = True
                print("Invalid death date", dday)
    
    return any_errors

def userstory42_fam(fam_objs):
    any_errors = False
    for f in fam_objs:
        mday = ""
        diday = ""
        if f.mar_date != "NA":
            mday = date_converter(f.mar_date)
            if date_check(mday) == True:
                any_errors = True
                print("Invalid marriage date", mday)


        if f.div_date != "NA":
            diday = date_converter(f.div_date)
            if date_check(diday) == True:
                any_errors = True
                print("Invalid divorce date", diday)
    return any_errors

def userstory10(fam_objs, indivi_objs):
    anyerrors = False
    for fam in fam_objs:
        for indiv in indivi_objs:
            if(fam.husband.id == indiv.id or fam.wife.id == indiv.id):
               if(fam.mar_date != "NA"):
                   married = date_converter(fam.mar_date) 
                   birthday = date_converter(indiv.b_date)
                   age = 0
                   age += int(married[2]) - int(birthday[2])
                   if married[1] > birthday[1]:
                       age = age - 1
                   if married[1] == birthday[1]:
                        if int(married[0]) > int(birthday[0]):
                            age = age -1 
                   if age < 14:
                       anyerrors = True
                       print("WARNING: " + indiv.name + " was married before 14")
    return anyerrors


def date_compare(date1,date2):
    #Returns older date
    if(date2[2] < date1[2]):
        return date2
    if(date2[2] > date1[2]):
        return date1
    
    if(date2[1] > date1[1]):
        return date2
    if(date2[1] < date1[1]):
        return date1
    
    if(date2[1] < date1[1]):
        return date2
    if(date2[1] > date1[1]):
        return date1


def userstory11(fam_objs):
    anyerrors = False
    for fam in range(len(fam_objs)-1):
        for check in range(fam+1, len(fam_objs)):
            if(fam_objs[fam].mar_date != "NA" and fam_objs[check].mar_date != "NA"):
                
                if(fam_objs[fam].husband.id == fam_objs[check].husband.id or fam_objs[fam].wife.id == fam_objs[check].wife.id):               
                    fam1Marriage = date_converter(fam_objs[fam].mar_date)
                    fam2Marriage = date_converter(fam_objs[check].mar_date)
                    
                    first_marriage = date_compare(fam1Marriage, fam2Marriage)
                    if(fam1Marriage == first_marriage):
                        fam1Marriage = fam_objs[fam]
                        fam2Marriage = fam_objs[check]
                    else:
                        fam1Marriage = fam_objs[check]
                        fam2Marriage = fam_objs[fam]
                      
                    if fam1Marriage.div_date == "NA":
                        anyerrors = True
                        print("WARNING: " + str(fam_objs[fam].id) + " and " + str(fam_objs[check].id) + " married at the same time")
                    else:
                        div_or_mar = date_compare(fam2Marriage, date_converter(fam1Marriage.div_date))
                        if fam2Marriage == div_or_mar:
                            anyerrors = True
                            print("WARNING: " + str(fam_objs[fam].id) + " and " + str(fam_objs[check].id) + " married at the same time")
    return anyerrors
    

def readgedcom(gedfile, printflag):
    '''Iterates through a GEDCOM file contents in array gedfile, returning formatted output
    showing various information, including if the tag is valid.'''
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
    individuals.sort(key=lambda x: x.id)
    table = PrettyTable()
    table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for i in individuals:
        table.add_row([i.id, i.name, i.gender, i.b_date, i.age, i.alive, i.d_date, i.child_id, i.spouse_id])
    print(table)

def tableFamily(families):
    families.sort(key=lambda x: x.id)
    table = PrettyTable()
    table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    for f in families:
        table.add_row([f.id, f.mar_date, f.div_date, f.husband.id, f.husband.name, f.wife.id, f.wife.name, f.children])
    print(table)

if __name__ == "__main__":

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

    o1 = userstory1_indivi(indivi_objs)
    o1_1 = userstory1_fam(fam_objs)
    o42 = userstory42_indivi(indivi_objs)
    o42_1 = userstory42_fam(fam_objs)

    #print(o1,o1_1,o42,o42_1)
    
    us10 = userstory10(fam_objs, indivi_objs)
    us11 = userstory11(fam_objs)
    
    #print(us10, us11)