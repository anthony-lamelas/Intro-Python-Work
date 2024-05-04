class Post:
    def __init__(self, username, content, timestamp):
        self.username = username
        self.content = content
        self.timestamp = timestamp
        
    def __str__(self):
        return f"Username: {self.username} \nContent: {self.content} \nTimestamp: {self.timestamp}\n"
    
    
class User:
    def __init__(self, username, posts = []):
        self.username = username
        self.posts = posts
    
    def add_post(self, post):
        self.posts.append(post)
    
    def display_post_history(self):
        print(f"User {self.username}'s Post History:")
        for post in self.posts:
            print(post)
        
        
        
        
        
def main():
    # Create instances of User representing different social media users
    user1 = User("Alice")
    user2 = User("Bob")
    # Create instances of Post representing different social media posts
    post1 = Post("Alice", "Feeling excited about the weekend!", "2023-01-01 10:00:00")
    post2 = Post("Bob", "Just finished reading a great book.", "2023-01-02 15:30:00")
    post3 = Post("Alice", "Cooked a delicious meal today.", "2023-01-03 18:45:00")
    # Add posts to users
    user1.add_post(post1)
    user2.add_post(post2)
    user1.add_post(post3)
    # Display post history for each user
    user1.display_post_history()
    user2.display_post_history()
    

main()




would u ra
