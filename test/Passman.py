#!/usr/bin/python3

"""
Author - HashTag (github.com/HashTag-4512)
Date - 22/5/21
Password Manager written in Python and SQL

"""

#importing packages

import os
import getpass
import pyfiglet
import sqlite3
from cryptography.fernet import Fernet
import re

#Variables
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
tr = True
folevar = "/etc/" # Directory to store pass hash 
filevar = "passinf.pm" # file tp store pass hash 
fullvar = folevar + filevar 
print(fullvar)

#integrity checking algs
def check(email):


    if (re.search(regex , email)):
        print("Valid email")

    else:
        print("Sorry, thats not a valid email!")


def check_passwd(passwd):
    spec_sym = ['!' , '@' , '#' , '$' , '%' , '&' , '*']
    chk_val = True


    #check if >8 char
    if len(passwd) < 8:
        print("Password must be atleast 8 charcters!")
        chk_val = False

    #check if > 20 char
    if len(passwd) > 20:
        print("Password must be less than 20 char")
        chk_val = False

    #check for numbers
    if not any(char.isdigit() for char in passwd):
        print("Must be atleast one number in password")
        chk_val = False


     #check for CAPS LETTERS
    if not any(char.isupper() for char in passwd): 
        print("Must be atleast one capital letter ")
        chk_val = False


     #check for lowercase letters
    if not any(char.islower() for char in passwd):
        print("Must be atleast one lowercase letter")
        chk_val = False

     #check for symbols
    if not any(char in spec_sym for char in passwd):
        print("Must be atleast one symbol in password")
        chk_val = False

    if chk_val:
        return chk_val



#encryption and decryption algs
def dec():
    dec_message = enc_type.decrypt(enc_message)
    encoding = "utf-8"
    convar = dec_message.decode(encoding)
    print(convar)



def enc(passwd):
    t = True
    key = Fernet.generate_key()
    global enc_type
    global enc_message
    global varr
    enc_type = Fernet(key)
    #var = input("Enter a message: ")

    varcon = bytes(passwd , "utf-8")

    enc_message = enc_type.encrypt(varcon)
    varr = enc_message.decode()
    #print(varr)




def newdec(askpass):
    key = Fernet.generate_key()
    f = Fernet(key)
    with open(fullvar , "rb") as encrypted_file:
        encrypted = encrypted_file.read()
        decoded_enc_file = encrypted.decode("utf-8")

    #decrypted = f.decrypt(decoded_enc_file)


    if askpass == decrypted:
        print("correct")

    else:
        print("incorrect")

def newenc(newpass):
    key = Fernet.generate_key()
    encoded_message = newpass.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(newpass)
    encrypted_message_str = str(encrypted_message)
    decoded_enc_message = encrypted_message_str.decode("utf-8")
    print("This is your password hash. DONT copy it. DONT memorize it. Just clear the screen \n" + encrypted_message_str)



    passwd_file =  open(fullvar ,'w+')
    passwd_file.write(decoded_enc_message)
    passwd_file.close()






    



    
#end of encryption algs
#######################
#SQL commnads

connect = sqlite3.connect("passmandb.db")
cursor = connect.cursor()


def create_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS passman (
                sitename text,
                siteemail text,
                sitepass text


        ) """)
    connect.commit()


def add_rec():
    cursor.execute("INSERT INTO passman (sitename, siteemail,sitepass) VALUES (?,?,?)", (Passman.webname, Passman.email , Passman.passwd))
    connect.commit()


def del_rec():
    delete = input("Enter the website name you want to delete: ")
    cursor.execute("DELETE FROM passman  WHERE sitename = (?)", (delete, ))
    connect.commit()



#to be worked on later because we need to give the user he decrypted passsword
def read_all():
    cursor.execute("SELECT * FROM passman")
    acc = cursor.fetchall()
    for accs in acc:
        print(accs)

    connect.commit()

def read_one():
    re_on = input("Enter the website name you want to see?: ")
    cursor.execute("SELECT * FROM passman WHERE sitename = (?) ", (re_on, ))
    for accs in acc:
        print(accs)

    connect.commit()



def update_rec():
    update = input("Enter the website name to update password: ")
    cursor.execute("UPDATE passman WHERE sitename = (?", (update, ))
    connect.commit()


#end of SQL commands


#figlet banner
figlet = pyfiglet.Figlet(font="doom")
print("----------------------------------------")
print(figlet.renderText("PassMan"))
print("     Created By H4X1ag   ")
print("     Version 2.0         ")
print("----------------------------------------")

def login():
    #check for root permissions
    if os.getuid() != 0:
        print("[!]PassMan needs root permissions to run!")
        exit()

    if os.path.exists(fullvar) != True:

        newpass = getpass.getpass("Enter a new password: ")
        newenc(newpass)
        
    #confirm = True
        
    else:
        askpass = getpass.getpass("Enter the Super User Password: ")
        newdec(askpass) 
        #print("Login Successfull")

def main():
    login()
    

if __name__ == "__main__":
    main()

    
