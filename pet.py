class Animal(object):
    """Animal class"""

    def __init__(self, voice):
        """Initialize an animal

        Args:
            voice (str): different animals have different voices
        """
        self._voice = voice

    def shout(self):
        """Animal can shout with their voice"""
        print(self._voice)


class Horse(Animal):
    def __init__(self):
        super(Horse, self).__init__('Neigh~')


class Pet(Animal):
    def __init__(self, owner, name, voice):
        super(Pet, self).__init__(voice)
        self.owner = owner
        self.name = name

    def shout(self):
        """Shout with their voice"""
        print("{}'s {}: {}".format(self.owner, self.name, self._voice))


class Cat(Pet):
    def __init__(self, owner, name):
        super(Cat, self).__init__(owner, name, 'Meow~')


class Dog(Pet):
    def __init__(self, owner, name):
        super(Dog, self).__init__(owner, name, 'Woof!')


PET_TYPE = {'Cat': Cat, 'Dog': Dog}
