## PROJECT PYTHON APPLICATION
 This is a project about making an application that manages passwords and even generates new password for a user.
## AUTHOR:
By Tabitha Wanjiku
## DESCRIPTION:
The project you create an an application using the concepts covered in python week1 content to help a user
manage their passwords and even generate new passwords.This application helps one to easily remember all their passwords and even create new ones.
# User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:

To create an account with my details - log in and password
Store my existing login credentials
Generate a password for a new credential/account
Copy my credentials to the clipboard
# BDD
Behaviour	                              Input	                                        Output
Display codes for navigation	        In terminal:                 | Welocome to                             
                                      $./password_locker.py         |the application! use the short codes
                                                                    |cc-Create nwe user,li-login
                                        	                          |ex-exit the navigation

Display prompt for creating an account |Enter: ca	      |Enter your first name, last name and password

Display prompt for login in	           |Enter: li       |Enter your account name and password

Display codes for navigation	       |Successful login	|Choose an option: cc - Create Credential,                                                       dp - Display Credentials, cp - Copy 
                                                          fc-find credential,lo- exit application
                                                        
Display prompt for creating a credential	|Enter: cc  |	Enter the account name, your username and password
                                                        also your site name

Display a list of credentials	            |Enter: dp	|Prints a list of saved credentials

Display prompt for which credential to |Enter:cp    |Enter account name                                     
 copy                                                     you wish to copy

Exit application	                        |Enter: ex	Exit the current navigation stage

Log out of the application                | Enter: lo  Log out of the application
# SETUP INSTALLATION
## Prerequisites
python3.6
pip
pyperclip
## Cloning
In your terminal:

  $ git clone https://github.com/tw8130/Password-Locker/
  $ cd Password
## Running the Application
To run the application, in your terminal:

  $ chmod +x run.py
  $ ./run.py
## Testing the Application
To run the tests for the class file:

  $ python3.6 password_test.py

## KNOWN BUGS:
Any bugs noted you can email me for clarification.
## TECHNOLOGIES USED:
.Python3.6
## CONTACT INFO:
You can email at:mwangitabitha2020@gmail.com
## LICENSE:
MIT License

Copyright (c) [2020] Tabitha Wanjiku]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.