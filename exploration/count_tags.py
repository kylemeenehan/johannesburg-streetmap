import xml.etree.cElementTree as ET

def count_tags(file):
    tags = {}
    for event, elem in ET.iterparse(file):
        if elem.tag in tags:
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    return tags