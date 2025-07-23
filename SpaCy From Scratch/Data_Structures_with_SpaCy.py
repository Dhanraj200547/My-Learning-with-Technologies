#Data Structures with spaCy ----------------------------------------------------------------------------------------------------------------
# import spacy

# nlp = spacy.blank("en")
# #shared Vocab and string store

# nlp.vocab.strings.add("Iphone")
# coffee_hash = nlp.vocab.strings.add("Coffee")
# print(nlp.vocab.strings[coffee_hash])  # Output: Coffee

# doc = nlp("I love Coffee")
# # print("Hash_value:",nlp.vocab.strings["Coffee"])

# #Lexemes in the Vocab-----------------------------------------------------------------------------------------------------------

# Lexeme = nlp.vocab["Coffee"]
# print("Lexeme text:", Lexeme.text)
# print("Lexeme hash:", Lexeme.orth)
# print("Lexeme is alpha:", Lexeme.is_alpha)

#Doc , span and Token-----------------------------------------------------------------------------------------------------------

import spacy
# from spacy.tokens import Doc, Span, Token

# # Create a Doc object
# nlp = spacy.blank("en")
# doc = Doc(nlp.vocab, words=["Hello", "world", "!"])

# # Create a Span object
# span = Span(doc, 0, 2)  # Span from token 0 to token 2 (exclusive)
# print("Span text:", span.text) 

#Word vectors and semantic similarity-----------------------------------------------------------------------------------------------------------

#load a pipeline

nlp = spacy.load("en_core_web_md")

#compare two docs
doc1 = nlp("I like Iphone")
doc2 = nlp("I like Apple phone")

print(doc1.similarity(doc2))

#compare two tokens
# token1 = doc1[2]  # "Iphone"
# token2 = doc2[2]  # "Apple"
# print(token1.similarity(token2))  # Compare the two tokens' vectors

# #compare doc with a token
# doc = nlp("I like Apple")
# token = doc[2]  # "Apple"
# print(doc.similarity(token))  # Compare the doc's vector with the token's vector

# #compare span with doc

# span = doc1[1:3]  # Span from token 1 to token 3 (exclusive)
# print(span.similarity(doc2))  # Compare the span's vector with the doc's vector

# #combining predictions and rules------------------------------------------------------------------------------------------------------------


