# Author: Nicholas Szegheo 10440343
import sys

TAGS = ["NAME","SEX","BIRT","DEAT","FAMC","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]

ALT_TAGS = ["INDI","FAM"]

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

            printgedline(list_line[0],list_line[2],list_line[1])
        else:
            if len(list_line) > 2:
                # Case of full line
                printgedline(list_line[0],list_line[1],list_line[2])
            else:
                # Case of no args
                printgedline(list_line[0],list_line[1],"")

if __name__ == "__main__":
    try:
        filename = input("Specify GEDCOM file: ")
        readgedcom(open(filename))
    except:
        for line in sys.exc_info():
            print(line)
    input("Press Enter to continue.")