class Diary:
    studentdiary = {}
    studentattendance = {}

    def __init__(self, students):
        for name in students:
            self.studentdiary[name] = 0
            self.studentattendance[name] = 0
    
    def addpoints(self, name, points):
        self.studentdiary[name] = points
    
    def addattendance(self, name, attendance):
        self.studentattendance[name] = attendance

    def avarangescore(self):
        return sum(self.studentdiary.values())/len(self.studentdiary.values())

    def countattendance(self):
        return sum(self.studentattendance.values())


students = ["Adam Nowak", "Jan Kowalski", "Janusz Polak"]
classone = Diary(students)
classone.addpoints("Adam Nowak", 2)
classone.addpoints("Jan Kowalski", 3)
classone.addpoints("Janusz Polak", 4)
classone.addattendance("Adam Nowak", 1)
classone.addattendance("Jan Kowalski", 0)
classone.addattendance("Janusz Polak", 1)

print("Avarange marks: " + str(classone.avarangescore()))
print("Student present :" + str(classone.countattendance()))