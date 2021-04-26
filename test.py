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


        self.assertEqual(dates_before_current_date_indivi(indivi_objs), False)
        self.assertEqual(dates_before_current_date_fam(fam_objs), True)

    
    def test_User_Story_42(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "Random /Name/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)

        self.assertEqual(reject_illegitimate_dates_indivi(indivi_objs), False)

        i2 = Individual(2, "Random /Name/", "F", "31 FEB 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        i3 = Individual(3, "Random /Name/", "F", "2 FEB 1980", 31, False, "32 JAN 1990", "NA", "NA")
        indivi_objs.append(i3)
        f = Family(1, "32 JAN 1990", "14 MAR 2022", i, i2, [])
        fam_objs.append(f)


        self.assertEqual(reject_illegitimate_dates_indivi(indivi_objs), True)
        self.assertEqual(reject_illegitimate_dates_fam(fam_objs), True)
    
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

        self.assertEqual(birth_before_marriage(fam_objs), True)        



    def test_User_Story_3(self):
        indivi_objs = []
        i = Individual(1, "Random /Name1/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        i2 = Individual(2, "Random /Name2/", "F", "1 FEB 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        i3 = Individual(3, "Random /Name3/", "F", "2 FEB 1980", 31, False, "31 JAN 1980", "NA", "NA")
        indivi_objs.append(i3)

        self.assertEqual(birth_before_death(indivi_objs), True)

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

        self.assertEqual(marriage_before_divorce(fam_objs), True)

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

        self.assertEqual(marriage_before_death(fam_objs), True)

    def test_User_Story_6(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "Random /Name1/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        i2 = Individual(2, "Random /Name2/", "F", "1 FEB 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        i3 = Individual(3, "Random /Name3/", "F", "2 FEB 1960", 31, False, "3 JAN 1981", "NA", "NA")
        indivi_objs.append(i3)
        f = Family(1, "3 JAN 1980", "1 JAN 2000", i, i3, [])
        fam_objs.append(f)

        self.assertEqual(divorce_before_death(fam_objs), True)
    
    def test_User_Story_7(self):
        indivi_objs = []
        i = Individual(1, "Random /Name1/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)

        self.assertEqual(less_than_150(indivi_objs), False)

        i2 = Individual(2, "Random /Name2/", "F", "1 FEB 1800", 221, True, "NA", "NA", "NA")
        indivi_objs.append(i2)

        i2 = Individual(2, "Random /Name3/", "F", "1 FEB 1850", 171, True, "NA", "NA", "NA")
        indivi_objs.append(i2)

        self.assertEqual(less_than_150(indivi_objs), True)
    


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

        self.assertFalse(correctGender(fam_objs))

        i3 = Individual(3, "Walter", "F", "NA", 20, True, "NA", "NA", "F2")
        indivi_objs.append(i3)
        i4 = Individual(4, "Julia", "M", "NA", 20, True, "NA", "NA", "F2")
        indivi_objs.append(i4)
        f2 = Family(2, "NA", "NA", i3, i4, [])
        fam_objs.append(f2)

        self.assertTrue(correctGender(fam_objs))
    
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

        self.assertFalse(uniqueID_indivi(indivi_objs))
        self.assertFalse(uniqueID_fam(fam_objs))

        i3 = Individual(i_id=2)
        indivi_objs.append(i3)
        f3 = Family(f_id=2)
        fam_objs.append(f3)

        self.assertTrue(uniqueID_indivi(indivi_objs))
        self.assertTrue(uniqueID_fam(fam_objs))

    def test_User_Story_23(self):
        indivi_objs = []

        i1 = Individual(1, "Johnny Test", "M", "1/2/2003", 20, True, "NA", "NA", "F1")
        indivi_objs.append(i1)
        i2 = Individual(2, "Johnny Bravo", "M", "1/2/2003", 20, True, "NA", "NA", "F2")
        indivi_objs.append(i2)
        i3 = Individual(3, "Johnny Bravo", "M", "2/2/2004", 20, True, "NA", "NA", "F3")
        indivi_objs.append(i3)

        self.assertFalse(uniqueNameAndBDay(indivi_objs))

        i4 = Individual(4, "Johnny Test", "M", "1/2/2003", 20, True, "NA", "NA", "F4")
        indivi_objs.append(i4)

        self.assertTrue(uniqueNameAndBDay(indivi_objs))

    def test_User_Story_24(self):
        fam_objs = []

        i1 = Individual(1, "Johnny Test", "M", "1/2/2003", 20, True, "NA", "NA", "F1")
        i2 = Individual(2, "Jennifer Test", "F", "1/2/2003", 20, True, "NA", "NA", "F1")
        f1 = Family(1, "10/10/2010", "NA", i1, i2, [])
        fam_objs.append(f1)

        i3 = Individual(3, "Johnny Bravo", "M", "1/2/2003", 20, True, "NA", "NA", "F2")
        i4 = Individual(4, "Jennifer Bravo", "F", "1/2/2003", 20, True, "NA", "NA", "F2")
        f2 = Family(2, "10/10/2010", "NA", i3, i4, [])
        fam_objs.append(f2)

        i5 = Individual(5, "Johnny Bravo", "M", "1/2/2003", 20, True, "NA", "NA", "F3")
        i6 = Individual(6, "Jennifer Bravo", "F", "1/2/2003", 20, True, "NA", "NA", "F3")
        f3 = Family(3, "2/2/2020", "NA", i5, i6, [])
        fam_objs.append(f3)

        self.assertFalse(uniqueFamilies(fam_objs))

        i7 = Individual(7, "Johnny Test", "M", "1/2/2005", 21, True, "NA", "NA", "F4")
        i8 = Individual(8, "Jennifer Test", "F", "1/2/2006", 22, True, "NA", "NA", "F4")
        f4 = Family(4, "10/10/2010", "NA", i7, i8, [])
        fam_objs.append(f4)

        self.assertTrue(uniqueFamilies(fam_objs))

    def test_User_Story_25(self):
        indivi_objs = []
        fam_objs = []

        i1 = Individual(1, "Johnny Test", "M", "1/2/2003", 20, True, "NA", "NA", "F1")
        i2 = Individual(2, "Jennifer Test", "F", "1/2/2003", 20, True, "NA", "NA", "F1")
        i3 = Individual(3, "Child1", "M", "2/3/2004", 2, True, "NA", "NA", "F1")
        i4 = Individual(4, "Child2", "F", "2/3/2004", 2, True, "NA", "NA", "F1")
        f1 = Family(1, "10/10/2010", "NA", i1, i2, [3,4])
        fam_objs.append(f1)

        i5 = Individual(5, "Johnny Bravo", "M", "1/2/2003", 20, True, "NA", "NA", "F2")
        i6 = Individual(6, "Jennifer Bravo", "F", "1/2/2003", 20, True, "NA", "NA", "F2")
        i7 = Individual(7, "Child1", "M", "2/3/2004", 2, True, "NA", "NA", "F2")
        i8 = Individual(8, "Child2", "F", "5/6/2011", 10, True, "NA", "NA", "F2")
        f2 = Family(2, "10/10/2010", "NA", i5, i6, [7,8])
        fam_objs.append(f2)

        i9 = Individual(9, "John B", "M", "1/2/2003", 20, True, "NA", "NA", "F3")
        i10 = Individual(10, "Jen B", "F", "1/2/2003", 20, True, "NA", "NA", "F3")
        i11 = Individual(11, "Child1", "M", "2/3/2004", 2, True, "NA", "NA", "F3")
        i12 = Individual(12, "Child1", "F", "5/6/2011", 10, True, "NA", "NA", "F3")
        f3 = Family(3, "10/10/2010", "NA", i9, i10, [11,12])
        fam_objs.append(f3)
        indivi_objs.extend([i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12])

        self.assertFalse(uniqueFirstName(indivi_objs, fam_objs))

        i13 = Individual(13, "Johnny B", "M", "1/2/2003", 20, True, "NA", "NA", "F4")
        i14 = Individual(14, "Jenny B", "F", "1/2/2003", 20, True, "NA", "NA", "F4")
        i15 = Individual(15, "Child1", "M", "2/3/2004", 2, True, "NA", "NA", "F4")
        i16 = Individual(16, "Child1", "F", "2/3/2004", 2, True, "NA", "NA", "F4")
        f4 = Family(4, "10/10/2010", "NA", i13, i14, [15,16])
        fam_objs.append(f4)
        indivi_objs.extend([i13,i14,i15,i16])

        self.assertTrue(uniqueFirstName(indivi_objs, fam_objs))

    def test_User_Story_30(self):
        fam_objs = []

        i1 = Individual(1, "Johnny Test", "M", "1/2/2003", 20, True, "NA", "NA", "F1")
        i2 = Individual(2, "Jennifer Test", "F", "1/2/2003", 20, True, "NA", "NA", "F1")
        f1 = Family(1, "10/10/2010", "NA", i1, i2, [])
        fam_objs.append(f1)

        i3 = Individual(3, "Johnny Bravo", "M", "1/2/2003", 20, False, "NA", "NA", "F2")
        i4 = Individual(4, "Jennifer Bravo", "F", "1/2/2003", 20, True, "NA", "NA", "F2")
        f2 = Family(2, "10/10/2010", "NA", i3, i4, [])
        fam_objs.append(f2)

        i5 = Individual(5, "John B", "M", "1/2/2003", 20, True, "NA", "NA", "F3")
        i6 = Individual(6, "Jen B", "F", "1/2/2003", 20, True, "NA", "NA", "F3")
        f3 = Family(3, "10/10/2010", "10/10/2020", i5, i6, [])
        fam_objs.append(f3)

        i7 = Individual(7, "John B", "M", "1/2/2003", 20, False, "NA", "NA", "F4")
        i8 = Individual(8, "Jen B", "F", "1/2/2003", 20, False, "NA", "NA", "F4")
        f4 = Family(4, "10/10/2010", "NA", i7, i8, [])
        fam_objs.append(f4)

        self.assertEqual(livingMarried(fam_objs), [i1,i2,i4])

    def test_User_Story_31(self):
        indivi_objs = []
        fam_objs = []

        i1 = Individual(1, "John Smith", "M", "1/1/2000", 31, True, "NA", "NA", "NA")
        i2 = Individual(2, "John B", "M", "1/1/2000", 30, True, "NA", "NA", "NA")
        i3 = Individual(3, "John C", "M", "1/1/2000", 50, False, "NA", "NA", "NA")
        i4 = Individual(4, "John C", "M", "1/1/2000", 50, True, "NA", "NA", "F1")

        i5 = Individual(5, "John D", "M", "1/1/2000", 45, True, "NA", "NA", "NA")
        i6 = Individual(6, "Jessica D", "F", "1/1/2000", 44, True, "NA", "NA", "NA")

        indivi_objs.extend([i1,i2,i3,i4,i5,i6])
        self.assertEqual(livingSingle(indivi_objs, fam_objs), [i1,i5,i6])

        f2 = Family(2, "2/2/2002", "3/3/2003", i5, i6, [])
        fam_objs.append(f2)

        self.assertEqual(livingSingle(indivi_objs, fam_objs), [i1])

    def test_User_Story_32(self):
        fam_objs = []

        i1 = Individual(1, "Child1", "M", "4/4/2000", 21, True, "NA", "NA", "NA")
        i2 = Individual(2, "Child2", "M", "4/3/2000", 21, True, "NA", "NA", "NA")
        i3 = Individual(3, "Child3", "M", "4/5/2000", 21, True, "NA", "NA", "NA")
        i4 = Individual(4, "Child4", "M", "7/7/2000", 20, True, "NA", "NA", "NA")

        f1 = Family(1, "NA", "NA", None, None, [i1,i2,i3,i4])
        fam_objs.append(f1)

        i5 = Individual(5, "Child5", "M", "1/1/2000", 21, True, "NA", "NA", "NA")

        f2 = Family(2, "NA", "NA", None, None, [i5])
        fam_objs.append(f2)

        i6 = Individual(6, "Child6", "M", "3/3/2000", 21, True, "NA", "NA", "NA")
        i7 = Individual(7, "Child7", "M", "3/2/2000", 21, True, "NA", "NA", "NA")

        f3 = Family(3, "NA", "NA", None, None, [i6,i7])
        fam_objs.append(f3)

        self.assertEqual(multipleBirths(fam_objs), [i2,i1,i3,i7,i6])


        




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
        
        self.assertEqual(marriage_after_14(fam_objs, indivi_objs), True)
        
        indivi_objs = []
        fam_objs = []
        i3 = Individual(3, "Frank Ham", "M", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        i4 = Individual(4, "Samantha Ham", "F", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i4)
        
        f2 = Family(2, "1 MAR 1994", "31 JAN 1993", i3, i4, [])
        fam_objs.append(f2)
        
        self.assertEqual(marriage_after_14(fam_objs, indivi_objs), False)
    
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
        
        self.assertEqual(no_bigamy(fam_objs), True)
        
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
        self.assertEqual(no_bigamy(fam_objs), True)
        
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
        self.assertEqual(no_bigamy(fam_objs), False)
        
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
        self.assertEqual(parents_age_check(fam_objs, indivi_objs), True)
        
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
        self.assertEqual(parents_age_check(fam_objs, indivi_objs), True)
        
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
        self.assertEqual(parents_age_check(fam_objs, indivi_objs), True)
        
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
        self.assertEqual(parents_age_check(fam_objs, indivi_objs), False)
        
    def test_User_Story_13(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "3 FEB 1941", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "Judy Smith", "F", "31 DEC 1999", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        i4 = Individual(4, "Brandon Smith", "M", "2 JAN 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i4)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [3, 4])
        fam_objs.append(f1)
        
        # tableIndi(indivi_objs)
        # tableFamily(fam_objs)
        self.assertEqual(siblings_spaced(fam_objs, indivi_objs), True)
        
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "3 FEB 1941", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "Judy Smith", "F", "2 NOV 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        i4 = Individual(4, "Brandon Smith", "M", "4 FEB 2001", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i4)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [3, 4])
        fam_objs.append(f1)
        
        # tableIndi(indivi_objs)
        # tableFamily(fam_objs)
        self.assertEqual(siblings_spaced(fam_objs, indivi_objs), True)
        
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "Jenny Smith", "F", "3 FEB 1941", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "Judy Smith", "F", "2 JAN 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        i4 = Individual(4, "Brandon Smith", "M", "10 SEP 2000", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i4)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [3, 4])
        fam_objs.append(f1)
        
        # tableIndi(indivi_objs)
        # tableFamily(fam_objs)
        self.assertEqual(siblings_spaced(fam_objs, indivi_objs), False)
    
    def test_User_Story_14(self):
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        i4 = Individual(4, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i4)
        
        i5 = Individual(5, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i5)
        
        i6 = Individual(6, "John Smith", "M", "12 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i6)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [1, 2, 3, 4, 5, 6])
        fam_objs.append(f1)
        
        self.assertEqual(multiple_births(fam_objs, indivi_objs), False)
        
        indivi_objs = []
        fam_objs = []
        i = Individual(1, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "John Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        i4 = Individual(4, "John Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i4)
        
        i5 = Individual(5, "John Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i5)
        
        i6 = Individual(6, "John Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i6)
        
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [1, 2, 3, 4, 5, 6])
        fam_objs.append(f1)
        
        self.assertEqual(multiple_births(fam_objs, indivi_objs), True)
    
    def test_User_Story_15(self):
        fam_objs = []
        
        f1 = Family(1, "31 JAN 2000", "NA", "i", "i2", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        fam_objs.append(f1)
        
        self.assertEqual(siblings_check(fam_objs), False)
        
        fam_objs = []
        
        f1 = Family(1, "31 JAN 2000", "NA", "i", "i2", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        fam_objs.append(f1)
        
        self.assertEqual(siblings_check(fam_objs), True)
    
    def test_User_Story_16(self):
        fam_objs = []
        indivi_objs = []
        
        husband = Individual(5, "John Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        f1 = Family(1, "31 JAN 2000", "NA", husband, "i2", [1, 2, 3])
        fam_objs.append(f1)
        
        i = Individual(1, "James Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        
        i2 = Individual(2, "John Pitt", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        
        i3 = Individual(3, "Brandon Harry Smith", "M", "10 JAN 1921", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        
        self.assertEqual(male_last_name(fam_objs, indivi_objs), True)
        
    def test_User_Story_17(self):
        fam_objs = []
        
        husband = Individual(5, "John Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        wife = Individual(4, "Mary Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        f1 = Family(1, "31 JAN 2000", "NA", husband, wife, [1, 2, 3])
        fam_objs.append(f1)
        
        husband = Individual(2, "Abe Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        wife = Individual(8, "Mary Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        f2 = Family(2, "31 JAN 2000", "NA", husband, wife, [10, 20, 30])
        fam_objs.append(f2)
        
        self.assertEqual(marriage_to_descendant(fam_objs), False)
        
        fam_objs = []
        
        husband = Individual(5, "John Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        wife = Individual(4, "Mary Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        f1 = Family(1, "31 JAN 2000", "NA", husband, wife, [1, 2, 3])
        fam_objs.append(f1)
        
        husband = Individual(2, "Abe Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        wife = Individual(4, "Mary Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        f2 = Family(2, "31 JAN 2000", "NA", husband, wife, [10, 20, 30])
        fam_objs.append(f2)
        
        husband = Individual(5, "John Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        wife = Individual(10, "Jenny Smith", "M", "11 JAN 1921", 31, True, "NA", "NA", "NA")
        f3 = Family(3, "31 JAN 2000", "NA", husband, wife, [100, 200, 300])
        fam_objs.append(f3)
        
        self.assertEqual(marriage_to_descendant(fam_objs), True)
        
        
        
        
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

    def test_User_Story_33(self):
        indivs = []
        fams = []
        # Living Family with young child
        f1 = Family(1, "NA", "NA", None, None, [3])
        n1 = Individual (1, "Dad Liveman", "M", "NA", 40, True, "NA", "NA", "F1")
        n2 = Individual (2, "Mom Liveman", "F", "NA", 37, True, "NA", "NA", "F1")
        n3 = Individual (3, "Son Liveman", "M", "NA", 7, True, "NA", "F1", "NA")
        f1.husband = n1
        f1.wife = n2
        indivs += [n1,n2,n3]
        fams += [f1]

        # Orphan Family with adult and young child
        f2 = Family(2, "NA", "NA", None, None, [6,7])
        o1 = Individual (4, "Dad Deadman", "M", "NA", 40, False, "NA", "NA", "F2")
        o2 = Individual (5, "Mom Deadman", "F", "NA", 37, False, "NA", "NA", "F2")
        o3 = Individual (6, "Sonny Deadman", "M", "NA", 7, True, "NA", "F2", "NA")
        o4 = Individual (7, "Grown Deadman", "M", "NA", 18, True, "NA", "F2", "NA")
        f2.husband = o1
        f2.wife = o2
        indivs += [o1, o2, o3, o4]
        fams += [f2]

        self.assertEqual(userstory33(indivs, fams), [o3])

    def test_User_Story_37(self):

        indivs = []
        fams = []
        # Living Family with young child
        f1 = Family(1, "NA", "NA", None, None, [3])
        n1 = Individual (1, "Dad Liveman", "M", "20 MAR 1981", 40, True, "NA", "NA", "F1")
        n2 = Individual (2, "Mom Liveman", "F", "10 MAR 1984", 37, True, "NA", "NA", "F1")
        n3 = Individual (3, "Son Liveman", "M", "1 MAR 2014", 7, True, "NA", "F1", "NA")
        f1.husband = n1
        f1.wife = n2
        indivs += [n1,n2,n3]
        fams += [f1]

        f2 = Family(2, "NA", "NA", None, None, [6])
        o1 = Individual (4, "Recent Deadman", "M", "10 JAN 1990", 31, False, date_to_gedstring(date.today()), "NA", "F2")
        o2 = Individual (5, "Wifey Deadman", "F", "10 JAN 1990", 31, True, "NA", "NA", "F2")
        o3 = Individual (6, "Sonny Deadman", "M", "NA", 7, True, "NA", "F2", "NA")
        f2.husband = o1
        f2.wife = o2
        indivs += [o1, o2, o3]
        fams += [f2]
        
        self.assertEqual(userstory37(indivs, fams), [o2,o3])
    

if __name__ == "__main__":
    unittest.main()