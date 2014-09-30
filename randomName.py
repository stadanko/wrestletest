import random

##Random name generator
def random_name(filename):
    
    ##Read in file
    infile = open(filename, 'r')

    ##Initialise Variables and lists
    name_list = []
    weight_list = []
    line = infile.readline()

    while line != '':
        line = line.rstrip('\n')
        
        ##Slice and create name and probability variables
        end = line.index(' ')
        name = line[0:end]
        ##weight = float(line.rsplit(' ', 1)[1])

        ##add name and probability to lists with matching indices. 
        name_list.append(name)
        ##weight_list.append(weight)

        line = infile.readline()
    infile.close()

    ##Calculate weight in terms of percent
    ##Meant to be able to choose a name more often based on popularity
    ##Not currently being used in function
##    totalWeight = sum(weight_list)
##    count = 0
##    for w in weight_list:
##        weight_list[count] = (w*100)/totalWeight
##        count+=1
    
    return name_list[random.randrange(len(name_list))]
