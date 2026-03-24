## 
# class Person represents a person with a name
# @author M. Van Gorp
class Person : 
    # Constructor
    def __init__(self, name = "") :
        self.setName(name)

    ## getName gets the person's name.
    #  @return the current name   
    def getName(self) :
        return self._name

    ## SetName sets the person's name
    #  @param name the new name   
    def setName(self, name) :
        self._name = name