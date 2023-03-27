import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def test_full_name(self):
        student = Student("Jhon", "Bipart")

        self.assertEqual(student.full_name, "Jhon Bipart")

    def test_alert_santa(self):
        student = Student("Jhon", "Bipart")
        student.alert_santa()

        self.assertTrue(student.naughty_list)

if __name__=='__main__':
    unittest.main()