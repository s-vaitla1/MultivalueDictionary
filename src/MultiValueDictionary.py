from src.IMultiValueDictionary import IMultiValueDictionary

class MultiValueDictionary(IMultiValueDictionary):

    def __init__(self):
        self.dict_ = dict()

    def getKeys(self):
        """Override getKeys method"""
        # print all keys in the dictionary
        for i, key in enumerate(self.dict_.keys()):
            print("{}) {}".format((i+1), key))
        
        # if no keys exist in the dictionary then print the appropriate message
        if len(self.dict_.keys()) == 0:
            print("(empty set)")
    
    def getValues(self, key):
        
        # if key does not exist then print an error
        if key not in self.dict_.keys():
            print("ERROR, key does not exist.")
            return
        
        # print all values for a given key
        for i, value in enumerate(self.dict_[key]):
            print("{}) {}".format((i+1), value))

    def add(self, key, value):

        # if key does not exist then add the key and value to the dictionary
        if key not in self.dict_.keys():
            self.dict_[key] = [value]
            print(") Added")
            return
        
        # if value already exists in the key then print the error
        if value in self.dict_[key]:
            print(") ERROR, value already exists")
            return

        # if key already exists then add only the value to that key
        self.dict_[key].append(value)
        print(") Added")

    def remove(self, key, value):

       # if value does not exist in the key then print the error
        if value not in self.dict_[key]:
            print(") ERROR, value does not exist")
            return

       # if the value exists in the key and is the last value for the key then remove key 
        if value in self.dict_[key]:
            if len(self.dict_[key]) == 1:
                del self.dict_[key]
                print(") Removed")
                return

        # if the value exists then remove the value   
        self.dict_[key].remove(value)
        print(") Removed")
        
    def removeAll(self, key):

        # if key does not exist then print the error
        if key not in self.dict_.keys():
            print(") ERROR, key does not exist")
            return

        # if key exists then remove all the values from the key and the key itself
        del self.dict_[key]
        print(") Removed")

    def clear(self):
        # remove all keys and values from the dictionary
        self.dict_.clear()
        print(") Cleared")

    def containKey(self, key):

        # if key exists in the dictionary then print true
        if key in self.dict_.keys():
            print(") true")
            return

        # if key doesn't exist in the dictionary
        print(") false")

    def containValue(self, key, value):
        
        # if value exists in the dictionary then print true
        if value in self.dict_[key]:
            print(") true")
            return

        # if value doesn't exist in the dictionary
        print(") false")
    
    def allMembers(self):

        # if even one key exists then print all values for the key 
        if self.dict_.keys():
            for i, key in enumerate(self.dict_.keys()):
                for j, value in enumerate(self.dict_[key]):
                    print(value)
            return
        
        # if no keys exist in the dictionary
        print("(empty set)")
        
    def items(self):

        # if even one key exists then print all the values along with the key 
        if self.dict_.keys():
            for i, key in enumerate(self.dict_.keys()):
                for j, value in enumerate(self.dict_[key]):
                    print("{}: {}".format(key, value))
            return

        # if no keys exist in the dictionary
        print("(empty set)")