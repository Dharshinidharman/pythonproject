import json
from sharedLib import crud
from sharedLib.filter import Filter
from sharedLib.calculation import Calculation


class management:
    def __init__(self):
        self.teachers = []
        self.load()
        self.crud = crud.CRUD(self.teachers)
        self.filter = Filter(self.teachers)
        self.calculation = Calculation(self.teachers)

    def load(self):
        try:
            with open("tmsData.json", "r") as file:
                data = json.load(file)
                for teacher_data in data:
                    t = crud.Teacher(**teacher_data)
                    self.teachers.append(t)
        except FileNotFoundError:
            pass


    def run(self):
        while True:
            self.content()
            ch = input("Enter number:")

            if ch == "1":
                self.crud.view()

            elif ch == "2":
                name = input("name ")
                dob = input("birthday(yyyy-mm-dd): ")
                classes= int(input("num of classes: "))
                contact = input("phone number: ")
                self.crud.add(name, dob, classes, contact)
            elif ch == "3":
                newid = input("new id")
                newname = input("new name")
                newdob = input("birthday(yyyy-mm-dd")
                newclass = int(input("num of classes"))
                newnum = input("new phone num")
                self.crud.update_teacher(newid, newname, newdob, newclass, newnum)

            elif ch == "4":
                id = input("id to delete")
                self.crud.delete_teacher(id)
            elif ch == "5":
                search= input("id to find")
                self.calculation.search(search)
            elif ch == "6":
                self.filter.findage(int(input("age to find")))
            elif ch == "7":
                self.filter.findclass(int(input("classes to find ")))

            elif ch == "8":
                self.calculation.avgclass()
            else:
                print("enter 1 to 8")

    def content(self):
        print("\nTeacher management records")
        print("1.show teachers")
        print("2.add")
        print("3.Update record")
        print("4.Delete")
        print("5.search teacher")
        print("6.filter age")
        print("7.filter class")
        print("8.Cal avg classes")

if __name__ == "__main__":
    tms = management()
    tms.run()