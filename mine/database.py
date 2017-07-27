class Database(object):

    def __init__(self,location):
        """Proof of concept assumes location == folder with a bunch of .csv files"""
        self.location = location


class Dataset(object):

    def __init__(self,location):
        """Proof of concept assumes location == address to a .csv file"""

        self.location = location
