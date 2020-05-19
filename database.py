import datetime


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

class CatDataBase:
    def __init__(self, filename):
        self.filename = filename
        self.category = []
        self.file = None
        self.load()

    def load(self):
        self.category = open(self.filename).read().splitlines()

    def add_category(self, myCat):
        if myCat in self.category:
            print("This category already exists!")
            return -1
        else:
            self.category.append(myCat)
            with open(self.filename, "a") as f:
                    f.write(myCat + "\n")
            return 1

    def getCategories(self):
        return self.category

#class ItemDataBase:
#    def __init__(self, filename):
#        self.filename = filename
#        self.items = []
#        self.file = None
#        self.load()

#    def load(self):
#        self.file = open(self.filename, "r")

#        for line in self.file:
#            category, itemName, quantity, notes = line.strip().split(";")
#            self.items.append([category, itemName, quantity, notes])

#        self.file.close()

#    def add_item(self, myCategory, myItemName, myQuantity, myNotes):
#        if [myCategory,myItemName,myQuantity,myNotes] in self.items:
#            print("This item already exists!")
#            return -1
#        else:
#            self.items.append([myCategory,myItemName,myQuantity,myNotes])
#            with open(self.filename, "a") as f:
#                f.write(myCategory + ";" + myItemName + ";" + myQuantity + ";" + myNotes + "/n")
#            return 1

#    def getItems(self):
#        return self.items