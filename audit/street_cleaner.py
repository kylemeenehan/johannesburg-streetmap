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