current_movies = {
    'The Grinch' : '11:00 AM',
    'Rudolph' : '1:00 PM',
    'Christmas Vacation' : '5:00 PM'
}

print("We are showing the following movies:")
for key in current_movies:
    print(key)

movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie is not playing.")
else:
    print(movie, 'is playing at', showtime)