import random
top = 101

def assignStyle(weight):
    coinFlip = random.randrange(2)
    if (weight > 280):
        return "Power House"
    elif(weight > 230):
        if (coinFlip == 0):
            return "Brawler"
        else:
            return "Technical"
    elif(weight > 200):
        if (coinFlip == 0):
            return "Fast Paced"
        else:
            return "Technical"
    else:
        return "High Flyer"

def assignPhysicalStats(style):
    
    if (style == "Power House"):
        
        strength =  random.randrange(top)
        aerial =    random.randrange(top)
        grappling = random.randrange(top)
        striking =  random.randrange(top)
        movement =  random.randrange(top)
        
        return strength, aerial, grappling, striking, movement
    
    elif (style == "Brawler"):
        
        strength =  random.randrange(top)
        aerial =    random.randrange(top)
        grappling = random.randrange(top)
        striking =  random.randrange(top)
        movement =  random.randrange(top)
        
        return strength, aerial, grappling, striking, movement

    elif (style == "Technical"):
        
        strength =  random.randrange(top)
        aerial =    random.randrange(top)
        grappling = random.randrange(top)
        striking =  random.randrange(top)
        movement =  random.randrange(top)
        
        return strength, aerial, grappling, striking, movement

    elif (style == "Fast Paced"):
        
        strength =  random.randrange(top)
        aerial =    random.randrange(top)
        grappling = random.randrange(top)
        striking =  random.randrange(top)
        movement =  random.randrange(top)
        
        return strength, aerial, grappling, striking, movement

    elif (style == "High Flyer"):
        
        strength =  random.randrange(top)
        aerial =    random.randrange(top)
        grappling = random.randrange(top)
        striking =  random.randrange(top)
        movement =  random.randrange(top)
        
        return strength, aerial, grappling, striking, movement
    
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
    
