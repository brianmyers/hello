from pprint import pprint
import logging

class Person:

    # All classes have an init function. The __init__() function is called automatically every time the 
    # class is being used to create a new object.
    # Use the __init__() function to assign values to object properties, or other operations that are 
    # necessary to do when the object is being created
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._ssn = None #non public access

    # The __str__() function controls what should be returned when the class object is represented as a string.
    def __str__(self):
        return f"{self.name}({self.age})"
    
    def __repr__(self):
        return str(vars(self))

    @property
    def ssn(self):
        return self._ssn
    
    @ssn.setter
    def ssn(self, value):
        logging.debug("adding extra to the ssn")
        new_value = str(value) + "-0000"
        self._ssn = new_value

    @ssn.deleter
    def ssn(self):
        del self._ssn
        
    def getMySecretPersonInfo(self):
        # The self parameter is the first parameter and is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        return str(self.ssn)