import unittest
from classes import *
from gedparse import *

class UserStoryTests(unittest.TestCase):

    def setUp(self):
        self.indivi_objs = []
        self.fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        self.indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "31 FEB 1990", 31, True, "NA", "NA", "NA")
        self.indivi_objs.append(i2)
        
        i3 = Individual(3, "Frank Ham", "M", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        self.indivi_objs.append(i3)
        
        i4 = Individual(4, "Samantha Ham", "F", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        self.indivi_objs.append(i4)
        
        i5 = Individual(5, "Judy Smith", "F", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        self.indivi_objs.append(i5)
        
        i6 = Individual(6, "Becky Ham", "F", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        self.indivi_objs.append(i6)
        
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [])
        self.fam_objs.append(f1)
        
        f2 = Family(2, "31 JAN 1990", "31 JAN 1993", i3, i4, [])
        self.fam_objs.append(f2)
        
        f3 = Family(3, "31 JAN 2010", "NA", i, i5, [])
        self.fam_objs.append(f3)
        
        f4 = Family(4, "31 JAN 1995", "NA", i3, i6, [])
        self.fam_objs.append(f4)

    def userstory10_1(self):
        self.assertEqual(userstory10(self.fam_objs, self.indivi_objs), True)
    
    def userstory11_1(self):
        self.assertEqual(userstory10(self.fam_objs, self.indivi_objs), True)


if __name__ == '__main__':
    unittest.main()

