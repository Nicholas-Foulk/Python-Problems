from sys import exit
from random import randint

#this is something ill come back to.
#in this example we are going to every location

class Scene(object):
    
    def enter(self):
        print "This scene is not yet configured."
        exit(1)

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        current_scene.enter()
        

class Death(Scene):
    quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]
    def enter(self):
        print Death.quips[randint(9,len(self.quips-1))]
        exit(1)
        
class UnitedStates(Scene):
    
    def enter(self):    
        print "Here we have a country bordered two continental oceans, the Pacific and Atlantic."
        print "The current population is 315 million people."
        print "The average age is around 41 years old."
        print "The current economy supports a large trade deficit."
        print "The demographic is around 60% american, 20% Hispanic, 13% African-American, and %7 miscelleanous."
        print "The country is considered developed and first-world."
        return 'UnitedKingdom'
            
            
            
        
class UnitedKingdom(Scene):

    def enter(self):
        print " Here we see a country that recently departed from the European Union, which has been a very controversial decision"
        print " the past few months. The older generation was known for voting to leave the Union while the younger generation voted"
        print " to stay. When the country first decided to enter the Union, it was the older generation for voted for joining. "
        print " Leaving the Union is known for having the effect of allowing U.K.'s government to change trading, immigrating, and "
        print " local policies. It is my opinion that seperating from the European Union allows for independence "
        print " It is my opinion that seperating from the European Union allows for independence between countries and as a result "
        print " will be better for the local economy. The public believes the economy will do horribly without the European Union "
        print " because the European Union will not negotiate good trading deals with the U.K."
        print "Neo liberalism agenda seems to support the idea of having open borders between all countries and I see that as bad because"
        print "it lowers the quality of living in more developed countries while raising the quality of living in poorer countries at the"
        print "same time."
        return 'Japan'

class Japan(Scene):

    def enter(self):
       print " Here we see a country that recently departed from the European Union, which has been a very controversial decision "
       print " the past few months. The older generation was known for voting to leave the Union while the younger generation voted "
       print " to stay.\n When the country first decided to enter the Union, it was the older generation for voted for joining. "
       print " Leaving the Union is known for having the effect of allowing U.K.'s government to change trading, immigrating, and "
       print " local policies. "
       print " It is my opinion that seperating from the European Union allows for independence between countries and as a result "
       print " will be better for the local economy. The public believes the economy will do horribly without the European Union "
       print " because the European Union will not negotiate good trading deals with the U.K."
       print " Neo liberalism agenda seems to support the idea of having open borders between all countries and I see that as bad because"
       print " it lowers the quality of living in more developed countries while raising the quality of living in poorer countries at the"
       print " same time."
       return 'Canada'

class Canada(Scene):

    def enter(self):     
        print " Here we see a country that recently departed from the European Union, which has been a very controversial decision "
        print " the past few months. The older generation was known for voting to leave the Union while the younger generation voted "
        print " to stay.\n When the country first decided to enter the Union, it was the older generation for voted for joining. "
        print " Leaving the Union is known for having the effect of allowing U.K.'s government to change trading, immigrating, and "
        print " local policies."
        print " It is my opinion that seperating from the European Union allows for independence between countries and as a result will "
        print " be better for the local economy. The public believes the economy will do horribly without the European Union because "
        print " the European Union will not negotiate good trading deals with the U.K."
        print " Neo liberalism agenda seems to support the idea of having open borders between all countries and I see that as bad because"
        print " it lowers the quality of living in more developed countries while raising the quality of living in poorer countries at the"
        print " same time."
        return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        exit(1)
        
class Map(object):

    scenes = {
        'UnitedStates': UnitedStates(),
        'UnitedKingdom': UnitedKingdom(),
        'Japan': Japan(),
        'Canada': Canada(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)  
        
a_map = Map('UnitedStates')
a_game = Engine(a_map)
a_game.play()
