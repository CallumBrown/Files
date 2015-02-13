#Callum
#Development

import pickle

class User:
    def __init__(self):
        self.name = None
        self.DoB = None

users = []

for count in range(2):
    people = User()
    people.name = input("Enter name: ")
    people.DoB = int(input("Enter date of birth: "))
    users.append(people)

with open("dev1.dat",mode="wb") as user_file:
    pickle.dump(users,user_file)


                     
    
    
