from light import Light
from heating import Heating
from music import MusicPlayer

# create a Light object
light01 = Light() # call the constructor __init__ to create an object
# access the attributes of the object
print(light01.name)
print(light01.type)
print(light01.level)
print(light01.status)
# call the methods of the object
light01.turn_on()
light01.increase()
# Do the same for Heating and MusicPlayer
heating01 = Heating()
print(heating01.name)
print(heating01.type)
print(heating01.level)
print(heating01.status)
heating01.turn_on()
heating01.decrease()

music01 = MusicPlayer()
print(music01.name)
print(music01.type)
print(music01.level)
print(music01.status)
music01.turn_on()
music01.play()
music01.next()
music01.next()
music01.pause()