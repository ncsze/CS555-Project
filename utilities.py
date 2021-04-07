from datetime import *
import datetime
from dateutil.relativedelta import *

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
    if int(d[1]) < string[1]:
        age = age - 1
    if int(d[1]) == string[1]:
        if int(d[0]) < int(string[0]):
            age = age -1 
    return age


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

# check if the date is valid or not
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
