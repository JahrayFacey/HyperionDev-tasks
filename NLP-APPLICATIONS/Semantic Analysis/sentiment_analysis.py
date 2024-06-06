# This is my capastone project that takes a review and performs sentiment analysis on it. 
# To ensure the best accuracy possible, I created two functions: One for precprocessing strings and one for performing the sentiment analysis.
# I also made use of the assessment and polarity attributes for more detailed outputs.
# After loading the model and add the text blob pipe to use the sentiment method, I get the spreadsheet which will be used for analysis.
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob')
amazon = pd.read_csv('amazon_product_reviews.csv', dtype={1:str,10:str})



# Removes all empty rows from the reviews.text column.
amazon.dropna(subset=['reviews.text'], inplace=True)

doc = nlp('reviews.text')
# Converts document to string and removes any whitespace and makes all letters lowercase.
# Tokenizes the converted string whilst removing all stop words and punctuation.
# Joins the tokens to a single string and saves it as a NLP doc with the variable reviews_data.

def preprocessing(text):
    """
    
    Takes a document and performs string conversion, with whitespace removed and all characters converted to lowercase.
    Then perfoms list comprehension to tokenize the string whilst removing all stop words and punctuation.
    It finally joins the tokens together to form a sentence, convert it to a document and return it.
    
    Args:
    text (doc)

    Returns:
    reviews_data (doc)
    """

    text = str(text).lower().strip()
    reviews_data = nlp(text)
    filtered_tokens = [token.text for token in reviews_data if not token.is_stop and not token.is_punct]
    review = ' '.join([token for token in filtered_tokens])
    reviews_data = nlp(review)
    
    return reviews_data

# Finally the program returns to the user the sentiment, polarity and sentiment.
# The sentiment and assessment attributes are converted into strings tp better format output.

def review_analysis(doc):


    
    ' ' ' Creates the polarity, sentiment and assement variables and outputs the result in a f-string. ' ' '
    
    polarity = doc._.blob.polarity
    sentiment = str(doc._.blob.sentiment)
    assessment = str(doc._.blob.sentiment_assessments.assessments)
    print(f"Polarity score is {polarity}, sentiment score is {sentiment} and assessment score is{assessment}")
    
    return polarity, sentiment, assessment


#print(amazon['reviews.text'].sample())
my_review_of_choice = preprocessing(amazon['reviews.text'][20])
review_analysis(my_review_of_choice)


