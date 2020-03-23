# i'm going to mess with passwords and files with python
import os

os.path.exists("/Users/ezrahampton/PycharmProjects/untitled")

PasswordFile = open('password.txt')


SecPassword = PasswordFile.read()

print("Enter Your Password: ")

typedPassword = input()


if typedPassword == SecPassword :
    print("Granted Welcome User Of Magic")

