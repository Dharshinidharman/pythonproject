class Calculation:
    def __init__(self, teachers):
        self.teachers = teachers

    def avgclass(self):
        t_class = 0

        for i in self.teachers:
            t_class +=i.classes_taught

        if len(self.teachers) > 0:
            avgclass= t_class / len(self.teachers)
        else:
            avgclass = 0

        print("Average number of classes taken by teachers: " + str("{:.2f}".format(avgclass)))

    def search(self, search_query):
        found = False
        for i in self.teachers:
            if search_query.lower() in i.name.lower() or search_query == str(i.teacher_id):
                print("ID: " + str(i.teacher_id) + ", Name: " + i.name + ", Age: " + str(i.age) +
                      ", Classes Taught: " + str(i.classes_taught) + ", Contact: " + i.contact)

                found = True

        if not found:
            print("print not exist")