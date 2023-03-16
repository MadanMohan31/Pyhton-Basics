# code for simple calculator.

a = int(input("enter the first value : "))
b = int(input("enter the second value : "))

add = a + b
sub = a - b
mul = a * b
div = a / b
mod = a % b

print("Addition       of %d and %d is %d" %(a,b,add))
print("Substracted    of %d and %d is %d" %(a,b,sub))
print("Multiplication of %d and %d is %d" %(a,b,mul))
print("Division       of %d and %d is %d" %(a,b,div))
print("Modulus        of %d and %d is %d" %(a,b,mod))
