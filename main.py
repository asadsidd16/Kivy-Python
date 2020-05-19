from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from database import CatDataBase
#from database import ItemDataBase


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created

class AddCatWindow(Screen):
    myCategory = ObjectProperty(None)
    current = ""

    def submit(self):
        if(cdb.add_category(self.myCategory.text) == 1):
            successCatWin()
            self.reset()
        else:
            duplicateCatWin()
            self.reset()

    def reset(self):
        self.myCategory.text == ""

class DelCatWindow(Screen):
    test = ObjectProperty(None)
    current = ""

class AddItemWindow(Screen):
#    myCategory = ObjectProperty(None)
#    myItem = ObjectProperty(None)
#    myQuantity = ObjectProperty(None)
#   myNote = ObjectProperty(None)
    current = ""

#    def submit(self):
#        if(idb.add_item(self.myCategory.text, self.myItem.text, self.myQuantity.text, self.myNote.text) == 1):
#            successItemWin()
#            self.reset()
#        else:
#            duplicateItemWin()
 #           self.reset()

    def reset(self):
        self.myCategory.text == ""
        self.myItem.text == ""
        self.myQuantity.text == ""
        self.myNote.text == ""

class DelItemWindow(Screen):
    test = ObjectProperty(None)
    current = ""

class WindowManager(ScreenManager):
    pass


def successItemWin():
    pop = Popup(title='Successful',
                  content=Label(text='Item has been successfully added'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def duplicateItemWin():
    pop = Popup(title='Failed',
                  content=Label(text='This item already exists'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def successCatWin():
    pop = Popup(title= "Successful", content = Label(Text = "Category has been successfully added"), size_hint = (None, None), size = (400,400))
    pop.open()

def duplicateCatWin():
    pop = Popup(title= "Failed", content = Label(Text = "This category already exists"), size_hint = (None, None), size = (400,400))
    pop.open()


def invalidLogin():
    pop = Popup(title='WARNING: Invalid Login',
                  content=Label(text='username or password is not recognized'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")
cdb = CatDataBase("categories.txt")
#idb = ItemDataBase("items.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"), AddCatWindow(name="addCat"), DelCatWindow(name="delCat"), AddItemWindow(name="addItem"), DelItemWindow(name="delItem")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()