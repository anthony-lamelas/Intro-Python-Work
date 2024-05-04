"""
Author: [Anthony Lamelas]
Assignment / Part: HW11 - Problems 1-3
Date due: May 2, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

class Instrument:
    #1.1
    def __init__(self, model, brand, strength):
        self.model = model
        self.brand = brand
        self.strength = strength
    #1.2
    def __str__(self):
        return f"{self.brand} {self.model} ({self.strength * 100} / 100 strength)"
    #1.3
    def does_break(self):
        import random
        rand = random.random()
        if rand < (self.strength / 2):
            return True
        else:
            return False

class Musician:
    #2.1
    def __init__(self, stage_name, instruments):
        self.stage_name = stage_name
        self.instruments = instruments
        self.number_of_instruments = len(self.instruments)
    #2.2
    def __str__(self):
        part_one = f"Musician object '{self.stage_name}', owning a "
        part_two = ""
        for instrument in self.instruments:
            part_two +=  f"{instrument.brand} {instrument.model} ({instrument.strength * 100} / 100 strength), "
        answer = part_one + part_two
        return answer[:-2]
    #2.3
    def pick_instrument(self, instrument_index = None):
        import random
        rand = 0
        if not self.instruments:
            return None
        elif instrument_index is None:
            rand = random.randint(0, len(self.instruments) -1)
            return self.instruments[rand]
        elif instrument_index > len(self.instruments) - 1:
            return self.instruments[-1]
        else:
            return self.instruments[instrument_index]
 
#3
def get_name_of_battle_winner(musician_one, musician_two):
    import random
    if not musician_one.instruments and not musician_two.instruments:
        return f"NO CONTEST"
    elif not musician_one.instruments and musician_two.instruments:
        return musician_two.stage_name
    elif musician_one.instruments and not musician_two.instruments:
        return musician_one.stage_name
    
    instrument_one = musician_one.pick_instrument()
    instrument_two = musician_two.pick_instrument()
    print("Robert's", instrument_one)
    print("Miki's", instrument_two)
    
    if instrument_one.strength > instrument_two.strength:
        break_test = instrument_one.does_break()
        if break_test == True:
            print("Robert's Broke")
            return musician_two.stage_name
        else:
            print("Robert's Didn't Break")
            return musician_one.stage_name
    elif instrument_one.strength < instrument_two.strength:
        break_test = instrument_two.does_break()
        if break_test == True:
            print("Miki's Broke")
            return musician_one.stage_name
        else:
            print("Miki's Didn't Break")
            return musician_two.stage_name
        
    elif instrument_one.strength == instrument_two.strength:
        rand = random.randint(1,2)
        print("Equal Strength")
        if rand == 1:
            return musician_one.stage_name
        elif rand == 2:
            return musician_two.stage_name
        
        

   
def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    gear = [danelectro, fender_vi, four_double_o_one]
    # Let's say both musicians have access to the same gear
    sad_musician = Musician("Robert Smith", gear)
    less_sad_musician = Musician("Miki Berenyi", gear)
    # Testing the get_name_of_battle_winner method a few times
    number_of_duels = 10
    for duel_number in range(number_of_duels):
        winner_name = get_name_of_battle_winner(sad_musician, less_sad_musician)
        print(f"THE WINNER OF DUEL #{duel_number + 1} IS {winner_name}!", end="\n\n")
    
main()
        
    

        
        
        