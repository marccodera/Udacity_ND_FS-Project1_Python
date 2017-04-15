import fresh_tomatoes
import media


def create_movies():
    """ Declare every movie instance made from the movie class.

    Instances:
        Each instance includes Movie Title, Story, Poster URL and Trailer URL.
        toy_story (Movie): Movie instance for Toy Story movie
        avatar (Movie): Movie instance for Avatar movie
        ciudad_de_dios (Movie): Movie instance for City Of God movie
        life_of_pi (Movie): Movie instance for Life Of Pi movie
        lord_of_the_rings (Movie): Movie instance for Lorf Of The Rings movie
        star_wars (Movie): Movie instance for Star Wars movie

    Variables:
        movies (array): Array of Movie instances that this function returns.

    Returns:
        An array of movies instances created inside the function.
    """

    # Declare Movie instance for Toy Story using media class
    cinema_paradiso = media.Movie("Cinema Paradiso",
                                  "A story of a boy and his passion for movie",
                                  "http://www.fotogramas.es/var/ezflow_site/storage/images/peliculas/cinema-paradiso/10324-1-esl-ES/Cinema-Paradiso1.jpg",  # NOQA
                                  "https://youtu.be/maV1ZYdAExw")
    # Declare Movie instance for Avatar using media class
    the_godfather = media.Movie("The Godfather",
                                "Story of most powerful mafia clan in NY",
                                "https://s-media-cache-ak0.pinimg.com/736x/40/b4/21/40b421c7cfe1b3059d5e50d79e968270.jpg",  # NOQA
                                "https://youtu.be/5DO-nDW43Ik")
    # Declare Movie instance for City Of God using media class
    city_of_god = media.Movie("City Of God",
                              "Two little kids become big gangsters in Brazil",
                              "http://es.web.img3.acsta.net/medias/nmedia/18/68/09/00/20071863.jpg",  # NOQA
                              "https://youtu.be/NN14_5fyXmk")
    # Declare Movie instance for Life Of Pi using media class
    life_of_pi = media.Movie("Life Of Pi",
                             "Life of a long term lost person in the sea",
                             "https://upload.wikimedia.org/wikipedia/en/4/45/Life_of_Pi_cover.png",  # NOQA
                             "https://youtu.be/j9Hjrs6WQ8M")
    # Declare Movie instance for Lord Of The Rings using media class
    lord_of_the_rings = media.Movie("Lord Of The Rings",
                                    "Life of a lost person in the sea",
                                    "http://fontmeme.com/images/The-Lord-of-the-Rings-Poster.jpg",  # NOQA
                                    "https://youtu.be/Pki6jbSbXIY")
    # Declare Movie instance for Star Wars using media class
    star_wars = media.Movie("Star Wars",
                            "Life of a long term lost person in the sea",
                            "https://s-media-cache-ak0.pinimg.com/236x/fc/12/81/fc12814f7f32b766409faf48df15ddf0.jpg",  # NOQA
                            "https://youtu.be/9gvqpFbRKtQ")

    # Creates movies Array with the instances created before
    movies = [city_of_god, life_of_pi, lord_of_the_rings,
              star_wars, cinema_paradiso, the_godfather]

    return movies  # Returns movies Array declared just before

# Calls fresh_tomatoes class to open the browser and build the movies library
# using create_movies() function to give the movies array to the class
fresh_tomatoes.open_movies_page(create_movies())
