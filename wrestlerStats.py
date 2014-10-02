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

def assignOverall(style, strength, aerial, grappling, striking, movement):
    
    if (style == "Power House"):
        return int(strength*.4+aerial*.15+grappling*.15+striking*.15+movement*.15)
    elif (style == "High Flyer"):
        return int(strength*.15+aerial*.4+grappling*.15+striking*.15+movement*.15)
    elif (style == "Technical"):
        return int(strength*.15+aerial*.15+grappling*.4+striking*.15+movement*.15)
    elif (style == "Brawler"):
        return int(strength*.15+aerial*.15+grappling*.15+striking*.4+movement*.15)
    elif (style == "Fast Paced"):
        return int(strength*.15+aerial*.15+grappling*.15+striking*.15+movement*.4)

def assignPopularity(microphone, look, charisma, selling, psychology, grit, honor):

    return (microphone*.18+look*.18+charisma*.18+selling*.18+psychology*.18+
            grit*.05+honor*.05)
    
def assignCharacterStats(weight):
    if (weight > 300):
        stamina = random.randrange(handicap)
    else:
        stamina = random.randrange(top)
    grit = random.randrange(top)
    honor = random.randrange(top)
    return stamina, grit, honor


    
