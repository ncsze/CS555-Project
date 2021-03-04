class Individual:
    def __init__(self,i_id, name, gender, b_date, age, alive, d_date, child, spouse):
        self.id = i_id
        self.name = name
        self.gender = gender
        self.b_date = b_date
        self.age = age
        self.alive = alive
        self.d_date = d_date
        self.child = child
        self.spouse = spouse
    
    def __init__(self):
        self.id = "NA"
        self.name = "NA"
        self.gender = "NA"
        self.b_date = "NA"
        self.age = 0
        self.alive = True
        self.d_date = "NA"
        self.child = None # Should be Individual Object
        self.spouse = None # Should be Individual Object



class Family:
    def __init__(self, f_id, mar_date,div_date, husband, wife, children):
        self.id = f_id
        self.mar_date = mar_date
        self.div_date = div_date
        # Individual object type
        self.husband = husband
        # Individual object type
        self.wife = wife
        # List of ID strings
        self.children = children

    def __init__(self):
        self.id = "NA"
        self.mar_date = "NA"
        self.div_date = "NA"
        # Individual object type
        self.husband = None
        # Individual object type
        self.wife = None
        # List of ID strings
        self.children = []