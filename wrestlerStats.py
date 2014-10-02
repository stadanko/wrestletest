import random
top = 101
handicap = 51

def assignPhysicalStats(weight):
    
    striking =  random.randrange(top)
    if (weight < 200):
        strength = random.randrange(handicap)
    else:
        strength = random.randrange(top)
    if (weight > 250):
        aerial = random.randrange(handicap)
    else:
        aerial = random.randrange(top)
    if (weight > 300):
        grappling = random.randrange(handicap)
    else:
        grappling = random.randrange(top)
    if (weight > 270):
        movement =  random.randrange(handicap)
    else:        
        movement =  random.randrange(top)
    
    return strength, aerial, grappling, striking, movement

def assignStyle(weight, strength, aerial, grappling, striking, movement):
    attributes = [strength, aerial, grappling, striking, movement]
    attributeValue = strength
    keyAttribute = 0
    for i in range(len(attributes)):
        if (attributes[i] > attributeValue):
            attributeValue = attributes[i]
            keyAttribute = i
        
    if (keyAttribute == 0):
        return "Power House"
    elif (keyAttribute == 1):
        return "High Flyer"
    elif (keyAttribute == 2):
        return "Technical"
    elif (keyAttribute == 3):
        return "Brawler"
    elif (keyAttribute == 4):
        return "Fast Paced"
    
def assignEntertainmentStats():
    
    microphone = random.randrange(top)
    look = random.randrange(top)
    charisma = random.randrange(top)
    selling = random.randrange(top)
    psychology = random.randrange(top)

    return microphone, look, charisma, selling, psychology

def assignOverall(style, strength, aerial, grappling, striking, movement,
                  microphone, look, charisma, selling, psychology):
    
    if (style == "Power House"):
        return int(strength*.2+aerial*.05+grappling*.1+striking*.1+movement*.1+
                microphone*.1+look*.1+charisma*.1+selling*.1+psychology*.1)
    elif (style == "High Flyer"):
        return int(strength*.1+aerial*.2+grappling*.1+striking*.1+movement*.05+
                microphone*.1+look*.1+charisma*.1+selling*.1+psychology*.1)
    elif (style == "Technical"):
        return int(strength*.1+aerial*.1+grappling*.2+striking*.05+movement*.1+
                microphone*.1+look*.1+charisma*.1+selling*.1+psychology*.1)
    elif (style == "Brawler"):
        return int(strength*.1+aerial*.1+grappling*.05+striking*.2+movement*.1+
                microphone*.1+look*.1+charisma*.1+selling*.1+psychology*.1)
    elif (style == "Fast Paced"):
        return int(strength*.05+aerial*.1+grappling*.1+striking*.1+movement*.2+
                microphone*.1+look*.1+charisma*.1+selling*.1+psychology*.1)
    return "xx"
    
def assignCharacterStats(weight):
    if (weight > 300):
        stamina = random.randrange(handicap)
    else:
        stamina = random.randrange(top)
    grit = random.randrange(top)
    honor = random.randrange(top)
    return stamina, grit, honor


    
