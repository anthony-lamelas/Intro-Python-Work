

def get_cast(pairings, movie):
    answer = []
    for key, value in pairings:
        if movie == value:
            answer.append(key)
    return answer

def convert(pairings):
    answer = {}
    
    for x,y in pairings:
        if x not in answer:
            answer.update({x:y})
        else:
            answer[x] += f", {y}"
    return answer

def get_average(convert):
    





pairings = [
 ("Cate Blanchett", "Babel"),
 ("Johnny Depp", "Edward Scissorhands"),
 ("Jack Nicholson", "One Flew Over the Cuckoo's Nest"),
 ("Angela Bassett", "Waiting to Exhale"),
 ("Jack Nicholson", "Batman"),
 ("Jack Nicholson", "The Departed"),
 ("Cate Blanchett", "The Lord of the Rings: The Two Towers"),
 ("Angela Bassett", "Black Panther"),
 ("Brad Pitt", "Fight Club"),
 ("Jodie Foster", "The Silence of the Lambs"),
 ("Edward Norton", "American History X"),
]

print(convert(pairings))