import spacy

#create a blank English model
nlp = spacy.blank("en")

doc = nlp("hello world! This is a test sentence.")

for token in doc:
    print(token.text, token.pos_, token.dep_)