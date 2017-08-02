# OpenStreetMap Data Case Study: Johannesburg

## Map Area

Johannesburg, South Africa

* [OpenStreetMap](https://www.openstreetmap.org/search?query=johannesburg#map=12/-26.2023/28.0436)
* [MapZen](https://mapzen.com/data/metro-extracts/metro/johannesburg_south-africa/) (Use this download to replicate results)

Johannesburg, South Africa, is where I was born and where I live now. I grew up in Hekpoort, but there aren't many streets there, so I've decided to take a look at the Jozi streets for this case study.

## Initial exploration

For the exploratory phase of this data extraction, I used a combination of example code and my own code to look through the data looking for innacuracies. I quickly discovered that passing the whole dataset through each function in series was inefficient, so I started to refactor the functions into classes that could process data by receiving a single element at a time from the main process. This is the code in the explore function that calls methods in separate classes one element at a time:

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

