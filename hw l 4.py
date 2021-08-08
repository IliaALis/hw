movies = [
          {'title':'The Way I See It', 'year':'2020','director':'Dawn Porter','rating':7},
          {'title':'Woman', 'year':'2019','director':'Yann Arthus-Bertrand','rating':3},
          {'title':'Postal', 'year':'2019','director':'Tyler Falbo','rating':6},
          {'title':'The Last Samurai', 'year':'2003','director':'Edward Zwick','rating':9},
          {'title':'Saving Private Ryan', 'year':'1998','director':'Steven Spielberg','rating':10},
          {'title':'10 Minutes Gone', 'year':'2019','director':'Brian A. Miller','rating':5},
          {'title':'Road to Red', 'year':'2020','director':'Tito da Costa','rating':4},
         ]
# print(movies)
while True:

    def get_movies(rating):
        a = False
        if rating.isdigit():
            n = int(rating)
            for movie in movies:
                if n <= movie['rating']:
                    a = True
                    newMovies = []
                    newMovies.append(movie['title'])
                    print(', '.join(newMovies))
                if a == False:

                    print('не в этом списке')
                    break
        else:
            print('no way')

        return 

    print('ввести рейтинг фильма:')
    get_movies(input())

    if input('repeat?(y/n)') == 'n':
          break
