'''
code to demonstrate write function.
this will completely erase the files data and add new text in the file.
NOTE = we should run the code only once after appending it. 
       the no of times we run, those many times the text will be added.
'''

# NOTE - use 'file.txt'

file = open("file.txt", "w")
file.write("\nAbhilesh - 1NC20IS001")
file.close()  


'''
Initial data in file

Madan Mohan - 1NC20IS018
J Kiran Gowda - 1NC20IS013
Hemanth Gowda - 1NC20IS012
Harshitha N - 1NC20IS011
Preksha C P - 1NC20IS029


After writing the file

Abhilesh - 1NC20IS001
'''

# We can create a new file by using write function.

file = open("file1.txt", "w")
file.write("This is a new file")
file.write("\nAbhilesh - 1NC20IS001")
file.close()  

'''
New file will be created with data

This is a new file
Abhilesh - 1NC20IS001
'''
