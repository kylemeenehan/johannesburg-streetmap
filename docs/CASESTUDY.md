# OpenStreetMap Data Case Study: Johannesburg

## Map Area

Johannesburg, South Africa

* [OpenStreetMap](https://www.openstreetmap.org/search?query=johannesburg#map=12/-26.2023/28.0436)
* [MapZen](https://mapzen.com/data/metro-extracts/metro/johannesburg_south-africa/) (Use this download to replicate results)

Johannesburg, South Africa, is where I was born and where I live now. I grew up in Hekpoort, but there aren't many streets there, so I've decided to take a look at the Jozi streets for this case study.

# Initial exploration

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

## Problems Encountered

* Inconsistent street types
    * eg: st, str, street, Street
* Different languages
    * We have eleven official languages in South Africa, mostly the challenge with this data though was changing street types from Afrikaans to English
* Misspelled and incorrect cities

### Inconsistent street types

I decided to clean these up before importing them into the database using a street cleaner class with a dictionary that maps errors to their corrections:

    correction_mapping = {
        'Ave': 'Avenue',
        'Dr': 'Drive',
        'Naude': 'Naude Drive',
        'St': 'Street',
        'Straat': 'Street',
        'Street)': 'Street',
        'ave': 'Avenue',
        'close': 'Close',
        'drive': 'Drive',
        'north': 'North',
        'road': 'Road',
        'street': 'Street'
        }

Then the clean_street method returns the street name with the corrected type using a the above dictionary.

    def clean_street(self, street_name):
        for key,value in self.correction_mapping.iteritems():
            street_as_list = street_name.split(' ')
            if key in street_as_list:
                street_name = street_name.replace(key, value)
                break

        return street_name

### Different languages, misspelled and incorrect cities
For these problems I followed a near identical solution to the problem of the incorrect street types.

# Populating the database

In order to work with the database efficiently, I decided to use Pandas. For example, after writing out the data to csv using the code provided, the following code populates the nodes table:

    def populate_nodes():
        df = pandas.read_csv(NODES_PATH)
        df.to_sql('nodes', conn, if_exists='replace', index=False)

Using Pandas meant that I was able to accomplish complex tasks while writing less code.

# File sizes

After outputting to csv and populating the db, these are the sizes of the resulting files:

    johannesburg.osm    159.1MB

    nodes.csv           59MB
    nodes_tags.csv      3MB
    ways.csv            6.7MB
    ways_nodes.csv      20.9MB
    ways_tags.csv       8.4MB

    johannesburg.db     87.2MB

# Querying the data

After I had the data cleaned, and imported into the database it was time to ask some questions of the data. For this I decided to use Pandas again. This menat that I could store the database queries and output the results of the query to the terminal when needed, without having to rewrite the queries manually. For example, the following code prints the number of rows in the nodes table:

    # print the number of rows in the nodes table
    num_rows = pandas.read_sql('SELECT COUNT(*) as num_rows from nodes', conn)
    print "\nNumber of rows in the nodes table:"
    print num_rows

At the time of writing the code above produced the following result:

    Number of entries for streets in the nodes_tags table:
    COUNT(*)
    0       772

In the example above, the conn variable is the connection to the sqlite database, established with the following code:

    conn = sqlite3.connect('db/johannesburg.db')

## Streets with the most entries in the nodes table

The following query lists the streets that are most referenced and the number of times that they're referenced

    # print the top ten streets by their number of entries
    unique_streets= pandas.read_sql('SELECT value, COUNT(*) as count FROM nodes_tags WHERE key = "street" GROUP BY value ORDER BY count DESC LIMIT 10', conn)
    print "\nTop ten streets by the number of entries with that street name, along with their counts:"
    print unique_streets

Which outputs:

    Top ten streets by the number of entries with that street name, along with their counts:
                    value  count
    0         Spoorlyn Road     34
    1  Van der Sterr Street     32
    2         Monument Road     27
    3      Fred Driver Road     25
    4        Canopus Street     17
    5          Osche Street     17
    6         Ruimte Street     14
    7       Saxonwold Drive     14
    8           Daniel Road     12
    9                 Mizen     12


## Number of Unique Users

The following query gets the number of unique users that have contributed to the dataset

    # print the number of unique users
    num_users = pandas.read_sql('SELECT COUNT(DISTINCT(combined.uid)) as num_users from (SELECT uid from nodes UNION ALL SELECT uid from ways GROUP BY uid) combined', conn)
    print "\nThe number of unique users is: "
    print num_users

Which outputs:

    The number of unique users is:
            num_users
    0       1186

## Top users by contributions

The following query lists the top users by their contributions to the nodes and the ways tables combined:

    # print the top ten users by contributions
    top_users = pandas.read_sql('SELECT user, COUNT(*) as contributions FROM (SELECT id, user, uid from nodes UNION ALL SELECT id, user, uid from ways) GROUP BY uid ORDER BY contributions DESC LIMIT 10', conn)
    print "\nThe top users by contributions are:"
    print top_users

Which outputs:

    0    thomasF           8482
    1  Ido Marom           7678
    2  Firefishy           5966
    3   NicRoets           5601
    4    altairb           4671
    5       chdr           4189
    6    Pa Deef           3410
    7   Tinshack           3047
    8  titanbeos           2907
    9   Markus59           2843


# Additional Ideas

It would be great to get the area covered by each user. In order to do that, we would have to get the gps locations of each of the contributsions. Looking at the top 10 rows of the nodes table, it's clear that we have that data:


    The top ten rows of the nodes table:
            id        lat        lon       user     uid  version  changeset
    0  21538282 -26.098922  28.014038  Firefishy    3560        3   16131674
    1  21538288 -26.098932  28.010641  Firefishy    3560        6   18479185
    2  21538289 -26.099314  28.010895     eltonp  289631        2    5217516
    3  21538295 -26.099650  28.011296  Firefishy    3560        3   16131674
    4  21538296 -26.100241  28.011681  Firefishy    3560        3   16131674
    5  21538311 -26.103789  28.013874     eltonp  289631        2    5217516
    6  21538363 -26.109169  28.017606  Firefishy    3560        4   16131674
    7  21587257 -26.110314  27.957861       Quin  357670        3    6274249
    8  21587259 -26.108705  27.958851       Quin  357670        3    6274249
    9  21587261 -26.106487  27.960113       Quin  357670        3    6274249

We would then have to get a list of all of the users, create subsets of the nodes table for each user, and write a python script that iterates through each coordinats, checks whether it is part of the existing area captured, or whether to increase the area that the user has contributed to.

The greatest challenge in this endeavor would be the geometry, but that could perhaps be simplified by using the Google Maps API's [Geometry Library](https://developers.google.com/maps/documentation/javascript/geometry) and calling computeArea(). In that case, the challenge would still be to get the coordinates into a closed loop without the noise of coordinates inside the polygon.

# Conclusion

This data is no Google Maps, but it's great to see so much user contributed data to an open source project! With volunteer work though, comes the challenge of dirty data. As we've seen here, there was a fair amount of cleaning to do, but it wasn't an impossible challenge. I think that with a few volunteers who have some data munging skills, the quality of the Johannesburg area data could be greatly improved and help future analysts and users.