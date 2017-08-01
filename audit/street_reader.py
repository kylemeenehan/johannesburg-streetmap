import street_cleaner as sc
import re

class Street_Reader:

    # RegEx to get the last word in a series of words under the assumption that the last word is the street type.
    street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

    def __init__(self):
        self.expected_street_types = sc.Street_Cleaner.expected_street_types
        self.street_types = []
        self.unexpected_streets = []

    # Checks whether the element passed in contains a street name
    def is_street_name(self,elem):
        return (elem.attrib['k'] == "addr:street")

    # Uses a regular expression to get the last word in a street. The assumption is that this is the street type.
    def extract_street_type(self,street_name):
        m = self.street_type_re.search(street_name)
        if m:
            return m.group()

    # Reads in an element and determines whether it's a node or a way tag
    # If it is a node or a way tag, iterates through tags and determines whether one of them is a street name
    # If it is a street name, appends the street type to the list of street names, only if it isn't there already
    # If it is not an expected street name, adds the full street name to the unexpected_streets
    def read_elem(self, elem):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if self.is_street_name(tag):
                    street_type = self.extract_street_type(tag.attrib['v'])
                    if street_type not in self.street_types:
                        self.street_types.append(street_type)
                    if street_type not in self.expected_street_types:
                        self.unexpected_streets.append(tag.attrib['v'])
    
    # Prints all of the street types found
    def print_street_types(self):
        print "Here is a list of all the street types: \n"
        self.street_types.sort()
        for street_type in self.street_types:
            print street_type
        print
    
    # Print the full name of streets that have an unexpected street name
    def print_unexpected_streets(self):
        print "Here is a list of streets with unexpected street names: \n"
        for street in self.unexpected_streets:
            print street
        print