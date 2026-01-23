#word counter
def word_counter(text):
    freq = {}
    for word in text.split():
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    return freq

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# print(word_counter(text))

# try:
#     x = int(input())
#     print(10 / x)
# except Exception as e:
#     print(f"Unable to proceed due to {e}")
# else:
#     print("Successfully Calculated")
# finally:
#     print("Cleaning resources")

#check if a number is prime or not


# def isprime(n):
#     prime = True
#     for i in range(2,n//2):
#         if n%i == 0:
#             prime = False
#     return prime

# print(isprime(x))

#fibonacci series

# def fibonacci(n):
#     if n <= 1:
#         return n 
#     return fibonacci(n-1) + fibonacci(n-2)
    
# for i in range(x + 1):
#     print(fibonacci(i),end = " ")

#Factorial

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

print(factorial(5))