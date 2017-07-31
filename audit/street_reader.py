import xml.etree.cElementTree as ET
from collections import defaultdict
import re

class Street_Reader:

    street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

    def __init__(self):
        self.street_types = []

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