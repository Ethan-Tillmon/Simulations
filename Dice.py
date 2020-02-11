import random

roll = random.randint(1,6)
numRolls = int(input("How many rolls? "))

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0

i = 0
while(i < numRolls):
    roll = random.randint(1,6)
    print(roll)
    if(roll == 1):
        counter1 += 1
    if(roll == 2):
        counter2 += 1
    if(roll == 3):
        counter3 += 1
    if(roll == 4):
        counter4 += 1
    if(roll == 5):
        counter5 += 1
    if(roll == 6):
        counter6 += 1

    i += 1

print("Number of 1: " + str(counter1))
print("Percent of 1: " + str(counter1 / numRolls * 100) + "%")
print("Number of 2: " + str(counter2))
print("Percent of 2: " + str(counter2 / numRolls * 100) + "%")
print("Number of 3: " + str(counter3))
print("Percent of 3: "  + str(counter3 / numRolls * 100) + "%")
print("Number of 4: " + str(counter4))
print("Percent of 4: " + str(counter4 / numRolls * 100) + "%")
print("Number of 5: " + str(counter5))
print("Percent of 5: " + str(counter5 / numRolls * 100) + "%")
print("Number of 6: " + str(counter6))
print("Percent of 6: " + str(counter6 / numRolls * 100) + "%")


