from __future__ import annotations
from abc import ABC, abstractmethod

class IMultiValueDictionary(ABC):

    # Returns all the keys in the dictionary. Order is not guaranteed.
    @abstractmethod
    def getKeys(self):
        raise NotImplementedError
    
    # Returns the collection of strings for the given key. 
    # Return order is not guaranteed. Returns an error if the key does not exists.
    @abstractmethod
    def getValues(self, key):
        raise NotImplementedError
    
    # Add a member to a collection for a given key. 
    # Displays an error if the value already existed in the collection.
    @abstractmethod
    def add(self, key, value):
        raise NotImplementedError
    
    # Removes a value from a key. 
    # If the last value is removed from the key, they key is removed from the dictionary. 
    # If the key or value does not exist, displays an error.
    @abstractmethod
    def remove(self, key, value):
        raise NotImplementedError
    
    # Removes all value for a key and removes the key from the dictionary. 
    # Returns an error if the key does not exist.
    @abstractmethod
    def removeAll(self, key):
        raise NotImplementedError
    
    # Removes all keys and all values from the dictionary.
    @abstractmethod
    def clear(self):
        raise NotImplementedError
    
    # Returns whether a key exists or not.
    @abstractmethod
    def containKey(self, key):
        raise NotImplementedError

    # Returns whether a value exists within a key. 
    # Returns false if the key does not exist.
    @abstractmethod
    def containValue(self, key, value):
        raise NotImplementedError
    
    # Returns all the values in the dictionary. 
    # Returns nothing if there are none. Order is not guaranteed.
    @abstractmethod
    def allMembers(self, key, value):
        raise NotImplementedError
    
    # Returns all keys in the dictionary and all of their values. 
    # Returns nothing if there are none. Order is not guaranteed.
    @abstractmethod
    def items(self, key, value):
        raise NotImplementedError