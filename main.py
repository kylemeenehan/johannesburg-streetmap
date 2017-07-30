import exploration.count_tags as CT
import exploration.get_unique_users as uu
import output.pprint as pp

johannesburg = 'data/johannesburg.osm'


def explore():
    print 'Tag Count'
    tag_count = CT.count_tags(johannesburg)
    pp.print_dict(tag_count)
    print len(uu.get_unique_users(johannesburg))


if __name__ == '__main__':
    explore()