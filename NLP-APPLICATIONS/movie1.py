# This my program that takes the description of a movie and will display the reccommended movie to watch next.
# 
import spacy
import pandas as pd
nlp = spacy.load("en_core_web_md")
file = open('movies.txt', 'r')
# An empty list is created and a for loop iterates through the text file to append inside.
descriptions = []
for line in file:
   descriptions.append(line)
# An empty dictionary and another for loop iterates through the descriptions list to seperate the title of a movie from the description and set them as the key and value respectively.
desc_dictionary = {}
for item in descriptions:
   movies = item.split(" :")
   desc_dictionary[movies[1]] = movies[0]
# The compare function iterates through the provided dictionary until it matches the description for a movie also provided otherwise an error message is printed.
# The loop variable is saved as the key for the dictionary and 
def compare(desc, dictionary):
   output = ""
   for key in dictionary:
    if key == desc:
       output = (dictionary[key])
       break
    else:
       output = print("key not found")
    print(output)
# These are a collection of movie descriptions that will be compared to the function's parameter. I put all movies in a list so it can be iterated.

# This is the function I created. It takes the description of a movie, converts it to a doc and compares it to every item on the list.
# The two variables 'score' and 'number' are to track the highest similarity score and the position of the descriptions list index respectively.
# Once the list has been iterated and the highest score has been saved it will return and output the name and description of the movie.

def suggestion(sentence):
    score = 0
    model_description = nlp(sentence)
    for model in descriptions:
     similarity = nlp(model).similarity(model_description)
     if similarity > score:
        score = similarity
        best_match = model
     #number= number + 1
    return best_match
compare("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him in to space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator",desc_dictionary)
suggested_movie = suggestion("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him in to space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator")
print(f"Based on what you just watched, we think {suggested_movie} is up your ally.")