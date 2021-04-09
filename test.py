import unittest
from classes import *
from gedparse import *
from datetime import date, timedelta

# TODO
class JYUserStoryTests(unittest.TestCase):
    
    def test_User_Story_1(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "Random /Name/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        i2 = Individual(2, "Random /Name/", "F", "31 FEB 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        i3 = Individual(3, "Random /Name/", "F", "2 FEB 1980", 31, False, "32 JAN 1990", "NA", "NA")
        indivi_objs.append(i3)
        f = Family(1, "32 JAN 1990", "14 MAR 2022", i, i2, [])
        fam_objs.append(f)


        self.assertEqual(userstory1_indivi(indivi_objs), False)
        self.assertEqual(userstory1_fam(fam_objs), True)

    
    def test_User_Story_42(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "Random /Name/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)

        self.assertEqual(userstory42_indivi(indivi_objs), False)

        i2 = Individual(2, "Random /Name/", "F", "31 FEB 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        i3 = Individual(3, "Random /Name/", "F", "2 FEB 1980", 31, False, "32 JAN 1990", "NA", "NA")
        indivi_objs.append(i3)
        f = Family(1, "32 JAN 1990", "14 MAR 2022", i, i2, [])
        fam_objs.append(f)


        self.assertEqual(userstory42_indivi(indivi_objs), True)
        self.assertEqual(userstory42_fam(fam_objs), True)
    
    def test_User_Story_2(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "Random /Name1/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        i2 = Individual(2, "Random /Name2/", "F", "1 FEB 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        i3 = Individual(3, "Random /Name3/", "F", "2 FEB 1980", 31, False, "3 JAN 1990", "NA", "NA")
        indivi_objs.append(i3)
        f = Family(1, "3 JAN 1990", "NA", i, i2, [])
        fam_objs.append(f)

        self.assertEqual(userstory2(fam_objs), True)        



    def test_User_Story_3(self):
        indivi_objs = []
        i = Individual(1, "Random /Name1/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        i2 = Individual(2, "Random /Name2/", "F", "1 FEB 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        i3 = Individual(3, "Random /Name3/", "F", "2 FEB 1980", 31, False, "31 JAN 1980", "NA", "NA")
        indivi_objs.append(i3)

        self.assertEqual(userstory3(indivi_objs), True)

    def test_User_Story_4(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "Random /Name1/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        i2 = Individual(2, "Random /Name2/", "F", "1 FEB 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        i3 = Individual(3, "Random /Name3/", "F", "2 FEB 1980", 31, False, "3 JAN 1990", "NA", "NA")
        indivi_objs.append(i3)
        f = Family(1, "3 JAN 1990", "1 JAN 1990", i, i2, [])
        fam_objs.append(f)

        self.assertEqual(userstory4(fam_objs), True)

    def test_User_Story_5(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "Random /Name1/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        i2 = Individual(2, "Random /Name2/", "F", "1 FEB 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        i3 = Individual(3, "Random /Name3/", "F", "2 FEB 1980", 31, False, "3 JAN 1981", "NA", "NA")
        indivi_objs.append(i3)
        f = Family(1, "3 JAN 1990", "1 JAN 2000", i, i3, [])
        fam_objs.append(f)

        self.assertEqual(userstory5(fam_objs), True)




class EYUserStoryTests(unittest.TestCase):
    def test_User_Story_21(self):
        indivi_objs = []
        fam_objs = []

        i1 = Individual(1, "John", "M", "NA", 20, True, "NA", "NA", "F1")
        indivi_objs.append(i1)
        i2 = Individual(2, "Emily", "F", "NA", 20, True, "NA", "NA", "F1")
        indivi_objs.append(i2)
        f1 = Family(1, "NA", "NA", i1, i2, [])
        fam_objs.append(f1)

        self.assertFalse(userstory21(fam_objs))

        i3 = Individual(3, "Walter", "F", "NA", 20, True, "NA", "NA", "F2")
        indivi_objs.append(i3)
        i4 = Individual(4, "Julia", "M", "NA", 20, True, "NA", "NA", "F2")
        indivi_objs.append(i4)
        f2 = Family(2, "NA", "NA", i3, i4, [])
        fam_objs.append(f2)

        self.assertTrue(userstory21(fam_objs))
    
    def test_User_Story_22(self):
        indivi_objs = []
        fam_objs = []

        i1 = Individual(1, "John", "M", "NA", 20, True, "NA", "NA", "F1")
        indivi_objs.append(i1)
        i2 = Individual(2, "Emily", "F", "NA", 20, True, "NA", "NA", "F1")
        indivi_objs.append(i2)
        f1 = Family(1, "NA", "NA", i1, i2, [])
        f2 = Family(f_id=2)
        fam_objs.append(f1)
        fam_objs.append(f2)

        self.assertFalse(userstory22_indivi(indivi_objs))
        self.assertFalse(userstory22_fam(fam_objs))

        i3 = Individual(i_id=2)
        indivi_objs.append(i3)
        f3 = Family(f_id=2)
        fam_objs.append(f3)

        self.assertTrue(userstory22_indivi(indivi_objs))
        self.assertTrue(userstory22_fam(fam_objs))

    def test_User_Story_23(self):
        indivi_objs = []

        i1 = Individual(1, "Johnny Test", "M", "1/2/2003", 20, True, "NA", "NA", "F1")
        indivi_objs.append(i1)
        i2 = Individual(2, "Johnny Bravo", "M", "1/2/2003", 20, True, "NA", "NA", "F2")
        indivi_objs.append(i2)
        i3 = Individual(3, "Johnny Bravo", "M", "2/2/2004", 20, True, "NA", "NA", "F3")
        indivi_objs.append(i3)

        self.assertFalse(userstory23(indivi_objs))

        i4 = Individual(4, "Johnny Test", "M", "1/2/2003", 20, True, "NA", "NA", "F4")
        indivi_objs.append(i4)

        self.assertTrue(userstory23(indivi_objs))

    def test_User_Story_24(self):
        fam_objs = []

        i1 = Individual(1, "Johnny Test", "M", "1/2/2003", 20, True, "NA", "NA", "F1")
        i2 = Individual(2, "Jennifer Test", "M", "1/2/2003", 20, True, "NA", "NA", "F1")
        f1 = Family(1, "10/10/2010", "NA", i1, i2, [])
        fam_objs.append(f1)

        i3 = Individual(3, "Johnny Bravo", "M", "1/2/2003", 20, True, "NA", "NA", "F2")
        i4 = Individual(4, "Jennifer Bravo", "M", "1/2/2003", 20, True, "NA", "NA", "F2")
        f2 = Family(2, "10/10/2010", "NA", i3, i4, [])
        fam_objs.append(f2)

        i5 = Individual(5, "Johnny Bravo", "M", "1/2/2003", 20, True, "NA", "NA", "F3")
        i6 = Individual(6, "Jennifer Bravo", "M", "1/2/2003", 20, True, "NA", "NA", "F3")
        f3 = Family(3, "2/2/2020", "NA", i5, i6, [])
        fam_objs.append(f3)

        self.assertFalse(userstory24(fam_objs))

        i7 = Individual(7, "Johnny Test", "M", "1/2/2005", 21, True, "NA", "NA", "F4")
        i8 = Individual(8, "Jennifer Test", "M", "1/2/2006", 22, True, "NA", "NA", "F4")
        f4 = Family(4, "10/10/2010", "NA", i7, i8, [])
        fam_objs.append(f4)

        self.assertTrue(userstory24(fam_objs))




class MPUserStoryTests(unittest.TestCase):
    
    def test_User_Story_10(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "31 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [])
        fam_objs.append(f1)
        
        self.assertEqual(userstory10(fam_objs, indivi_objs), True)
        
        indivi_objs = []
        fam_objs = []
        i3 = Individual(3, "Frank Ham", "M", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        i4 = Individual(4, "Samantha Ham", "F", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i4)
        
        f2 = Family(2, "1 MAR 1994", "31 JAN 1993", i3, i4, [])
        fam_objs.append(f2)
        
        self.assertEqual(userstory10(fam_objs, indivi_objs), False)
    
    def test_User_Story_11(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "31 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [])
        fam_objs.append(f1)
        
        i3 = Individual(3, "Judy Smith", "F", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        f2 = Family(2, "31 JAN 2005", "NA", i, i3, [])
        fam_objs.append(f2)
        
        self.assertEqual(userstory11(fam_objs), True)
        
        indivi_objs = []
        fam_objs = []
        i = Individual(4, "John Smith", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(5, "Jenny Smith", "F", "31 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        f1 = Family(3, "31 JAN 2000", "31 DEC 2005", i, i2, [])
        fam_objs.append(f1)
        
        i3 = Individual(6, "Judy Smith", "F", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        f2 = Family(4, "31 JAN 2005", "NA", i, i3, [])
        fam_objs.append(f2)
        #tableFamily(fam_objs)
        self.assertEqual(userstory11(fam_objs), True)
        
        indivi_objs = []
        fam_objs = []
        i = Individual(7, "John Smith", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(8, "Jenny Smith", "F", "31 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        f1 = Family(5, "31 JAN 2000", "29 JAN 2005", i, i2, [])
        fam_objs.append(f1)
        
        i3 = Individual(9, "Judy Smith", "F", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        f2 = Family(6, "30 JAN 2005", "NA", i, i3, [])
        fam_objs.append(f2)
        # tableFamily(fam_objs)
        self.assertEqual(userstory11(fam_objs), False)
        
    def test_User_Story_12(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1919", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "1 FEB 1940", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "Judy Smith", "F", "2 FEB 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [3])
        fam_objs.append(f1)
        
        # tableIndi(indivi_objs)
        # tableFamily(fam_objs)
        self.assertEqual(userstory12(fam_objs, indivi_objs), True)
        
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1919", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "1 FEB 1941", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "Judy Smith", "F", "2 FEB 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [3])
        fam_objs.append(f1)
        
        # tableIndi(indivi_objs)
        # tableFamily(fam_objs)
        self.assertEqual(userstory12(fam_objs, indivi_objs), True)
        
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "3 FEB 1940", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "Judy Smith", "F", "2 FEB 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [3])
        fam_objs.append(f1)
        
        # tableIndi(indivi_objs)
        # tableFamily(fam_objs)
        self.assertEqual(userstory12(fam_objs, indivi_objs), True)
        
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "3 FEB 1941", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "Judy Smith", "F", "2 FEB 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [3])
        fam_objs.append(f1)
        
        # tableIndi(indivi_objs)
        # tableFamily(fam_objs)
        self.assertEqual(userstory12(fam_objs, indivi_objs), False)
        
    def test_User_Story_13(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "3 FEB 1941", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "Judy Smith", "F", "2 FEB 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        i4 = Individual(4, "Brandon Smith", "M", "4 FEB 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i4)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [3, 4])
        fam_objs.append(f1)
        
        # tableIndi(indivi_objs)
        # tableFamily(fam_objs)
        self.assertEqual(userstory13(fam_objs, indivi_objs), True)
        
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "3 FEB 1941", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "Judy Smith", "F", "2 JUN 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        i4 = Individual(4, "Brandon Smith", "M", "4 FEB 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i4)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [3, 4])
        fam_objs.append(f1)
        
        # tableIndi(indivi_objs)
        # tableFamily(fam_objs)
        self.assertEqual(userstory13(fam_objs, indivi_objs), True)
        
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "3 FEB 1941", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "Judy Smith", "F", "2 FEB 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        i4 = Individual(4, "Brandon Smith", "M", "2 FEB 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i4)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [3, 4])
        fam_objs.append(f1)
        
        # tableIndi(indivi_objs)
        # tableFamily(fam_objs)
        self.assertEqual(userstory13(fam_objs, indivi_objs), False)
        
def date_to_gedstring(date_object):
    '''Helper method for testing, lets you convert datetime objects like date.today() into GEDCOM-format strings'''
    month = date_object.month
    day = date_object.day
    year = date_object.year

    switcher = {
        1: "JAN",
        2: "FEB",
        3: "MAR",
        4: "APR",
        5: "MAY",
        6: "JUN",
        7: "JUL",
        8: "AUG",
        9: "SEP",
        10: "OCT",
        11: "NOV",
        12: "DEC"
    }
    month = switcher.get(month , "Invalid month")
    return (str(day) +" "+ month +" "+ str(year))



class NSUserStoryTests(unittest.TestCase):

    def test_User_Story_29(self):
        
        individuals = []
        liveman = Individual(1, "Alive Man", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        deadman = Individual(1, "Dead Man", "M", "10 JAN 1990", 31, False, "10 JAN 2015", "NA", "NA")
        individuals.append(liveman)
        individuals.append(deadman)
        self.assertEqual(userstory29(individuals), [deadman])
    
    def test_User_Story_36(self):
        
        individuals = []
        liveman = Individual(1, "Alive Man", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        deadman = Individual(1, "Dead Man", "M", "10 JAN 1990", 31, False, "10 JAN 2015", "NA", "NA")
        recentlydeadman = Individual(1, "Recent Deadman", "M", "10 JAN 1990", 31, False, date_to_gedstring(date.today()), "NA", "NA")
        individuals.append(liveman)
        individuals.append(deadman)
        individuals.append(recentlydeadman)
        self.assertEqual(userstory36(individuals), [recentlydeadman])

    def test_User_Story_38(self):
        individuals = []
        soon = date.today() + timedelta(days=15)
        toofar = date.today() + timedelta(days=31)
        liveman = Individual(1, "Alive Man", "M", date_to_gedstring(date.today().replace(year = 1990)), 31, True, "NA", "NA", "NA")
        deadman = Individual(1, "Just Diedman", "M", date_to_gedstring(date.today().replace(year = 1990)), 31, False, "20 MAR 2021", "NA", "NA")
        soonman = Individual(1, "Cake Soonman", "M", date_to_gedstring(soon.replace(year = 1990)), 31, True, "NA", "NA", "NA")
        notsoonman = Individual(1, "Cake Laterman", "M", date_to_gedstring(toofar.replace(year = 1990)), 31, True, "NA", "NA", "NA")
        individuals.append(liveman)
        individuals.append(deadman)
        individuals.append(soonman)
        individuals.append(notsoonman)
        self.assertEqual(userstory38(individuals), [liveman,soonman])

    def test_User_Story_35(self):
        individuals = []

        today = date.today()
        tomorrow = today + timedelta(days = 1)
        yesterday = today - timedelta(days = 1)
        yesteryear = today - timedelta(days = 1, weeks = 52)
        whileago = today - timedelta(days = 45)

        tomorrowman = Individual(1, "Un Bornman", "M", date_to_gedstring(tomorrow), 0, True, "NA", "NA", "NA")
        yesterdayman = Individual(1, "Just Bornman", "M", date_to_gedstring(yesterday), 0, True, "NA", "NA", "NA")
        yesteryearman = Individual(1, "Born Longagoman", "M", date_to_gedstring(yesteryear), 1, True, "NA", "NA", "NA")
        whileagoman = Individual(1, "Borna Whileagoman", "M", date_to_gedstring(whileago), 0, True, "NA", "NA", "NA")

        individuals = [tomorrowman, yesterdayman, yesteryearman, whileagoman]

        self.assertEqual(userstory35(individuals), [yesterdayman] )
    

if __name__ == "__main__":
    unittest.main()