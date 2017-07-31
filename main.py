import xml.etree.cElementTree as ET
import pprint

import exploration.user_counter as uc
import audit.street_reader as sr
import exploration.tag_counter as tc

johannesburg = 'data/johannesburg.osm'


def explore():
    # print 'Tag Count'
    # tag_count = CT.count_tags(johannesburg)
    # pp.print_dict(tag_count)
    # print len(uu.get_unique_users(johannesburg))
    street_reader = sr.Street_Reader()
    tag_counter = tc.Tag_Counter()
    user_counter = uc.User_Counter()
    for event, elem in ET.iterparse(johannesburg):
        street_reader.read_elem(elem)
        tag_counter.read_elem(elem)
        user_counter.read_elem(elem)

    print "Tags: "
    tag_counter.print_tag_count()
    user_counter.print_num_users()
    # pprint.pprint(street_reader.street_types)


if __name__ == '__main__':
    explore()