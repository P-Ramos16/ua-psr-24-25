from colorama import Fore, Style

class Dog:
    def __init__(self):
        return 
            
    def initFromValues(self, name, color, age):
        self.name, self.color, self.age = name, color, age
        self.brothers = []  # no brothers for now
        return self

    def initFromDict(self, dict):
        
        self.name = dict["name"]
        self.color = dict["color"]
        self.age = dict["age"]
        
        self.brothers = []
        
        for br in dict["brothers"]:
            self.brothers.append(br)
            
        return self

    def addBrother(self, name):
        self.brothers.append(name)

    def __str__(self):
        return 'name: ' + Fore.RED + str(self.name) + Fore.RESET + \
               ', age: ' + Fore.RED + str(self.age) + Fore.RESET +\
               ', color: ' + Fore.RED + str(self.color) + Fore.RESET +\
               ', brothers: ' + Fore.BLUE + str(self.brothers) + Style.RESET_ALL
               
    def toDict(self):
        return {"name" : str(self.name),
                "age"  : str(self.age),
                "color": str(self.color),
                "brothers": self.brothers}