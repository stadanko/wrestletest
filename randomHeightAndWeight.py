import random

##Height range is 66 to 91 inches
##Most common range is 72 to 78 inches / Used 70%
##Least common range is 66 to 91 inches / Used 30%
##Weight range is 160 to 400 lbs
##range for 66 to 71 is 160 to 200
##range for 72 to 78 is 201 to 280
##range for 79 to 91 is 281 to 400

def random_height_and_weight():
    height, inches = random_height()
    return height, random_weight(inches)

def random_height():

    roll = random.randrange(1, 11)
    if (roll <= 7):
        return getHeightFromRange(70, 78)
    else:
        return getHeightFromRange(66, 91)

def random_weight(height):
    if (height < 70):
        weight = random.randrange(160, 201)
    elif(height < 79):
        weight = random.randrange(201, 281)
    else:
        weight = random.randrange(281, 401)
    return weight

def getHeightFromRange(low, high):
    inches = random.randrange(low, high+1)
    return str(inches/12) + "'" + str(inches%12) + '"', inches
