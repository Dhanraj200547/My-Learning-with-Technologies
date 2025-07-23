#Training a neural network model with spaCy

import spacy
from spacy.tokens import Doc, Span, Token ,DocBin

nlp = spacy.blank("en")

doc1 = nlp("Iphone X is a great phone.")
doc1.ents = [Span(doc1,0,2,label="GADGET")]

doc2 = nlp("I need a new phone.")
doc2.ents = []

docs = [doc1, doc2]

#splitting the docs into train and test sets
train_docs = docs[len(docs)//2]
test_docs = docs[len(docs)//2:]

#docbin container
train_docbin = DocBin(docs=train_docs)
train_docbin.to_disk("train.spacy")

test_docbin = DocBin(docs=test_docs)
test_docbin.to_disk("test.spacy")

