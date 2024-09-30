#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]
    def __init__(self, name = 'Keith', breed= "Mastiff"):
          self.name = name
          self.breed = breed

    @property
    def name(self):
        return self._name
    
    @property
    def breed(self):
        return self._breed
    

    @name.setter    
    def name(self, value):
        if isinstance(value,str) and 1 <= len(value) <= 25:
            self._name = value
        else:
           print("Name must be string between 1 and 25 characters.")

    @breed.setter
    def breed(self, value):
        if value in Dog.APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")     