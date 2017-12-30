import fresh_tomatoes
import media

# creating instances of media.Movie
avengers = media.Movie("The Avengers", "Heroes get together.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                        "https://www.youtube.com/watch?v=eOrNdBpGMv8")

kung_fu_hustle = media.Movie("Kung Fu Hustle", "A hooligan becomes something more.",
                     "https://upload.wikimedia.org/wikipedia/en/0/00/KungFuHustleHKposter.jpg",
                     "https://www.youtube.com/watch?v=-m3IB7N_PRk")

memento = media.Movie("Memento", "A person tries to remember.",
                      "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0")

inception = media.Movie("Inception", "We have to go deeper.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

power_rangers = media.Movie("Power Rangers", "Teenagers with attitudes.",
                            "https://upload.wikimedia.org/wikipedia/en/7/78/Power_Rangers_%282017_Official_Theatrical_Poster%29.png",
                            "https://www.youtube.com/watch?v=5kIe6UZHSXw")

inside_out = media.Movie("Inside Out", "Emotions come to life.",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=seMwpP0yeu4")

# combining all instances into a movies array
movies = [avengers, kung_fu_hustle, memento, inception, power_rangers, inside_out]
