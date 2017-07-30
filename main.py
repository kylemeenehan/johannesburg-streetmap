import xml.etree.cElementTree as ET
import exploration.count_tags as CT
import exploration.get_unique_users as uu
import audit.street_reader as sr
import output.pprint as pp

johannesburg = 'data/johannesburg.osm'


def explore():
    # print 'Tag Count'
    # tag_count = CT.count_tags(johannesburg)
    # pp.print_dict(tag_count)
    # print len(uu.get_unique_users(johannesburg))
    street_reader = sr.Street_Reader()
    for event, elem in ET.iterparse(johannesburg):
        street_reader.get_street_types(elem)
    for street_type in street_reader.street_types:
        print street_type


if __name__ == '__main__':
    explore()