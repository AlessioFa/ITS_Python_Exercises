class Movie:
    def __init__(self, movie_id: str, title: str, director: str) -> None:
        self._movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False

    def rent(self) -> None:
        
        if self.is_rented:
            print("Error: The movie has been rented.")
        
        else:
            self.is_rented = True

    def return_movie(self) -> None:
        
        if not self.is_rented:
            print("Error: The movie has not been rented to anyone.")
        
        else:
            self.is_rented = False


class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.rented_movies: list[Movie] = []

    def rent_movie(self, movie: Movie) -> None:
        
        if movie.is_rented:
            print("Error: The movie has been rented already.")
        
        else:
            movie.rent()
            self.rented_movies.append(movie)

    def return_movie(self, movie: Movie) -> None:
        
        if movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
        
        else:
            print("Error: The client didn't rent this movie.")


class VideoRentalStore:
    def __init__(self, movies: dict[str, Movie] = {}, customers: dict[str, Customer] = {}):
        self.movies = movies
        self.customers = customers

    def add_movie(self, movie_id: str, title: str, director: str) -> None:
        
        if movie_id not in self.movies:
            movie = Movie(movie_id, title, director)
            self.movies[movie_id] = movie
        
        else:
            print("Error: The movie is already in the catalog!")

    def register_customer(self, customer_id: str, name: str) -> None:
        
        if customer_id not in self.customers:
            customer = Customer(customer_id, name)
            self.customers[customer_id] = customer
        
        else:
            print("Error: The client is already in the database!")

    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        
        if movie_id in self.movies and customer_id in self.customers:
            movie = self.movies[movie_id]
            self.customers[customer_id].rent_movie(movie)
        
        else:
            print("Error: Client or movie not found.")

    def return_movie(self, customer_id: str, movie_id: str) -> None:
        
        if movie_id in self.movies and customer_id in self.customers:
            
            movie = self.movies[movie_id]
            self.customers[customer_id].return_movie(movie)
        
        else:
            print("Error: Client or movie not found!")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        
        else:
            print("Error: The client doesn't exist.")
            return []

    def get_all_movies(self) -> list[Movie]:
        rented_movies: list[Movie] = []

        for customer in self.customers.values():
            rented_movies += customer.rented_movies
    
        return rented_movies