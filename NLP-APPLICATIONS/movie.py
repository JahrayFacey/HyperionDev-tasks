# This my program that takes the description of a movie and will display the reccommended movie to watch next.
import spacy
import pandas as pd
nlp = spacy.load("en_core_web_md")
movie_descriptions = pd.read_csv('movies.txt')
# These are a collection of movie descriptions that will be compared to the function's parameter. I put all movies in a list so it can be iterated.
movie_a = "Movie A: When Hiccup discovers Toothless isn't the only Night Fury, he must seek 'The Hidden World', a secret Dragon Utopia before a hired tyrant named Grimmel finds it first."
movie_b = "Movie B: After the death of Superman, several new people present themselves as possible successors."
movie_c = "Movie C:A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up."
movie_d = "Movie D: A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson."
movie_e = "Movie E: A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed."
movie_f = "Movie F: In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from."
movie_g = "Movie G: The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes."
movie_h = "Movie H: A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral."
movie_i = "Movie I: Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow."
movie_j = "movie J:Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."
descriptions = [movie_a,movie_b,movie_c,movie_d,movie_e,movie_f,movie_g,movie_h,movie_i,movie_j]
# This is the function I created. It takes the description of a movie, converts it to a doc and compares it to every item on the list.
# The two variables 'score' and 'number' are to track the highest similarity score and the position of the descriptions list index respectively.
# Once the list has been iterated and the highest score has been saved it will return and output the name and description of the movie.

def suggestion(sentence):
    score = 0
    model_description = nlp(sentence)
    for model in movie_descriptions:
     similarity = nlp(model).similarity(model_description)
     if similarity > score:
        score = similarity
        best_match = model
     number= number + 1
    return best_match
suggested_movie = suggestion("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him in to space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator")
print(f"Based on what you just watched, we think {suggested_movie} is up your ally.")