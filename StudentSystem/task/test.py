import unittest
from system import StudentSystem

class TestStudentSystem(unittest.TestCase):
    def setUp(self):
        self.system = StudentSystem()

    def test_all_students(self):
        students = self.system.all_students()
        self.assertEqual(len(students), 5)  # Check initial student count

    def test_get_details(self):
        student_details = self.system.get_details(1)
        self.assertEqual(student_details[0].name, "Ahmed")  # Check name of student with ID 1
        self.assertEqual(len(student_details), 1)  # Check that only one student is returned

    def test_add_user(self):
        result = self.system.add_user("6", "Sara", "Female", [90, 92, 85, 88, 91])
        self.assertEqual(result, "Success")  # Check if addition is successful
        self.assertEqual(len(self.system.all_students()), 6)  # Check if the student count increased

    def test_delete_user(self):
        result = self.system.delete_user(5, "Ali")
        self.assertEqual(result, "Success")  # Check if deletion is successful
        self.assertEqual(len(self.system.all_students()), 4)  # Check if the student count decreased

    def test_grade(self):
        grades = [90, 80, 70, 60, 50]
        result = self.system.grade(grades)
        self.assertEqual(result, "Good")  # Check the correct grade based on average

if __name__ == "__main__":
    unittest.main()