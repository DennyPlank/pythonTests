import random
class Person:

    def __init__(self, first_name, last_name, health, status):
        """ 
        intitialize attributes to be unsed in for a
        class methods of this class.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hello, my name is {} {}.".format(self.first_name, self.last_name))

    def emotion(self):
        emotion = random.randrang(1,3)
        if emotion == 1:
            print("{} is happy".format(self.first_name))
        if emotion == 2:
            print("{} is sad".format(self.first_name))
        if emotion == 3:
            print("{} is angry".format(self.first_name))
    
Dennis = Person("Dennis", "Plank", 95, status=True)
Ray = Person("Ray", "Jones", 44, status=False)
Sara = Person("Sara", "Plank", 88, status=True)

print("{} is my friend? {}".format(Dennis.first_name, Dennis.status))

# class Enemy(Person):
#     def __inti__(self, weapon, first_name, last_name, health, status):
#         super().__init__(first_name, last_name, health, status)
#         self.weapon = weapon

#         def hurt(self, other):
#             if self.weapon == "rock":
#                 other.health -= 10
#             elif self.weapon == 'stick':
#                 other.health -= 5
#             print(other.health)

#         def insult(self, other)