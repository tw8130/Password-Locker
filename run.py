#!/usr/bin/env python3.6
import pyperclip
from user_credentials import User , Credential

def create_user(fname,lname,password):
    '''
    Function to create a new user account
    '''
    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user account
    '''
    User.save_user(user)

def verify_user(first_name,password):
    '''
    Function that verifies if a user exists before creating a credential account
    '''
    checking_user = Credential.check_user(first_name,password)
    return checking_user

def create_credential(user_name,account_name,site_name,password):
    '''
    Function to create a new credential account
    '''
    new_credential = Credential(user_name,account_name,site_name,password)
    return new_credential

def save_credential(credential):
    '''
    Function to save a new credential account
    '''
    Credential.save_credentials(credential)

def del_credential(credential):
    '''
    Function to delete an unwanted credential
    '''
    Credential.delete_credentials(credential)

def find_credential(account_name):
    '''
    Function that finds a credential by account_name and returns the credential
    '''
    return Credential.find_by_account_name(account_name)

def display_credentials(user_name):
    '''
    Function to display the credentials saved
    '''
    return Credential.display_credentials(user_name)

def copy_credential(account_name):
    '''
    Function that copies the credentials information to the clipboard
    '''
    return Credential.copy_credential(account_name)

def generate_password():
    '''
    Function that generates a password according to the users length
    '''
    gen_pass = Credential.generate_password()
    return gen_pass

def main():
    print(' ')
    print('''
    
██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗   ▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄☆       
██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝   ███████████████████████
██║   ██║███████║██║   ██║██║     ██║      ▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤
╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║      ▀░▐▓▓▓▓▓▓▌▀█░░░█▀
 ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║       ░░▓▓▓▓▓▓█▄▄▄▄▄█▀
  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝        █▓▓▓▓▓▌  
    ''')
    print(' ')
    print('Hello! Welcome to your password locker application')
    print('\n')
    while True:
        print(' ')
        print("-"*60)
        print('Use this short codes:\n cc-Create a new account \n li-Login \n ex-Exit')
        short_code = input('Enter one of choices above:').lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'cc':
            print("-"*60)
            print(' ')
            print('Now create a new account:')
            first_name = input('Enter your first name').strip()
            print('\n')
            last_name = input('Enter your last name').strip()
            print('\n')
            password = input('Enter your password').strip()
            print('\n')
            save_user(create_user(first_name,last_name,password))
            print(" ")
            print(f'New account:{first_name} {last_name} with your {password} was created')
            print('\n')
        
        elif short_code == 'li':
            print("-"*60)
            print('')
            print('Enter your account details to login:')
            print('\n')
            user_name = input('Enter your first name').strip()
            print('\n')
            password = str(input('Enter your password'))
            # user_exists = verify_user(user_name ,password)
            # if user_exists == user_name:
            print(" ")
            print(f'Hey {user_name}, You can now login to your account.')
            print('/n')
            while True:
                print("-"*60)
                print('Choose a short code: \n cc-Create a credential \n dp-Display Credentials \n fc-Find credential \n del-Delete credential \n cp-Copy credential \n lo-Log out')
                short_code = input('Enter an option:').lower().strip()
                print("-"*60)
                if short_code == 'cc':
                    print(' ')
                    print('Enter your credential details:')
                    account_name = input('Enter your account\'s name').strip()
                    print('\n')
                    site_name = input('Enter your site\'s name').strip()
                    while True :
                        print(' ')
                        print("-"*60)
                        print('Choose an option to: \n ee-Enter existing password \n gp-Generate a password \n ex-Exit')
                        print('\n')
                        ch_psw = input('Enter an option:').lower().strip()
                        print("-"*60)
                        if ch_psw == 'ee':
                            print(" ")
                            password = input('Enter your password').strip()
                            print('\n')
                            save_credential(create_credential(user_name,account_name,site_name,password))
                            print(' ')
                            print(f'View your credential: Account name {account_name}- Site name {site_name}- Password {password}')
                        elif ch_psw == 'gp':
                            password = generate_password()
                            print(password)
                            print('\n')
                            save_credential(create_credential(user_name,account_name,site_name,password))
                            print(' ')
                            print(f'View your credential: Account name {account_name}- Site name {site_name}- Password {password}')
                            
                        elif ch_psw == 'ex':
                            break
                        else:
                            print('Try again Please enter valid option!!')
                        # save_credential(create_credential(user_name,account_name,site_name,password))
                        # print(' ')
                        # print(f'View your credential: Account name {account_name}- Site name {site_name}- Password {password}')
                        print('\n')

                elif short_code == 'dp':
                    print(' ')
                    if display_credentials(user_name):
                        print('Yolo! here is your credential list') 
                        print('\n ') 
                        for credential in display_credentials(user_name):
                            print(f'Account name {credential.account_name}- Site name {credential.site_name}- Password {credential.password}')
                        print('\n ')
                    else:
                        print(' ')
                        print('You do not seem to have any credentials saved yet')
                        print('\n')
                    
                elif short_code == 'cp':
                    print('')
                    chosen_account = input('Enter account name for credential pasword to copy:')
                    copy_credential(chosen_account)
                    print('Credential has been copied')
                    
                elif short_code == 'fc':
                    print('')
                    account_name = input()
                    if find_credential(account_name):
                        print('Find your credential account here!')
                        for credential in find_by_account_name(account_name):
                            print(f'User name {credential.user_name}- Site name {credential.site_name}- Password {credential.password}')
                        print('\n')
                    else:
                        print(' ')
                        print('Oops! Cannot find your credential!')
                    
                elif short_code == 'lo':
                    print("-"*60)
                    print(' ')
                    print('            THANKS FOR DROPING IN!')
                    print('             BYE.......BYE........')
                    print('\n')
                    break
                else:
                    print("-"*60)
                    print(' ')
                    print('      I really didn\t get that.Please use the short codes')
                    print('      RETRY!!!')
                    print(' ')

if __name__ == '__main__':
    main()               



                    

                        

                        
                        
            







