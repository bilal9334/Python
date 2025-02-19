class Movie:
    """Movie Ratings if they are family-friendly"""

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if 0 < value < 10:
            self._rating = value
        else:
            print("Rating should be between 0 and 10")

    @property
    def is_family_friendly(self):
        if self._rating <= 5:
            return True
        else:
            return False


if __name__ == '__main__':
    movie = Movie("Inception", 9)
    print(movie.rating)
    print(movie.is_family_friendly)

    movie.rating = 4
    print(movie.is_family_friendly)

    movie.rating = 11
