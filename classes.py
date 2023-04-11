class person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def info(self):
        print( f"First Name : {self.first_name} \nLast name : {self.last_name} \nAge : {self.age}" )

bob = person("bob", "smith", 21)

print(bob.first_name)
