import xml.etree.cElementTree as ET
import pprint

import exploration.user_counter as uc
import exploration.tag_counter as tc
import audit.street_reader as sr
import audit.city_reader as cr

johannesburg = 'data/johannesburg.osm'


def explore():
    print 'Exploring Data... \n'
    tag_counter = tc.Tag_Counter()
    user_counter = uc.User_Counter()
    street_reader = sr.Street_Reader()
    city_reader = cr.City_Reader()
    for event, elem in ET.iterparse(johannesburg):
        tag_counter.read_elem(elem)
        user_counter.read_elem(elem)
        street_reader.read_elem(elem)
        city_reader.read_elem(elem)

    user_counter.print_num_users()
    tag_counter.print_tag_count()
    #tag_counter.print_tag_types()
    street_reader.print_street_types()
    street_reader.print_unexpected_streets()
    street_reader.print_suggested_corrections()
    city_reader.print_cities()
    city_reader.print_num_cities()


if __name__ == '__main__':
    explore()