from student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation = False):
        super().__init__(self, name, grade, classes)
        self.gets_transportation = gets_transportation 

    
    def display_transportation_message(self):
        does_message = "does" if self.gets_transportation else "doesn't"
        return f"{self.name} {does_message} get transporation"
    
    
    def summary(self):
        student_summary = super().summary()
        gets_transportation = self.display_transportation_message()
        
        return "\n".join((student_summary, gets_transportation))
  