import webapp2
import randomName
import randomCityAndState
import randomHeightAndWeight

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

    def __str__(self):
        return Worker.__str__(Worker()) + \
               str(self.type)
        

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
