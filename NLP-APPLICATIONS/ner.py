import spacy

sample_1 = u"The complex houses married and single soldiers and their families."
sample_2 = u"The horse raced past the barn fell."

gardenpathSentences = [sample_1, sample_2]
gardenpathSentences.append(u"Mary gave the child a Band-Aid.")
gardenpathSentences.append(u"That Jill is never here hurts.")
gardenpathSentences.append(u"The cotton clothing is made of grows in Mississippi.")
nlp = spacy.load("en_core_web_sm")
doc = nlp(gardenpathSentences[4])


for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
doc_1 = nlp(sample_2)
for ent in doc_1.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
def tokenize(sample):
    doc_2 = nlp(sample)
    print([(w.text,w.pos_)for w in doc_2])
    for token in doc_2:
     print(token, " | ", spacy.explain(token.pos_), " | ", token.lemma_)
     