# This is my program for natural learning processing using SpaCy.
import spacy
# I load the small english model and create a list with 5 garden path sentences.
nlp = spacy.load('en_core_web_sm')
sample_1 = u"The complex houses married and single soldiers and their families."
sample_2 = u"The horse raced past the barn fell."

gardenpathSentences = [sample_1, sample_2]
gardenpathSentences.append(u"Mary gave the child a Band-Aid.")
gardenpathSentences.append(u"That Jill is never here hurts.")
gardenpathSentences.append(u"The cotton clothing is made of grows in Mississippi.")

# This is a function to tokenize one of the sentences in my gardenpathSentences list.
# Not only does it tokenize every word and punctuation but also used the spacy.explain method. 
# To give a brief description on each token.

def tokenize(sample):
    doc = nlp(sample)
    print([(w.text,w.pos_)for w in doc])
    for token in doc:
     print(token, " | ", spacy.explain(token.pos_), " | ", token.lemma_)
# This is a function to perform named entity recognition. It iterates through one of the sentences to
# It iterates through a sentence and adds the token and its respective label and adds it to an empty label.

def named_Entity_Recognition(sample):
   doc = nlp(sample)
   entities = {}
   for ent in doc.ents:
      entities[ent.text] = ent.label_

   return entities

tokenize(gardenpathSentences[3])
entities = named_Entity_Recognition(gardenpathSentences[3])
print(entities)

#The first entity that I looked up was "Mississippi", A state in USA. The type returned was GPE which describes geopolitical entities like countries and cities.
# In this regard, Mississppi makes sense to be lablelled GPE.
#The second entitiy was 'Jill'. NER highlights the type as PERSON.
#In this sentence Jill is the name of someone so the type PERSON is accurate. 
