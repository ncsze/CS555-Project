import unittest
from classes import *
from gedparse import *

class UserStoryTests(unittest.TestCase):

    def setUp(self):
        self.indivi_objs = []
        self.fam_objs = []
        i = Individual(1, "Random /Name/", "M", "10 JAN 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i)
        i2 = Individual(2, "Random /Name/", "F", "31 FEB 1990", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i2)
        i3 = Individual(3, "Random /Name/", "M", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i3)
        i4 = Individual(4, "Random /Name/", "F", "2 FEB 1980", 31, True, "NA", "NA", "NA")
        indivi_objs.append(i4)
        f1 = Family(1, "31 JAN 2000", "NA", i, i2, [])
        fam_objs.append(f1)
        f2 = Family(1, "31 JAN 1990", "NA", i3, i4, [])
        fam_objs.append(f2)
        f = Family(1, "")

    def userstory10_1(self):
        self.assertEqual(userstory10(self.fam_objs, self.indivi_objs), True)

    def userstory10_2(self):
        self.assertEqual(userstory10(self.fam_objs), False)
        


if __name__ == '__main__':
    unittest.main()

