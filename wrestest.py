import webapp2
import randomName
import randomCityAndState
import randomHeightAndWeight
import wrestlerStats

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(Wrestler())

class Worker(object):

    def __init__(self):
        self.first = randomName.random_name('first_names.txt')
        self.last = randomName.random_name('last_names.txt')
        self.city, self.state = randomCityAndState.random_city_and_state('cities_and_states_short.txt')
        self.height, self.weight = randomHeightAndWeight.random_height_and_weight()

    def __str__(self):
        return str(self.first)+' '+str(self.last) + '\n' \
               + str(self.city) + str(self.state) + '\n' \
               + str(self.height) + ' ' + str(self.weight) + '\n'

class Wrestler(Worker):
    def __init__(self):
        Worker.__init__(self)
        self.type = "Wrestler"
        self.style = wrestlerStats.assignStyle(self.weight)
        self.strength, self.aerial, self.grappling, self.striking, self.movement \
                       = wrestlerStats.assignPhysicalStats(self.style)
        self.microphone, self.look, self.charisma, self.selling, self.psychology \
                       = wrestlerStats.assignEntertainmentStats()
        self.overall = wrestlerStats.assignOverall(self.style, self.strength, self.aerial, self.grappling,
                                                   self.striking, self.movement, self.microphone, self.look,
                                                   self.charisma, self.selling, self.psychology)
    
    def __str__(self):
        return Worker.__str__(self) + \
               "Type:       " + str(self.type) + '\n' + \
               "Style:      " + str(self.style) + '\n' + \
               "Overall:    " + str(self.overall) + '\n' + \
               "Strength:   " + str(self.strength) + '\n' + \
               "Aerial:     " + str(self.aerial) + '\n' + \
               "Grappling:  " + str(self.grappling) + '\n' + \
               "Striking:   " + str(self.striking) + '\n' + \
               "Movement:   " + str(self.movement) + '\n' + \
               "Microphone: " + str(self.microphone) + '\n' + \
               "Look:       " + str(self.look) + '\n' + \
               "Charisma:   " + str(self.charisma) + '\n' + \
               "Selling:    " + str(self.selling) + '\n' + \
               "Psychology: " + str(self.psychology)
    

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
