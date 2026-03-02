class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class GuestTeacher(Teacher):
    def __init__(self, name, subject, rate):
        super().__init__(name, subject)
        self.rate = rate

    def salary(self):
        return self.rate * 40    # 40 hours per month

g = GuestTeacher("Ayush", "Maths", 500)

print(g.name, g.subject, g.rate, g.salary())
