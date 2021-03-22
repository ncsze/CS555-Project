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
                   if married[1] < birthday[1]:
                       age = age - 1
                   if married[1] == birthday[1]:
                        if int(married[0]) < int(birthday[0]):
                            age = age - 1 
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
    
    if(date2[1] < date1[1]):
        return date2
    if(date2[1] > date1[1]):
        return date1
    
    if(date2[0] < date1[0]):
        return date2
    if(date2[0] > date1[0]):
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
                        print("WARNING: Family " + str(fam_objs[fam].id) + " and Family " + str(fam_objs[check].id) + " married at the same time")
                    else:
                        div_or_mar = date_compare(date_converter(fam2Marriage.mar_date), date_converter(fam1Marriage.div_date))
                        if date_converter(fam2Marriage.mar_date) == div_or_mar:
                            anyerrors = True
                            print("WARNING: Family " + str(fam_objs[fam].id) + " and Family " + str(fam_objs[check].id) + " married at the same time")
    return anyerrors