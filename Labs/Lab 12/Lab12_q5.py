class Pirate:
    def __init__(self, name, loot=0):
        self.name = name
        self.loot = loot
        self.status = "Solo"

    def __str__(self):
        return f"{self.status} {self.name}"

    def update_loot(self, loot_change):
        self.loot += loot_change
        if self.loot < 0:
            self.loot = 0

    def update_status(self, status):
        self.status = status

    def get_loot(self):
        return self.loot


class Crew:
    def __init__(self, name):
        self.name = name
        self.pirates = []
        self.captain = None  # Initialize captain as None
        self.total_loot = 0

    def __str__(self):
        part_one = f"{self.name} under {self.captain} with the following crew members:\n"
        part_two = ""
        if self.pirates:
            for pirate in self.pirates:
                part_two += f"{pirate}\n"
        else:
            part_two = "No crew members yet."
        return part_one + part_two + f"With a total loot of: {self.total_loot}\n"

    def add_crew_member(self, pirate, role):
        self.pirates.append(pirate)
        self.total_loot += pirate.loot
        if role == "Captain" and self.captain is None:  # Check if captain slot is empty
            self.captain = pirate.name
        elif role == "Member":
            pirate.update_status("Member")  # Update status of member pirates
        else:
            return False  # Invalid role or captain slot already filled
        return True  # Successfully added member or captain

    def remove_crew_member(self, pirate):
        if pirate in self.pirates:
            self.pirates.remove(pirate)
            self.total_loot -= pirate.loot
            if pirate.name == self.captain:
                self.captain = None  # Reset captain if removed
            return True
        else:
            return False


def main():
    # Creating our pirates
    pirate_luffy = Pirate("Monkey D. Luffy")
    pirate_zoro = Pirate("Roronoa Zoro", 5)
    pirate_sanji = Pirate("Vinsmoke Sanji", 100)
    pirate_whitebeard = Pirate("Edward Newgate")
    pirate_marco = Pirate("Marco The Phoenix")
    pirate_ace = Pirate("Portgas D. Ace", 10)
    # Updating the loot of some pirates
    pirate_whitebeard.update_loot(40)
    pirate_sanji.update_loot(-20)
    pirate_marco.update_loot(-10)
    # Printing the current status of all our pirates
    all_pirates = [pirate_luffy, pirate_zoro, pirate_sanji,
                   pirate_whitebeard, pirate_marco, pirate_ace]
    for pirate in all_pirates:
        print(pirate, pirate.get_loot())
    print()
    # Creating our 2 crews
    strawhat_crew = Crew("Strawhat Crew")
    whitebeard_crew = Crew("Whitebeard Crew")
    # Print the empty crews
    print("---------------------------Printing empty crews---------------------------")
    print(strawhat_crew)
    print(whitebeard_crew)
    print()
    # Add members to each crew
    for pirate in all_pirates[:3]:
        is_pirate_added = strawhat_crew.add_crew_member(pirate, "Captain")
        if not is_pirate_added:
            strawhat_crew.add_crew_member(pirate, "Member")
    for pirate in all_pirates[3:]:
        is_pirate_added = whitebeard_crew.add_crew_member(pirate, "Captain")
        if not is_pirate_added:
            whitebeard_crew.add_crew_member(pirate, "Member")
    # Print the newly made crews
    print("---------------------------Printing the newly made crews---------------------------")
    print(strawhat_crew)
    print(whitebeard_crew)
    print()
    # Adding and removing a Pirate to a crew
    pirate_blackbeard = Pirate("Blackbeard", 50)
    # Removing a pirate not part of the crew
    whitebeard_crew.remove_crew_member(pirate_blackbeard)
    # Adding a Pirate to the crew then removing the pirate
    whitebeard_crew.remove_crew_member(pirate_whitebeard)
    whitebeard_crew.add_crew_member(pirate_blackbeard, "Captain")
    print("---------------------------Printing the new crew after captain changes---------------------------")
    print(whitebeard_crew)
    print(pirate_whitebeard)


main()
