# @author Emaad Gafoor
# ADD CODE -- import the Pet class from Pet.py
from Pet import Pet

# ADD CODE -- Assign to a variable named dog a new Pet object with
# no parameters sent to the constructor
dog = Pet()

# ADD CODE -- Assign to a variable named cat a new Pet object with a
# name of "Jack" and a weight of 3.5 sent to the constructor
cat = Pet("Jack", 3.5)

print(dog)
print(cat)
# ADD CODE -- Use the set methods and method chaining to change the dog's
# name to Spot and the weight to 10.5. This is one line of code.
dog.setName("Spot").setWeight(10.5)

print(dog)
cat.setWeight(-2.5)
print(cat)