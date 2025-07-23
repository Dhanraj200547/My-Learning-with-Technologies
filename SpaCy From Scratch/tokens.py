import spacy

#create a blank English model
nlp = spacy.blank("en")

doc = nlp("hello world! This is a test sentence.")

# for token in doc:
#     print(token.text)

#Spanning-----------------------------------------------------------------------------------------------------------

# span = doc[1:4]
# print(span.text)

#Lexical Attributes-----------------------------------------------------------------------------------------------------------

# print([i for i in range(len(doc))])
# print([token.text for token in doc])

# print("is alpha:",[token.is_alpha for token in doc])
# print("is num:",[token.like_num for token in doc])
# print("is punc:",[token.is_punct for token in doc])

#Trained Pipelines Working -------------------------------------------------------------------------------------------

#python pipeline package download - $ python -m spacy download en_core_web_sm
#Loading a trained pipeline

# nlp = spacy.load("en_core_web_sm")

# doc = nlp("Test Sentence for spacy pipeline. named entities are London and Paris.")
# # for token in doc:
# #     print(token.text,token.pos_ , token.dep_)
    
# #predicting named entities

# for ent in doc.ents:
#     print(ent.text, ent.label_)
    
    
#Rule based Matching-----------------------------------------------------------------------------------------------------------

# from spacy.matcher import Matcher

# # Load the English NLP model
# nlp = spacy.load("en_core_web_sm")

# # Create a matcher object
# matcher = Matcher(nlp.vocab)

# #Add a pattern to match like iphone X
# pattern = [{"TEXT":"Iphone"},{"TEXT":"X"}]
# matcher.add("IPHONE_X_PATTERN",[pattern])

# #process the text
# doc = nlp("Iphone X type is my favourite phone")

# #call matcher on the doc
# matches = matcher(doc)
# #iterate over the matches
# for match_id,start,end in matches:
#     matched_span = doc[start:end]
#     print(matched_span.text, start, end, match_id)
    
    
