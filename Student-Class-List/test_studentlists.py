'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    def test_add_student_remove_student_verify_not_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Geralt')
        test_class.add_student('Yennefer')
        test_class.remove_student('Geralt')

        self.assertNotIn('Geralt', test_class.class_list)


    def test_add_student_remove_student_raises_student_error(self):
        test_class = ClassList(3)
        test_class.add_student('Link')
        test_class.add_student('Zelda')
        

        with self.assertRaises(StudentError):
            test_class.remove_student('Ganon')


    
    def test_remove_student_empty_list_raises_student_error(self):
        test_class = ClassList(3)
        
        with self.assertRaises(StudentError):
            test_class.remove_student('Spike')



    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    def test_is_enrolled_student_not_enrolled(self):
        test_class = ClassList(3)
        test_class.add_student('Finn')
        test_class.add_student('Jake')

        self.assertFalse(test_class.is_enrolled('Ice King'))


    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


    def test_index_of_student_empty_class(self):
        test_class = ClassList(3)
        
        self.assertIsNone(test_class.index_of_student('Harry'))
 

    def test_index_of_student_student_not_in_class(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Ron')

        self.assertIsNone(test_class.index_of_student('Hermoine'))

   
    def test_is_class_full_with_full_class(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Ron')
        test_class.add_student('Hermoine')

        self.assertTrue(test_class.is_class_full)
    

    def test_is_class_full_with_empty_or_partial_class(self):
        test_class = ClassList(3)

        # Test before adding students
        self.assertFalse(test_class.is_class_full())

        test_class.add_student('Harry')
        test_class.add_student('Ron')
        
        # Test after adding students
        self.assertFalse(test_class.is_class_full())

if __name__ == '__main__':
    import unittest
    unittest.main()