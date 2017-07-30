import xml.etree.cElementTree as ET
from collections import defaultdict
import re

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def extract_street_type(street_name):
    m = street_type_re.search(street_name)
    if m:
        return m.group()


def get_street_types(path):
    street_types = []
    for event, elem in ET.iterparse(path, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    street_type = extract_street_type(tag.attrib['v'])
                    if street_type not in street_types:
                        street_types.append(street_type)
    for street_type in street_types:
        print street_type
