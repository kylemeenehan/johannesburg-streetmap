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
        print "Here is a list of all the tag types, with the number of that type: \n"
        for key, value in self.tags.iteritems():
            print str(key) + ' : ' + str(value)
        print