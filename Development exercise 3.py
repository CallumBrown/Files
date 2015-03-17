#Callum
#Development

import pickle

class User:
    def __init__(self):
        self.name = None
        self.DoB = None

with open ("dev1.dat",mode="rb") as name_file:
    names = pickle.load(name_file)
    print(names)

for name in names:
    print(name)
