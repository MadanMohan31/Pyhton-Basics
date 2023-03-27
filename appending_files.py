'''
code to demonstrate append function.
this helps to add a new line at the end of the text file.
in a text file we have to keep a new line to append the new text.
if we do not have a new line, it continues with the last line of the file.
NOTE = we should run the code only once after appending it. 
       the no of times we run, those many times the text will be added.
'''

# NOTE - use 'file.txt'

file = open("file.txt", "a")
file.write("Abhilesh - 1NC20IS001")
file.close()  

'''
Initial data in file

Madan Mohan - 1NC20IS018
J Kiran Gowda - 1NC20IS013
Hemanth Gowda - 1NC20IS012
Harshitha N - 1NC20IS011
Preksha C P - 1NC20IS029


After appending

Madan Mohan - 1NC20IS018
J Kiran Gowda - 1NC20IS013
Hemanth Gowda - 1NC20IS012
Harshitha N - 1NC20IS011
Preksha C P - 1NC20IS029
Abhilesh - 1NC20IS001
''' 
