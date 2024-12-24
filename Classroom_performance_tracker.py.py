class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def calculate_average(self):
        
        return sum(self.marks) / len(self.marks) if self.marks else 0
def calculate_average_marks(students):
 
    averages = {}
    for name, marks in students.items():
        student = Student(name, marks)
        averages[name] = round(student.calculate_average(), 2)  
    return averages

def find_top_performer(averages):
  
    top_student = max(averages, key=averages.get)
    return top_student
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
average_marks = calculate_average_marks(students)
top_performer = find_top_performer(average_marks)
print(f"Average Marks: {average_marks}")
print(f"Top Performer: {top_performer}")
