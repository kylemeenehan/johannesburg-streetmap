# This class serves to take streets that are spelled or formatted incorrectly and correct them
class Street_Cleaner:
    
    # A list of expected street types
    expected_street_types = ['Avenue', 'Boulevard', 'Close', 'Corner', 'Crescent', 'Derby', 'Drive', 'East', 'Grove', 'Lane', 'North', 'Place', 'Road', 'South', 'Square', 'Straight', 'Street', 'Way', 'West']

    # A dictionary containing the eroneous street types and their corrections
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
    
    def __init__(self):
        self.streets = []

    # This function prints out suggested corrections for a given list of streets
    def suggest_cleans(self, streets):
        streets_with_no_suggestions = []
        print 'Suggested Cleans :'
        for street in streets:
            street_as_list = street.split(' ')
            if street_as_list[-1] in self.correction_mapping:
                street_as_list[-1] = self.correction_mapping[street_as_list[-1]]
                print street + ' => ' + ' '.join(street_as_list)
            else:
                streets_with_no_suggestions.append(street)
        print '\nThere are no suggested cleans for these streets:'
        for street in streets_with_no_suggestions:
            print street
        print

    def clean_street(self, street_name):
        for key,value in self.correction_mapping.iteritems():
            street_as_list = street_name.split(' ')
            if key in street_as_list:
                street_name = street_name.replace(key, value)
                break

        return street_name