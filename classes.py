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



class Family:
    def __init__(self, f_id, mar_date,div_date, husband, wife, children):
        self.id = f_id
        self.mar_date = mar_date
        self.div_date = div_date
        # Individual type
        self.husband = husband
        # Individual type
        self.wife = wife
        # List of ID strings
        self.children = children