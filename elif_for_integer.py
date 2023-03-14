# program to find out maximum number

def max_num(num1,num2,num3):
    
    if num1 >= num2 and num1 >= num3:
        return num1
    
    elif num2 >= num1 and num2 >= num3:
        return num2
    
    else:
        return num3

print(max_num(200, 500, 50))

# > greater than
# < less than
# == equal to
# != not equal to
# <= greater than or equal to
# <= lesser than or equal to
