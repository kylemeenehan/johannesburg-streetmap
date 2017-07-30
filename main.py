import exploration.count_tags as CT
import output.pprint as pp

johannesburg = 'data/johannesburg.osm'

tag_count = CT.count_tags(johannesburg)
pp.print_dict(tag_count)