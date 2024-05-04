class Animal:
    
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_sick = False
        
        
    def __str__(self):
        sick_status = "Yes" if self.is_sick else "No"
        return f"{self.name} the {self.species}, Age: {self.age}, Sick: {sick_status}"
    
    def mark_sick(self):
        self.is_sick = True
        
    def mark_healthy(self):
        self.is_sick = False
        
        
class Clinic:
    
    def __init__(self):
        self.animals = []
        
    def __str__(self):
        returned_animals = ""
        if not self.animals:
            return f"The clinic is currently empty."
        else:
            for animal in self.animals:
                returned_animals += f"{animal.name} the {animal.species}, Age: {animal.age}, Sick: {animal.is_sick} \n"
            return returned_animals
        
    def add_animal(self,animal):
        self.animals.append(animal)
        
    def find_animal(self,name):
        for animal in self.animals:
            if name == animal.name:
                return animal  
        else:
            return None
        
    
def main():
    clinic = Clinic()
    clinic.add_animal(Animal("Buddy", "Dog", 5))
    clinic.add_animal(Animal("Whiskers", "Cat", 3))
    clinic.add_animal(Animal("Tweety", "Bird", 2))
    print("Listing all animals in the clinic:")
    print(clinic)
    print("\nMarking 'Whiskers' as sick .")
    cat = clinic.find_animal("Whiskers")
    if cat:
        cat.mark_sick()
        print("\nListing all animals after marking 'Whiskers' sick:")
    print(clinic)

main()
        
    
                
    
    
