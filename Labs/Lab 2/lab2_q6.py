venom= bool()
large = bool()
aggro = bool()

input1= str(input("Is the snake venomous?"))
input2= str(input("Is the snake large?"))
input3= str(input("Is the snake aggressive?"))
if input1 == "yes":
    venom = True
elif input1 == "no":
    venom = False
    
if input2 == "yes":
    large = True
elif input2 == "no":
    large = False
    
if input3 == "yes":
    aggro = True
elif input3 == "no":
    aggro = False
    
    
    

if venom == True:
    if large == True:
        if aggro == True:
            print("That is a C++ Cobra. It evolved from the C Serpents many years ago. Reports show they have the weird habit of pointing at objects with their tails.")
        elif aggro == False:
            print("That is a C Serpent. It can be found in the sea. Has the ability to control their memory, being able to allocate parts of their brain for certain tasks and permanently delete information from their memories.")
    elif large == False:
        if aggro == True:
            print("That is a Matlab Mamba. It is commonly used to introduce mech-ies to working with snakes. They often hatch plots to catch their prey and enjoy graphical images.")
        elif aggro == False:
            print("That is a Verilog Viper. : Many people first see these snakes around architectures. Reports claim that they like to chew on circuit wires.")
            
elif venom == False:
    if large == True:
        if aggro == True:
            print("That is a Assembly Anaconda. Many people hate learning about these snakes, as they look very intimidating. In the Totally Official CS1114 Snake Register, they are said to love being in low level altitudes.")
        elif aggro == False:
            print("This is an Assembly Anaconda. : Many people hate learning about these snakes, as they look very intimidating. In the Totally Official CS1114 Snake Register, they are said to love being in low level altitudes.")
    elif large == False:
        if aggro == True:
            print("That is a Javascript Treesnake. Despite its name, they are completely different from the Java Kingsnake. They like to lay on the nodes of a tree to browse through nearby animals for their next meal. ")
        elif aggro == False:
            print("That is a Java Kingsnake. It is very befitting of their name, they are objectively the most sophisticated snake species. One may even say they are very classy")