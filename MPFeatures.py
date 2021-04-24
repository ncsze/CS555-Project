from utilities import *

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

def userstory12(fam_objs, indivi_objs):
    anyerrors = False
    for fam in fam_objs:
        fatherAge = 0
        motherAge = 0
        for child in fam.children:
            childAge = 0
            childName = ""
            for person in indivi_objs:
                if(fam.husband.id == person.id):
                    fatherAge = calc_age(person.b_date)
                if(fam.wife.id == person.id):
                    motherAge = calc_age(person.b_date)  
                if(child == person.id):
                    childAge = calc_age(person.b_date)
                    childName = person.name
            if(motherAge-childAge > 59 and fatherAge-childAge > 79):
                anyerrors = True
                print("WARNING: " + str(childName) + " mother is " + str(motherAge-childAge) + " years older and father is " + str(fatherAge-childAge) + " years older ")
            elif(motherAge-childAge > 59):
                anyerrors = True
                print("WARNING: " + str(childName) + " mother is " + str(motherAge-childAge) + " years older")
            elif(fatherAge-childAge > 79):
                anyerrors = True
                print("WARNING: " + str(childName) + " father is " + str(fatherAge-childAge) + " years older")
    return anyerrors

def userstory13(fam_objs, indivi_objs):
    anyerrors = False
    for fam in fam_objs:
        for i in range(0, len(fam.children)):
            for k in range(i+1, len(fam.children)):
                child1 = ""
                child2 = ""
                for person in indivi_objs:
                    if(fam.children[i] == person.id):
                        child1 = person
                    if(fam.children[k] == person.id):
                        child2 = person
                start = datetime.date(int(date_converter(child1.b_date)[2]), date_converter(child1.b_date)[1],int(date_converter(child1.b_date)[0]))
                end = datetime.date(int(date_converter(child2.b_date)[2]), date_converter(child2.b_date)[1],int(date_converter(child2.b_date)[0]))
                first = min(start,end)
                second = max(start,end)
                difference = (second-first).days
                
                months_num = 0
                while(second > first):
                    first = first + relativedelta(months=+1)
                    months_num+=1
                        
                if(difference > 1 and months_num < 9):
                    anyerrors = True
                    print("WARNING: " + child1.name + " and " + child2.name + " born to close")                   
    return anyerrors

def userstory14(fam_objs, indivi_objs):
    anyerrors = False
    for fam in fam_objs:
        for i in range(0, len(fam.children)):
            amount = 1
            for k in range(i+1, len(fam.children)):
                child1 = ""
                child2 = ""
                for person in indivi_objs:
                    if(fam.children[i] == person.id):
                        child1 = person
                    if(fam.children[k] == person.id):
                        child2 = person
                start = datetime.date(int(date_converter(child1.b_date)[2]), date_converter(child1.b_date)[1],int(date_converter(child1.b_date)[0]))
                end = datetime.date(int(date_converter(child2.b_date)[2]), date_converter(child2.b_date)[1],int(date_converter(child2.b_date)[0]))
                first = min(start,end)
                second = max(start,end)
                difference = (second-first).days
                
                if(difference < 2):
                    amount+=1
            if(amount > 5):
                anyerrors = True
                print("WARNING: " + str(amount) + " children born at the same time in family with ID " + str(fam.id))
    return anyerrors

def userstory15(fam_objs):
    anyerrors = False
    for fam in fam_objs:
        if(len(fam.children) >= 15):
            anyerrors = True
            print("WARNING: " + str(len(fam.children)) + " siblings in family with ID " + str(fam.id))
    return anyerrors

def userstory16(fam_objs, indivi_objs):
    anyerrors = False
    for fam in fam_objs:
        for childId in fam.children:
            for person in indivi_objs:
                if(childId == person.id):
                    if(not (lastName(fam.husband.name) == lastName(person.name)) and person.gender == 'M'):
                            anyerrors = True
                            print("WARNING: " + fam.husband.name + " and " + person.name + " have different last names")
    return anyerrors

def userstory17_helper(source, children, fam_objs, anyerrors):
    for child in children:
        for fam in fam_objs:
            if((child == fam.husband.id and source.id == fam.wife.id) or (child == fam.wife.id and source.id == fam.husband.id)):         
                anyerrors = True
                print("WARNING: Person of ID " + str(source.id) + " is married to their descendant, person of ID " + str(child))
            if(child == fam.husband.id or child == fam.wife.id):
                return userstory17_helper(source, fam.children, fam_objs, anyerrors)
    return anyerrors

def userstory17(fam_objs):
    anyerrors = False
    for fam in fam_objs:
        wifeError = userstory17_helper(fam.wife, fam.children, fam_objs, False)
        husbandError = userstory17_helper(fam.husband, fam.children, fam_objs, False)
        if( wifeError or husbandError ):
            anyerrors = True      
    return anyerrors
    
                    
                
                        