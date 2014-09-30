import random

def random_city_and_state(filename):

    ##Read in file
    infile = open(filename, 'r')

    ##Initialise Variables and lists
    city_list = []
    state_list = []
    line = infile.readline()

    while line != '':
        line = line.rstrip('\n')

        end = line.index(' city')
        comma = line.index(', ')
        city = line[0:end]
        state = line[comma:]
        
        city_list.append(city)
        state_list.append(state)
        line = infile.readline()
        
    infile.close()

    randomNum = random.randrange(len(city_list))


    
    return city_list[randomNum], state_list[randomNum]
