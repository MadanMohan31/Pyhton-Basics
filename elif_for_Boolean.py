# this program is for mendel experiment on pea plant

print("***MENDEL EXPERIMENT***")
print("")
print("Enter 1 if Tall or 0 if Dwarf")
print("")

Father = int(input("Enter the Father height : "))
Mother = int(input("Enter the Mother height : "))

print("")

if Father == 1 and Mother == 1:
    print("Father is Tall and Mother is Tall.")
    print("Child is Tall.")
    
elif Father == 1 and Mother == 0:
    print("Father is Tall and Mother is Dwarf.")
    print("Child is Tall.")
    
elif Father == 0 and Mother == 1:
    print("Father is Dwarf and Mother is Tall.")
    print("Child is Tall.")
    
else:
    print("Father is Dwarf and Mother is Dwarf.")
    print("Child is Dwarf.")
    
