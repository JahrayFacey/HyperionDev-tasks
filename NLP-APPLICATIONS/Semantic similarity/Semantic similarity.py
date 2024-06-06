import spacy

nlp=spacy.load('en_core_web_md')
word1=nlp("cat")
word2=nlp("monkey")
word3=nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# Cat and monkey had the highest similarity score because they are both animals
# Bananna and monkey have the second highest due to bannanas being heavily associated with monkeys
# Cats are animals and bananas are fruits so their similarity is really low
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# For loop for outputting the similarity between all possible combinations of words.
sentnece_to_compare = "Why is my dog on the car"
sentences = ["Where did my dog go?", "Hello, there is my car","I will name my Diana"]
model_sentence = nlp(sentnece_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f"{sentence} - {similarity}")
# For loop for comparing a model sentence to a list of sentences.

word4 = nlp("Science")
word5 = nlp("Book")
word6 = nlp("Car")
print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

# After using a small model for the example file, I noticed that not all comparisions were outputted
# as it doesn't contain vectors so it uses parser, tagger and NER to compare.
# Another observation is that the scores presented are noticably smaller.