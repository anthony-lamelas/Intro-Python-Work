def get_cast(pairings, movie):
    answer = []
    for key, value in pairings:
        if movie == value:
            answer.append(key)
    return answer


def convert(pairings):
    answer = {}
    for star, movie in pairings:
        if star in answer:
            answer[star].append(movie)
        else:
            answer[star] = [movie]
    return answer


def get_average(convert):
    total_movies = 0
    total_actors = 0
    for movies_list in convert.values():
        total_movies += len(movies_list)
        total_actors += 1
    return total_movies / total_actors

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

convert = (convert(pairings))
print(convert)
a= get_average(convert)
print(a)
