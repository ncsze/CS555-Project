from datetime import date
## had to copy and paste some functions from gedparse over to avoid circular dependencies 
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
                print("WARNING: Invalid birthday year", bday)
            if int(d[2]) == int(bday[2]):
                if int(d[1]) < int(bday[1]):
                    any_errors = True
                    print("WARNING: Invalid birthday year", bday)
                if int(d[1]) == int(bday[1]):
                    if int(d[0]) < int(bday[0]):
                        any_errors = True
                        print("WARNING: Invalid birthday year", bday)
        if i.d_date != "NA":
            dday = date_converter(i.d_date)
            if int(d[2]) < int(dday[2]):
                any_errors = True
                print("WARNING: Invalid death year", dday)
            if int(d[2]) == int(dday[2]):
                if int(d[1]) < int(dday[1]):
                    any_errors = True
                    print("WARNING: Invalid death year", dday)
                if int(d[1]) == int(dday[1]):
                    if int(d[0]) < int(dday[0]):
                        any_errors = True
                        print("WARNING: Invalid death year", dday)

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
                print("WARNING: Invalid marriage year", mday)
            if int(d[2]) == int(mday[2]):
                if int(d[1]) < int(mday[1]):
                    any_errors = True
                    print("WARNING: Invalid marriage year", mday)
                if int(d[1]) == int(mday[1]):
                    if int(d[0]) < int(mday[0]):
                        any_errors = True
                        print("WARNING: Invalid marriage year", mday)
        if f.div_date != "NA":
            diday = date_converter(f.div_date)
            if int(d[2]) < int(diday[2]):
                any_errors = True
                print("WARNING: Invalid divorce year", diday)
            if int(d[2]) == int(diday[2]):
                if int(d[1]) < int(diday[1]):
                    any_errors = True
                    print("WARNING: Invalid divorce year", diday)
                if int(d[1]) == int(diday[1]):
                    if int(d[0]) < int(diday[0]):
                        any_errors = True
                        print("WARNING: Invalid divorce year", diday)

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

def userstory42_indivi(indivi_objs):
    any_errors = False
    for i in indivi_objs:
        bday = ""
        dday = ""
        if i.b_date != "NA":
            bday = date_converter(i.b_date)
            if date_check(bday) == True:
                any_errors = True
                print("WARNING: Invalid birthday date", bday)

        if i.d_date != "NA":
            dday = date_converter(i.d_date)
            if date_check(dday) == True:
                any_errors = True
                print("WARNING: Invalid death date", dday)
    
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
                print("WARNING: Invalid marriage date", mday)


        if f.div_date != "NA":
            diday = date_converter(f.div_date)
            if date_check(diday) == True:
                any_errors = True
                print("WARNING: Invalid divorce date", diday)
    return any_errors

# check if date 1 occurs before date 2 return false if it doesn't
def compare_dates(date1, date2):
    valid = True
    if int(date1[2]) > int(date2[2]):
        valid = False
    if int(date1[2]) == int(date2[2]):
        if int(date1[1]) > int(date2[1]):
            valid = False
        if int(date1[1]) == int(date2[1]):
            if int(date1[0]) > int(date2[0]):
                valid = False

    return valid


def userstory2(fam_objs):
    any_errors = False
    for f in fam_objs:
        bday_husband = ""
        bday_wife = ""
        mday = ""

        if f.mar_date != "NA":
            mday = date_converter(f.mar_date)
        
        bday_husband = date_converter(f.husband.b_date)
        bday_wife = date_converter(f.wife.b_date)

        if mday != "" and bday_husband != "" and bday_wife != "":
            if compare_dates(bday_husband, mday) == False:
                any_errors = True
                print("WARNING: Marriage of " + f.husband.name + " occurs before birth.")
            
            if compare_dates(bday_wife, mday) == False:
                any_errors = True
                print("WARNING: Marriage of " + f.wife.name + " occurs before birth.")

    return any_errors

def userstory3(indivi_objs):
    any_errors = False
    for i in indivi_objs:
        bday = ""
        dday = ""
        if i.b_date != "NA":
            bday = date_converter(i.b_date)

        if i.d_date != "NA":
            dday = date_converter(i.d_date)
        
        if bday != "" and dday != "":
            if compare_dates(bday, dday) == False:
                any_errors = True
                print("WARNING: Death of individual " + i.name + " occurs before birth.")

    return any_errors



