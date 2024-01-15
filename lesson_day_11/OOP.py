class Human:
    def __init__(self, name, age, head, body, legs, hands):
        self.name = name
        self.age = age
        self.head = head
        self.body = body
        self.legs = legs
        self.hands = hands

    def say_hello(self):
        print(f'Hello, my name is {self.name}, I am {self.age} years old')

EnkhAldar = Human('Enkh-Aldar', 21, 1, 1, 2, 2)
EnkhAldar.say_hello()

class Animal:
    def __init__(self, name, age, race, gender):
        self.name = name
        self.age = age
        self.race = race
        self.gender = gender
    def make_sound(self, sound):
        print('I make a sound: ', sound)

dog = Animal('Bankhar', 1, 'Tuvd Bankhar', 'male')
dog.make_sound('Woof Woof')
bear = Animal('Goviin bor', 2, 'Mazaalai', 'female')
bear.make_sound('Grrrrr')
bird = Animal('Khun', 3, 'Usnii Shuwuu', 'male')
bird.make_sound('Chirp Chirp')


class Father:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    
    
    def say_hello(self):
        print(f'Hello, my name is {self.name}, I am {self.age} years old, I have nationality {self.nationality} ')
        

class Son(Father):
    def greeting(self):
        print('Hello, I am son')
        
class Daugther(Father):
    def greeting(self):
        print('Hello, I am daughter')
        
byambadorj = Father('Byambadorj', 55, 'Mongolian')
byambadorj.say_hello()
EnkhAldar = Son('Enkh-Aldar', 21, 'Mongolian')
EnkhAldar.greeting()
EnkhAldar.say_hello()
Enkhjargal = Daugther('Enkhjargal', 30, 'Mongolian')
Enkhjargal.greeting()
Enkhjargal.say_hello()

