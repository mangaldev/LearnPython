class Training:
    name = "DataEngineering Course"
    students = []

    @staticmethod
    def add_a_student(name): #has no reference to self
        students.append(name) # Cant access instance variables

t=Training()
t.add_a_student("Stud1")
t.add_a_student("Stud2")

print(t.students)
