class Training:
    name = "DataEngineering Course"

    def __init__(self):
        self.students = []

    def add_a_student(self, name):
        self.students.append(name)


t = Training()
t.add_a_student("Stud1")
t.add_a_student("Stud2")
print(t.students)  # ['Stud1', 'Stud2']

t1 = Training()
t1.add_a_student("Stud1")
print(t1.students)  # ['Stud1', 'Stud2', 'Stud1']
