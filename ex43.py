from sys import exit
from random import randint
from textrap import dedent
class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.ennter()
            current_scene =  self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()

        

class Death(Scene):
    quips = [ "You died.", "Your Mom wourld be proud....if she were smarter", "Such a luser", "I have a small puppy that's better", "You're worse than your Dad's jokes." ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""Quick on the draw you yank out your blaster and fire it at the Gothon.His clown costume is following ans moving around his body"""))

        action = input("> ")

        if action == "dodge!":
            print(dedent("""Like a world classs boxer you dodge,weave, slip and slide right as the Gothon's blaster cranks a laser past your head."""))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""Lucky for you they make you learn Gothon insults in the academy.You tell the one Gothon joke you know:Lbhe zbgure vf fb sng, jura fur fvgf nevhaq gur ubhfr,not to laugh"""))
            return 'laser_weapon_aromy'
        else:
            pint("DOES NOT COMPUTE")
            return 'cnetral_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""You do a drive roll into the Weapon Armory""""))

        code = f"{randint(1,9){randint(1,9)}{randint(1,9)}"
        guess = input("[keyboard]> ")
        guesses = 0

        while guess != code and gusses < 10:
            print("BZZZZEDDD !")
            gusses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""The container clicks open and the seal breaks"""))
            return 'death'


class TheBridge(Scene):
     
    def enter(self):
         print(dedent("""You burst  onto the Bridge with the netron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship."""))

         action = input("> ")

         if action == "throw the bomb""

         print(dedent("""In a panic you throw the bomb at the group of Gothons and make a leap for the door."""))
         return 'death'

        elif action == "slowly place the bomb":
        print(dedent("""You point your blaster at the bomb under your arm and the Gothons put their hands yp and start to sweat."""))
        return 'escape_pod'

        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
    print(dedent("""you rush through the ship desperately trying to make it to the escape pod before the whole ship explodes."""))

    good_pod  = randint(1,5)
    guess = input("[pod #]> ")

    if int(guess) != good_pod:
    print(dedent("""You jump into pod {guess} and hit the eject button.The pod easily slides out into space heading to the planet below."""))
    return 'death'

    else:
        print(dedent("""You Jump into pod {guess} and hit the eject button.The pod easily slides out into space heading to the planet below."""))
        return 'finished'

class Finisher(Scene):

            def enter(self):
                print("you won! Good job.")
                return 'finished'

class Map(object):

    scences = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death': Death(),
            'finished': Finished(),
            }

    def __init__(self,start_scence):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scences.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
