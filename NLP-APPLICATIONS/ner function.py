import spacy

def named_entity_recognition(sentence):
    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load("en_core_web_sm")
    
    # Process the input sentence using SpaCy
    doc = nlp(sentence)
    
    # Iterate through each named entity in the processed document
    entities = {}
    for ent in doc.ents:
        entities[ent.text] = ent.label_
    
    return entities

# Example usage:
sentence = "Apple is looking at buying U.K. startup for $1 billion"
entities = named_entity_recognition(sentence)
print(entities)