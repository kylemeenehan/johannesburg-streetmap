# This class contains methods that are useful for exploring tag data
class Tag_Counter:
    def __init__(self):
        self.tags = {}
        self.tag_types = []

    def read_elem(self,elem):
        if elem.tag in self.tags:
            self.tags[elem.tag] += 1
        else:
            self.tags[elem.tag] = 1

        if elem.tag == 'tag' and elem.attrib['k'] not in self.tag_types:
            self.tag_types.append(elem.attrib['k'])

    def get_tags(self):
        return self.tags

    def print_tag_count(self):
        print "Here is a list of all the tag types, with the number of that type: \n"
        for key, value in self.tags.iteritems():
            print str(key) + ' : ' + str(value)
        print

    def print_tag_types(self):
        print "Here is a list of the differennt tag types: \n"
        self.tag_types.sort()
        for tag_type in self.tag_types:
            print tag_type
        print
    
