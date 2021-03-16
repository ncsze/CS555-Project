import unittest
from classes import *
from gedparse import *

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
        
        f2 = Family(2, "3 FEB 1994", "31 JAN 1993", i3, i4, [])
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
        
        f1 = Family(3, "31 JAN 2000", "31 FEB 2005", i, i2, [])
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
        



if __name__ == "__main__":
    unittest.main()