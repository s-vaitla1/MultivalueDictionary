from src.Commands import * 
from src.MultiValueDictionary import MultiValueDictionary

class MultiValueDictApp():
    
    def __init__(self):
        self.multiValueDictionary = MultiValueDictionary()
 
    def run(self, command, args):
        if command == KEYS:
            self.multiValueDictionary.getKeys()
        
        elif command == MEMBERS:
            try:
                self.multiValueDictionary.getValues(args[0])
            except IndexError:
                print(") ERROR, enter a key with the command")
        
        elif command == ADD:
            try:
                self.multiValueDictionary.add(args[0], args[1])
            except IndexError:
                print(") ERROR, enter a key and value with the command")
            
        elif command == REMOVE:
            try:
                self.multiValueDictionary.remove(args[0], args[1])
            except KeyError:
                print(") ERROR, both key and value don't exist")
            except IndexError: 
                print(") ERROR, key does not exist")
            
        elif command == REMOVEALL:
            try:
                self.multiValueDictionary.removeAll(args[0])
            except IndexError:
                print(") ERROR, enter a key with the command")
        
        elif command == CLEAR:
            self.multiValueDictionary.clear()
            
        elif command == KEYEXISTS:
            try:
                self.multiValueDictionary.containKey(args[0])
            except IndexError: 
                print(") false")
        
        elif command == VALUEEXISTS:
            try:
                self.multiValueDictionary.containValue(args[0], args[1])
            except KeyError:
                print(") false")
            except IndexError: 
                print(") ERROR, enter a key and value with the command")
        
        elif command == ALLMEMBERS:
                self.multiValueDictionary.allMembers()
        
        elif command == ITEMS:
                self.multiValueDictionary.items()

        elif command == EXIT:
            exit(1)
        
        else:
            print(") Command does not exists")