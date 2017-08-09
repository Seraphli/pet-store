class Animal(object):
    """Animal class"""

    def __init__(self, voice):
        """Initialize an animal
        
        Args:
            voice (str): different animals have different voices
        """
        self.__voice = voice

    def shout(self):
        """Animal can shout with their voice"""
        print(self.__voice)


class Horse(Animal):
    def __init__(self):
        super(Horse, self).__init__('Neigh~')


class Pet(Animal):
    pass


class Cat(Pet):
    def __init__(self):
        super(Cat, self).__init__('Meow~')


class Dog(Pet):
    def __init__(self):
        super(Dog, self).__init__('Woof!')


class PetStore(object):
    """This is pet store"""

    def __init__(self):
        """There are untold cages"""
        self.cages = []

    def put_pet(self, pet):
        """Leave your pet in the pet store
        
        Args:
            pet (Pet): your pet
        """
        self.cages.append(pet)
