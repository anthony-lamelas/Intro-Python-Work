class Pet:
    
    def __init__(self, name, ptype, age):
        self.name = name
        self.type = ptype
        self.age = age
        self.fave_treats = []
        
    def rename(self, new_name):
        self.name = new_name
        
    def birthday(self):
        self.age += 1
        
    def add_treat(self, treat):
        self.fave_treats.append(treat)
        
    def __str__(self):
        treats = ""
        for treat in self.fave_treats:
            treats += treat + "\n"
            
        return f"{self.name} is a {self.type} that is {self.age} years old. \nFavorite treats: \n{treats}"
        
def main():
    plist = []
    response = ""
    while response.lower() != "q":
        response = input("Enter a command: ")
        
        if response == "adopt":
            name = input("What is the name of the pet? ")
            ptype = input("What type of pet is it? ")
            age = int(input("What is the age of the pet? "))  
            animal_name = Pet(name, ptype, age)
            plist.append(animal_name)

        elif response == "rename":
            old_name = input("What is the current name of the pet? ")
            new_name = input("What do you want the new name to be? ")
            for pet in plist:
                if pet.name == old_name:
                    pet.rename(new_name)

        elif response == "birthday":
            bname = input("What is the name of the pet? ")
            for pet in plist:
                if pet.name == bname:
                    pet.birthday()

        elif response == "treat":
            pname = input("What is the name of the pet? ")
            tname = input("What is the name of the treat? ")
            for pet in plist:
                if pet.name == pname:
                    pet.add_treat(tname)

        elif response == "pets":
            for pet in plist:
                print(pet)
        
            

main()

       
       
            
            