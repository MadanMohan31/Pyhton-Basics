# simple program for nested elif statement

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male.")

elif is_male and not(is_tall):
    print("You are the short male.")
    
elif not(is_male) and is_tall:
    print("You are not a male but tall.")
    
else:
    print("You are not a male but short.")
