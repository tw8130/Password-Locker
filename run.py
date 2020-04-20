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

