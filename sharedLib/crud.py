import json
from datetime import datetime

# crud.py
# crud.py

class Teacher:
    def __init__(self, teacher_id, name, age, dob, classes_taught, contact):
        self.teacher_id = teacher_id
        self.name = name
        self.age = age
        self.dob = dob
        self.classes_taught = classes_taught
        self.contact = contact

    def cal_age(self):

        t = datetime.today()
        bd = datetime.strptime(self.dob, "%Y-%m-%d")
        age = t.year - bd.year - ((t.month, t.day) < (bd.month, bd.day))
        return age



class CRUD:
    def __init__(self, teachers):
        self.teachers = teachers

    def view(self):
        print("Teachers:")
        for i in self.teachers:
            print(  "Name: " + i.name + ", Age: " + str(i.age) + ",DOB: " + str(i.dob) +
                  ", Classes: " + str(i.classes_taught) + ", Contact: " + i.contact)

    def add(self, name, dob, classes_taught, contact):
        id = len(self.teachers) + 1
        t = Teacher(id, name, None, dob, classes_taught, contact)
        t.age = t.cal_age()  # No need to pass dob here
        self.teachers.append(t)
        print("Teacher " + name + " added")

        self.save_data()

    def update_teacher(self, teacher_id, new_name, new_dob, new_classes_taught, new_contact):
        for i in self.teachers:
            if i.teacher_id == int(teacher_id):
                i.name = new_name
                i.age = i.cal_age()
                i.dob = new_dob
                i.classes_taught = new_classes_taught
                i.contact = new_contact

                print("Teacher " + str(teacher_id) + " updated")
                break
        else:
            print("Teacher with ID " + str(teacher_id) + " not found")
        self.save_data()

    def delete_teacher(self, teacher_id):
        filterteach = []

        for i in self.teachers:
            if i.teacher_id != int(teacher_id):
                filterteach.append(i)

        self.teachers = filterteach

        print("Teacher " + str(teacher_id) + " deleted")
        self.save_data()

    def save_data(self):
        try:
            with open("tmsData.json", "w") as file:
                data = []

                for teacher in self.teachers:
                    teacher_data = {
                        "teacher_id": teacher.teacher_id,
                        "name": teacher.name,
                        "age": teacher.age,
                        "dob": teacher.dob,
                        "classes_taught": teacher.classes_taught,
                        "contact": teacher.contact
                    }
                    data.append(teacher_data)

                json.dump(data, file, indent=2)
        except Exception as e:
            print("Error saving data: " + str(e))


