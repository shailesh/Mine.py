from os import listdir
from os.path import isfile, join
import json

class Database(object):

    def __init__(self,location):
        """Proof of concept assumes location points to a folder with a bunch of .csv files"""
        self.location = location
        self.load_datasets()

    def __len__(self):
        return len(self.datasets)

    def load_datasets(self):

        files = [f for f in listdir(self.location) if (isfile(join(self.location, f)) and f[-4:] == '.csv')]

        self.datasets = {}

        for fname in files:
            self.datasets[fname] = CSVDataset(self.location+"/"+fname)

        return self.datasets

    def keys(self):
        return self.datasets.keys()

    def to_dict(self):
        me = list()
        for d in self.datasets.values():
            me.append(d.to_dict())
        return me

    def to_json(self):
        return json.dumps(self.to_dict())

    def __getitem__(self,i):
        if(type(i) == int):
            return list(self.datasets.values())[i]
        else:
            return self.datasets[i]

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(list(self.datasets.values()))


class CSVDataset(object):

    def __init__(self,location):
        """Proof of concept assumes location is the full path to a .csv file"""

        self.location = location
        self.name = self.location.split("/")[-1]

        f = open(self.location,'r')
        self.labels = f.readline()[:-1].split(",")
        f.close()

    def __len__(self):
        f = open(self.location,'r')
        raw = f.readlines()
        f.close()
        return len(raw)

    def to_dict(self):
        me = {}
        me['name'] = self.name
        me['length'] = len(self)
        me['labels'] = self.labels
        return me

    def to_json(self):
        return json.dumps(self.to_dict())

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<Dataset:"+str(self.name) + ":"+ str(len(self)) + ">"
