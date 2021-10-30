import random
elementinp1 = input("Enter first element:")
elementinp2 = input("Enter second element:")
elementinp3 = input("Enter third element:")
elementinp4 = input("Enter fourth element:")
elementinp5 = input("Enter fifth element:")
allelements = [elementinp1,elementinp2,elementinp3,elementinp4,elementinp5]
elementindex =  random.randint(0, len(allelements) -1)
element = allelements[elementindex]
print(f" Your element is:{element}")