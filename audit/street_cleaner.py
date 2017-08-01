class Street_Cleaner:
    
    expected_street_types = ['Avenue', 'Boulevard', 'Close', 'Corner', 'Crescent', 'Derby', 'Drive', 'East', 'Grove', 'Lane', 'North', 'Place', 'Road', 'South', 'Square', 'Straight', 'Street', 'Way', 'West']

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