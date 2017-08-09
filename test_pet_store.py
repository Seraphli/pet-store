import unittest
from pet_store import *


class TestPetStore(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cat(self):
        lily = Cat('Peter', 'Lily')
        lily.shout()

    def test_dog(self):
        sam = Dog('Peter', 'Sam')
        sam.shout()

    def test_pet_store(self):
        store = PetStore()
        lily = Cat('Peter', 'Lily')
        store.put_pet(lily)
        sam = Dog('Peter', 'Sam')
        store.put_pet(sam)
        jim = Horse()
        # There is a note in PyCharm showing a type error
        # But you can run this code without errors
        store.put_pet(jim)
        store.pets_party()


if __name__ == '__main__':
    unittest.main()
