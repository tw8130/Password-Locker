import unittest #Importing the unittest module
from user_credentials import User 

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
    unittest.TestCase: TestCase that helps in creating test cases
    '''
    def setUp(self):
        '''
        SetUp method to run before each test cases
        '''
        self.new_user = User('Tabby' ,'Wanjiku' ,'twpd254')

    def test__init__(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,'Tabby')
        self.assertEqual(self.new_user.last_name,'Wanjiku')
        self.assertEqual(self.new_user.password,'twpd254') 

if __name__ == '__main__':
    unittest.main()
        