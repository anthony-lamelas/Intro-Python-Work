class VideoGameStore:
    def __init__(self, owner, games):
        self.owner = owner
        self.games = games
        
        
        
    def __str__(self):
        games_list = '\n'.join([f'\t{title} by {author}' for title, author in self.games])
        return f"Welcome to {self.owner}'s Video Game Store!\nWe have the following titles available for you:\n{games_list}"
    
    def buy_game(self,game):
        if game in self.games:
            for i in range(len(self.games)-1):
                if game == self.games[i]:
                    self.games.remove(game)
                    print("Thank you for your purchase of", game[0])
            return True
        else:
            print("Sorry, we do not have", game[0])
            return False
        
    
    def view_games(self):
        print("Available titles:")
        for game in self.games:
            print(f"\t{game[0]}")    
    
        
        
def main():
    bobs_store = VideoGameStore("Bob", [("Overwatch","Blizzard"), ("Super Meat Boy", "Team Meat"), ("Deltarune","Toby Fox")])
    print(bobs_store)
    bobs_store.buy_game(("League of Legends", "Riot Games"))
    bobs_store.buy_game(("Overwatch", "Blizzard"))
    bobs_store.view_games()
    
    
main()
        