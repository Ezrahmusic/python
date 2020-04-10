import ezgmail
import os
UnreadThreads = ezgmail.unread()
ezgmail.summary("unreadThreads")
ezgmail.init()
ezgmail.EMAIL_ADDRESS('anin4325@gmail.com')
os.chdir('/Users/ezrahampton/PycharmProjects/untitled')

ezgmail.send('anin4325@gmail.com', 'python scripting', "Hello all and welcome to the new age of tech and such",
cc='ezrahamptonmusic@gmail.com', bcc='ezra.hamptoniii@gmail.com,')

