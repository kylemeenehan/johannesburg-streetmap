class City_Reader:

    def __init__(self):
        self.cities = []

    # Checks whether the element passed in is a city
    def is_city(self,elem):
        return (elem.attrib['k'] == "addr:city")


    # Reads in an element and determines whether it's a node or a way tag
    # If it is a node or a way tag, iterates through tags and determines whether one of them is a place
    def read_elem(self, elem):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if self.is_city(tag):
                    city = tag.attrib['v']
                    if city not in self.cities:
                        self.cities.append(city)
    
    # Prints all of the cites types found
    def print_cities(self):
        print "Here is a list of all the cites: \n"
        self.cities.sort()
        for city in self.cities:
            print city
        print
    
    def print_num_cities(self):
        print "There are "  + str(len(self.cities)) + "cities."