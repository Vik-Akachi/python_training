#!/#usr/bin/python3

#program to calculate a person's age.

print("""
AGE /MBI CALCULATOR
      """)
#Get the subject's name.
name = input("what is your name?: ")

#get the subject age details.

yob = input('what is your birth year?: ')
mob = input('what is you birth month (1 - 12)?: ')
dob = input('what day in the month?: ')
cyr = input('in which year are you?: ')

# subtract the year of birth from the current year
age = int(cyr) - int(yob)
#print(name, " you were born on: ", dob, "-", mob, "-", yob)
##print(name, "You are", age, end=" ")
#print("years old")
#calculating weight

height = input("what's your height(in meters)?: ")
weight = input("whats your weight(in kg)? ")
mbi = (float(weight) / (float(height) * float(height)))

print(name, " you were born on: ", dob, "-", mob, "-", yob)
print("and you are", age, end=" ")
print("years old")

#check the age with the bmi and advice accordingly
i = 25

#while(i): this causes infinite loop
# i += 1: incrementing it makes the infinite loop worse.

if(i > mbi and age < 30):
      print("wow,", name, """you are in good shape, maintain it.""")
elif(i > mbi and age > 30):
      print(name, """Good job for maintaining this shape at your current age.""")
elif(i < mbi and age < 30):
      print(name, """YOU ARE OVER-WEIGHT! you are too young to be over weight""")
elif(i < mbi and age > 30):
    print("Dear,", name, """your age suggests that you should exercise more and change your diet to none-fatty foods and less of sugar. You are over-weight""")
else:
     print(name, """I, cannot calculate your age and mbi with Zero data""")
#print(name, "Your mbi is: ", mbi)

#closing remarks
print(name, "Thanks for stopping by, see you next time")
