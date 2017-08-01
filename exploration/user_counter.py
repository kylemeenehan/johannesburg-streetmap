import re

class User_Counter:
    def __init__(self):
        self.users = set()

    def get_user(self,elem):
        return elem.attrib['uid']


    def read_elem(self, elem):        
        if 'uid' in elem.attrib:
            user = self.get_user(elem)
            if user not in self.users:
                self.users.add(user)

    def print_num_users(self):
        print "There are " + str(len(self.users)) + " unique users.\n"