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

    def test_save_user(self):
        '''
        Test to check if the users info is saved in the users_list
        '''
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.users_list),3)


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for credentials class behaviours
    
    Args:
    unittest.TestCase:TestCase class to help in creating test cases
    '''
    def test_check_user(self):
        '''
        Test to check if users login works as it is suppossed to
        '''
        self.new_user = User('Tabby','Wanjiku' ,'twpd254')
        self.new_user.save_user()
        user2 = User('Nicky' ,'Wanjiku',  'twpd254')
        user2.save_user()

        for user in User.users_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user2.first_name
        return current_user

        self.assertEqual(current_user ,Credential.check_user(user2.password ,user2.first_name))


if __name__ == '__main__':
    unittest.main(verbosity=2)
        