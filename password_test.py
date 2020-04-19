import unittest #Importing the unittest module
from user_credentials import User , Credential

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
        self.assertEqual(len(User.users_list),1)


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

    def setUp(self):
        '''
        SetUp method to run before each test cases for credentials class
        '''
        self.new_credential= Credential('Tabby','Instagram','google.com','twpd254')

    def test__init__(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.user_name,'Tabby')
        self.assertEqual(self.new_credential.account_name,'Instagram')
        self.assertEqual(self.new_credential.site_name ,'google.com')
        self.assertEqual(self.new_credential.password,'twpd254')

    def test_save_credentials(self):
        '''
        Test to check if the new credential info is saved in the credentials_list
        '''
        self.new_credential.save_credentials()
        instagram = Credential('Tabby','Instagram','google.com','twpd254')
        instagram.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)

    def tearDown(self) :
        '''
        tearDown method that does clean up after each test case has run. 
        '''
        Credential.credentials_list = []  
        User.users_list = []

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credential from our credentials_list
        '''
        self.new_credential.save_credentials() 
        instagram = Credential('Tabby','Instagram','google.com','twpd254') #new credential
        instagram.save_credentials()

        self.new_credential.delete_credentials()# Deleting a credential object
        self.assertEqual(len(Credential.credentials_list),1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
        