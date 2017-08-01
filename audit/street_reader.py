import street_cleaner as sc
import re

class Street_Reader:

    street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

    def __init__(self):
        self.expected_street_types = sc.Street_Cleaner.expected_street_types
        self.street_types = []
        self.unexpected_streets = []

    def is_street_name(self,elem):
        return (elem.attrib['k'] == "addr:street")

    def extract_street_type(self,street_name):
        m = self.street_type_re.search(street_name)
        if m:
            return m.group()


    def read_elem(self, elem):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if self.is_street_name(tag):
                    street_type = self.extract_street_type(tag.attrib['v'])
                    if street_type not in self.street_types:
                        self.street_types.append(street_type)
                    if street_type not in self.expected_street_types:
                        self.unexpected_streets.append(tag.attrib['v'])

    def print_street_types(self):
        print "Here is a list of all the street types: \n"
        self.street_types.sort()
        for street_type in self.street_types:
            print street_type
        print
    
    def print_unexpected_streets(self):
        print "Here is a list of streets with unexpected street names: \n"
        for street in self.unexpected_streets:
            print street
        print