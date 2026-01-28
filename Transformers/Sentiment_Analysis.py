from transformers import pipeline

# model = pipeline("sentiment-analysis")
model = pipeline("text-generation")

# text = "The movie is not so good"

text = "Baa baa black sheep "
result = model(text,max_length = 50)

print(result[0])