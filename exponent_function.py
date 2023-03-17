# Exponential functions give the power value of the given number
print(2**3)

# Exponential function by using for loop
def power_of(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result

print(power_of(3, 2))
