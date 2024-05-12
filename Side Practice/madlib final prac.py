class MadLib:
    def __init__(self, filepath):
        try:
            with open(self.filepath, 'r') as file:
                self.contents = file.readlines()
        except FileNotFoundError:
            self.contents = []
            print("File not found.")
            
            
    def populate_madlib(self, word_bank):
        for i in range(len(self.contents)):
            if "[N]" in self.contents[i]:
                self.contents[i] = self.contents[i].replace("[N]", get_noun(word_bank))
            elif "[V]" in self.contents[i]:
                self.contents[i] = self.contents[i].replace("[V]", get_verb(word_bank))
            elif "[AV]" in self.contents[i]:
                self.contents[i] = self.contents[i].replace("[AV]", get_advb(word_bank))
            elif "[AJ]" in self.contents[i]:
                self.contents[i] = self.contents[i].replace("[AJ]", get_adjv(word_bank))
                
    def __str__(self):
        return ''.join(self.contents)
    
def main():
    word_bank = WordBank()
    madlib = MadLib('madlib.txt')
    madlib.populate_madlib(word_bank)
    print(madlib)

main()