import xml.etree.cElementTree as ET

class Tag_Counter:
    def __init__(self):
        self.tags = {}

    def read_elem(self,elem):
        if elem.tag in self.tags:
            self.tags[elem.tag] += 1
        else:
            self.tags[elem.tag] = 1

    def get_tags(self):
        return self.tags

    def print_tag_count(self):
        for key, value in self.tags.iteritems():
            print str(key) + ' : ' + str(value)