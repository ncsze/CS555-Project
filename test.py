import unittest
from classes import *
from gedparse import *

# TODO
class UserStoryTests(unittest.TestCase):

    def setUp(self):
        self.indivi_objs = []
        self.fam_objs = []
        i = Individual(1, "Random /Name/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        i2 = Individual(2, "Random /Name/", "F", "31 FEB 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        i3 = Individual(3, "Random /Name/", "F", "2 FEB 1980", 31, False, "32 JAN 1990", "NA", "NA")
        indivi_objs.append(i3)
        f = Family(1, "32 JAN 1990", "14 MAR 2022", None, None, [])
        fam_objs.append(f)
    
    def test_User_Story_1I(self):
        self.assertEqual(userstory1_indivi(indivi_objs), False)

    def test_User_Story_1F(self):
        self.assertEqual(userstory1_indivi(fam_objs), True)
    
    def test_User_Story_42I(self):
        self.assertEqual(userstory42_indivi(indivi_objs), True)

    def test_User_Story_42F(self):
        self.assertEqual(userstory42_indivi(fam_objs), True)
        


if __name__ == "__main__":
    unittest.main()