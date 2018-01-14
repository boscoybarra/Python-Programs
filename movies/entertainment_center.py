import fresh_tomatoes
import media

# Note: It is good practice to use your class or call it from another file instead of doing so from media.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                    "A marine on an alien planet.",
                    "https://vignette.wikia.nocookie.net/jamescameronsavatar/images/e/e3/French-avatar-poster.jpg/revision/latest/scale-to-width-down/361?cb=20100414212452",
                    "https://youtu.be/5PSNL1qE6VY")



star_wars_viii = media.Movie("Star Wars: The Last Jedi",
                            "Luke Skywalker's peaceful and solitary existence gets upended when he encounters Rey, a young woman who shows strong signs of the Force. Her desire to learn the ways of the Jedi forces Luke to make a decision that changes their lives forever. Meanwhile, Kylo Ren and General Hux lead the First Order in an all-out assault against Leia and the Resistance for supremacy of the galaxy.",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcRgcIU4MKHZkZNeDt_tAewyfwX7PAmSdj_7wdg_FInkZw8Um9F_",
                            "https://www.youtube.com/watch?v=CS0WQ9LuCaw")


movies = [toy_story, avatar, star_wars_viii]

fresh_tomatoes.open_movies_page(movies)
