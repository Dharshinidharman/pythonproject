class Filter:
    def __init__(self, teachers):
        self.teachers = teachers

    def findage(self, age):
        fliter_teach = []

        for teacher in self.teachers:
            if teacher.age == age:
                fliter_teach.append(teacher)

        self.teacher_res(fliter_teach)

    def findclass(self,classes):
        fliter_teach = []

        for teacher in self.teachers:
            if teacher.classes_taught == classes:
                fliter_teach.append(teacher)
        self.teacher_res(fliter_teach)

    def teacher_res(self, fliter_teach):
        print("Filtered Teachers:")
        if not fliter_teach:
            print("No teachers match the criteria.")
        else:
            for i in fliter_teach:
                print("ID: " + str(i.teacher_id) + ", Name: " + i.name + ", Age: " + str(i.age) + ", " "Classes Taught: " + str(i.classes_taught) + ", Contact: " + i.contact)

