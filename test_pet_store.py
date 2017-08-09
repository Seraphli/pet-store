import unittest
from pet_store import *


class TestPetStore(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cat(self):
        lily = Cat()
        lily.shout()

    def test_dog(self):
        sam = Dog()
        sam.shout()

    def test_pet_store(self):
        store = PetStore()
        lily = Cat()
        store.put_pet(lily)
        sam = Dog()
        store.put_pet(sam)
        jim = Horse()
        # There is a note in PyCharm showing a type error
        # But you can run this code without errors
        store.put_pet(jim)
        for pet in store.cages:
            pet.shout()


if __name__ == '__main__':
    unittest.main()
