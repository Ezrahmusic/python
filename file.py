import os
os.remove("blah.txt")
file = open("/Users/ezrahampton/PycharmProjects/untitled/blah.txt","a")
file.write("i'm adding this to a file")
file.close()

file = open("/Users/ezrahampton/PycharmProjects/untitled/blah.txt","r" )
print(file.read())
#this worked!

#i'm using "os" to remove the file
if os.path.exists("blah.txt") :
 os.remove("blah.txt")
else:
    print("Sorry I Can't! but check your files! i added something in there!")
#this deleted the file and now it's gone.

#this next one will delete a dir
os.rmdir("del_me")
#this dir is now gone

