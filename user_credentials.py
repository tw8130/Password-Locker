
global users_list
class User:
    '''
    Class that creates a users account and saves their information
    '''

    #global users_list
    users_list=[]   #the class variable

    def __init__(self,first_name,last_name,password):
        '''
        The __init__ method that helps us define properties for our objects
        '''
        #Instance variables
        self.first_name =first_name
        self.last_name =last_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into users_list
        '''
        User.users_list.append(self)

class Credentials:
    '''
    Class to create an account credentials,delete,view,save information and generate passwords
    '''
    #Class variables
    credentials_list =[]
    user_credentials_list =[]

    @classmethod
    def check_user(cls,first_name,password):
        '''
        Method checks if users input matches entries in users_list
        '''
        current_user =''
        for user in User.users_list:
            if(user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user

    def __init__(self,user_name,account_name,site_name,password):
        '''
        The __init__ method that helps us define properties for our objects
        '''
        #instance variables
        self.user_name = user_name
        self.account_name = account_name
        self.site_name = site_name
        self.password = password
    
    def save_credentials(self):
        '''
        Method to save credentials instance objects that are newly created
        '''
        Credential.credentials_list.append(self)


