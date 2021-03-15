class Individual:
    def __init__(self, i_id = None, name = "NA", gender = "NA", b_date = "NA", age = 0, alive = True, d_date = "NA", child = "NA", spouse = "NA"):
        self.id = i_id
        self.name = name
        self.gender = gender
        self.b_date = b_date
        self.age = age
        self.alive = alive
        self.d_date = d_date
        self.child_id = child # Should be a Family ID
        self.spouse_id = spouse # Should be a Family ID

class Family:
    def __init__(self, f_id = None, mar_date = "NA", div_date = "NA", husband = None, wife = None, children = []):
        self.id = f_id
        self.mar_date = mar_date
        self.div_date = div_date
        # Individual object type
        self.husband = husband
        # Individual object type
        self.wife = wife
        # List of ID strings
        self.children = children