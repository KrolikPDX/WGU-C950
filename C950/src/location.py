#Joseph Demyanovskiy 001208427

class Location(object):
    def __str__(self):
        return '[{}, {}, {}]'.format(self.name, self.street, self.city)

    def __init__(self, name, street, city, state, zip_code): #add graph index
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
