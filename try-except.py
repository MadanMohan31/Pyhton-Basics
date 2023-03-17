# code to catch errors in python
'''
this helps to run the code when we have entered a wrong value.
in TRY, if the code gets wrong input,
it execute the code present in except
'''

try:
    num = int(input("enter the number : "))
    print(num)
except:
    print("invalid input")
    
    
    
# using multiple except condition
# here we catch particular errors.
try:
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the first number : "))
    
    print(num1 / num2)

except ZeroDivisionError:
    print("Divided by 0")
except ValueError:
    print("Invalid Input")
