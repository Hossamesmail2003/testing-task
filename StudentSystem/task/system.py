class Student:
    def __init__(self, student_id, name, gender, degrees):
        self.id = student_id
        self.name = name
        self.gender = gender
        self.degrees = degrees


class StudentSystem:
    def __init__(self):
        self.students = [
            Student(1, "Ahmed", "male", [94, 83, 72, 56, 98]),
            Student(4, "Aml", "Female", [60, 89, 65, 74, 55]),
            Student(3, "Donia", "Female", [80, 95, 93, 97, 98]),
            Student(2, "Mohamed", "male", [80, 84, 87, 90, 68]),
            Student(5, "Ali", "male", [49, 55, 30, 50, 48]),
        ]

    def all_students(self):
        return self.students

    def get_details(self, student_id):
        return [student for student in self.students if student.id == student_id]

    def add_user(self, student_id, name, gender, degrees):
        if not student_id or not name:
            return "Student ID or Name couldn't be empty"
        else:
            self.students.append(Student(int(student_id), name, gender, degrees))
            return "Success"

    def delete_user(self, student_id, name):
        for student in self.students:
            if student.id == student_id and student.name == name:
                self.students.remove(student)
                return "Success"
        return "Fail"

    def total_result(self, degrees):
        return sum(degrees)

    def grade(self, degrees):
        total = self.total_result(degrees)
        percentage = (total / 500) * 100
        if percentage >= 85:
            return "Excellent"
        elif 75 <= percentage < 85:
            return "Very Good"
        elif 50 <= percentage < 75:
            return "Good"
        else:
            return "Fail"

system = StudentSystem()
    # Example usage:
print(system.all_students())
print(system.add_user("6", "Sara", "Female", [90, 92, 85, 88, 91]))
print(system.get_details(3))
print(system.delete_user(5, "Ali"))
print(system.grade([85, 90, 78, 88, 92]))