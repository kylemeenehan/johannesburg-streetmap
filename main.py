import xml.etree.cElementTree as ET
import pprint

import exploration.user_counter as uc
import audit.street_reader as sr
import exploration.tag_counter as tc

johannesburg = 'data/johannesburg.osm'


def explore():
    print 'Exploring Data... \n'
    street_reader = sr.Street_Reader()
    tag_counter = tc.Tag_Counter()
    user_counter = uc.User_Counter()
    for event, elem in ET.iterparse(johannesburg):
        street_reader.read_elem(elem)
        tag_counter.read_elem(elem)
        user_counter.read_elem(elem)

    user_counter.print_num_users()
    tag_counter.print_tag_count()
    street_reader.print_street_types()
    street_reader.print_unexpected_streets()
    street_reader.print_suggested_corrections()


if __name__ == '__main__':
    explore()