import unittest
from classes import *
from gedparse import *

# TODO
class UserStoryTests(unittest.TestCase):

    def setUp(self):
        self.indivi_objs = []
        self.fam_objs = []
        i = Individual(1, "Random /Name/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        self.indivi_objs.append(i)
        i2 = Individual(2, "Random /Name/", "F", "31 FEB 1990", 31, True, "NA", "NA", "NA")
        self.indivi_objs.append(i2)
        i3 = Individual(3, "Random /Name/", "F", "2 FEB 1980", 31, False, "32 JAN 1990", "NA", "NA")
        self.indivi_objs.append(i3)
        f = Family(1, "32 JAN 1990", "14 MAR 2022", None, None, [])
        self.fam_objs.append(f)
    
    def test_User_Story_1I(self):
        self.assertEqual(userstory1_indivi(self.indivi_objs), False)

    def test_User_Story_1F(self):
        self.assertEqual(userstory1_indivi(self.fam_objs), True)
    
    def test_User_Story_42I(self):
        self.assertEqual(userstory42_indivi(self.indivi_objs), True)

    def test_User_Story_42F(self):
        self.assertEqual(userstory42_indivi(self.fam_objs), True)


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


if __name__ == "__main__":
    unittest.main()