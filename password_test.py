
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
        
        