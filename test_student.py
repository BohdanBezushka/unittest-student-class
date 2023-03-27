import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def test_full_name(self):
        student = Student("Jhon", "Bipart")

        self.assertEqual(student.full_name, "Jhon Bipart")


if __name__=='__main__':
    unittest.main()