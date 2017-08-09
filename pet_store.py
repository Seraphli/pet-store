#!/usr/bin/env python

import argparse
import pickle
import os


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


class PetStore(object):
    """This is pet store"""

    def __init__(self):
        """There are untold cages"""
        self.__cages = []

    def load_state(self):
        if os.path.exists('pet_store.state'):
            with open('pet_store.state', 'r') as f:
                self.__cages = pickle.load(f)

    def save_state(self):
        with open('pet_store.state', 'w') as f:
            pickle.dump(self.__cages, f)

    def put_pet(self, pet):
        """Leave your pet in the pet store
        
        Args:
            pet (Pet): your pet
        """
        self.__cages.append(pet)

    def get_pet(self, owner):
        for pet in self.__cages:
            if pet.owner == owner:
                yield pet

    def pets_party(self):
        for pet in self.__cages:
            pet.shout()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--owner', required=True, metavar='Peter',
                        type=str, help='owner of pets')
    parser.add_argument('--pet', action='append', metavar='Pet-Name',
                        type=str, help='put your pets here')
    return parser.parse_args()


def main():
    args = parse_args()
    store = PetStore()
    store.load_state()
    owner = args.owner
    if args.pet:
        for arg in args.pet:
            pet_type = arg[:arg.index('-')]
            pet_name = arg[arg.index('-') + 1:]
            if pet_type in PET_TYPE.keys():
                p = PET_TYPE[pet_type](owner, pet_name)
                p.shout()
                store.put_pet(p)
    else:
        for idx, pet in enumerate(store.get_pet(owner)):
            print('{:>3}. {} {}'.format(idx + 1, pet.__class__.__name__, pet.name))
    store.save_state()


if __name__ == '__main__':
    main()
