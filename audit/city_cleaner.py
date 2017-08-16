class City_Cleaner:

    correction_mapping = {
      'Benini': 'Benoni',
      'Bonaro Park': 'Bonaero Park',
      'Edenvale, Ekurhuleni': 'Edenvale',
      'Ekurhuleni, Edenvale': 'Edenvale',
      'Ekurhuleni. Edenvale': 'Edenvale',
      'Fourways - Johannesburg': 'Fourways',
      'Johanesburg': 'Johannesburg',
      'Kempton Pank': 'Kempton Park',
      'Kempton Parl': 'Kempton Park',
      'Kempton park': 'Kempton Park',
      'Kyalami, Midrand': 'Kyalami',
      'Roodepoort, Weltevredenpark': 'Weltevredenpark',
      'Weltevreden Park, Roodepoort': 'Weltevredenpark',
      'Sandton, Johannesburg': 'Sandton',
      'Vorsterkroon, Nigel': 'Nigel',
      'johannesburg': 'Johannesburg',
      'mayfair': 'Mayfair',
      'midrand': 'Midrand',
      
    }

    def clean_city(self, city):
        for key,value in self.correction_mapping.iteritems():
            if city == key:
                city = value
                break

        return city

    