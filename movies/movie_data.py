import media

# set movies info
# create movie instances
sherlock_info = ["Sherlock",
                 "90",
                 "A modernised series of adaptations of the Sherlock Holmes "
                 "novels by Sir Arthur Conan Doyle. ",
                 "https://vignette.wikia.nocookie.net/bakerstreet/images/9/9d/BBC_Sherlock_Poster.jpg/revision/latest?cb=20130416134410",  # NOQA
                 "https://www.youtube.com/watch?v=qlcWFoNqZHc"]

crouching_tiger_info = ["Crouching Tiger, Hidden Dragon",
                        "120",
                        "A young Chinese warrior steals a sword from a famed "
                        "swordsman and then escapes into a world of romantic "
                        "adventure with a mysterious man in the frontier of "
                        "the nation.",
                        "https://upload.wikimedia.org/wikipedia/en/9/97/Crouching_tiger_hidden_dragon_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=gLpZ_5bHmo8"]

big_bang_theory_info = ["The Big Bang Theory",
                        "21",
                        "A woman who moves into an apartment across the hall "
                        "from two brilliant but socially awkward physicists "
                        "shows them how little they know about life outside "
                        "of the laboratory.",
                        "https://vignette.wikia.nocookie.net/bigbangtheory/images/f/f3/Big_bang_theory_poster.jpg/revision/latest?cb=20090218074507",  # NOQA
                        "https://www.youtube.com/watch?v=WBb3fojgW0Q"]

thor_info = ["Thor: Ragnarok",
             "130",
             "Two years after the battle of Sokovia, Thor is imprisoned by "
             "the fire demon Surtur in Muspelheim.",
             "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",  # NOQA
             "https://www.youtube.com/watch?v=v7MGUNV8MxU"]

panda_info = ["Kung Fu Panda",
              "92",
              "Po might just be the laziest, clumsiest panda in the Valley "
              "of Peace, but he secretly dreams of becoming a kung fu legend.",
              "https://www.fulcrumgallery.com/product-images/AZAA8ADA-P603955.jpg",  # NOQA
              "https://www.youtube.com/watch?v=PXi3Mv6KMzY"]

youth_info = ["Fang hua",
              "136",
              "A look at the lives of members of a Military Cultural Troupe "
              "in the 1970s.",
              "https://m.media-amazon.com/images/M/MV5BMGIwM2NiZGEtYTNkZi00NjAzLThjMTAtODUzY2MyNjE4OTdlXkEyXkFqcGdeQXVyNTMyNTA3Mzc@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
              "https://www.youtube.com/watch?v=qq8fCA8vXZc"]


def get_movies():
    """get movies info

       Args:
       None.

       Returns:
       movies(Movie[]).
    """
    sherlock = media.Movie(sherlock_info[0],
                           sherlock_info[1],
                           sherlock_info[2],
                           sherlock_info[3],
                           sherlock_info[4])
    crouching_tiger = media.Movie(crouching_tiger_info[0],
                                  crouching_tiger_info[1],
                                  crouching_tiger_info[2],
                                  crouching_tiger_info[3],
                                  crouching_tiger_info[4])
    big_bang_theory = media.Movie(big_bang_theory_info[0],
                                  big_bang_theory_info[1],
                                  big_bang_theory_info[2],
                                  big_bang_theory_info[3],
                                  big_bang_theory_info[4])
    thor = media.Movie(thor_info[0],
                       thor_info[1],
                       thor_info[2],
                       thor_info[3],
                       thor_info[4])
    panda = media.Movie(panda_info[0],
                        panda_info[1],
                        panda_info[2],
                        panda_info[3],
                        panda_info[4])
    youth = media.Movie(youth_info[0],
                        youth_info[1],
                        youth_info[2],
                        youth_info[3],
                        youth_info[4])
    movies = [sherlock, crouching_tiger, big_bang_theory, thor, panda, youth]
    return movies
