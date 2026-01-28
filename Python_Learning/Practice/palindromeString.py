word = input()

reversed_word = word[::-1]

if word == reversed_word:
    print(word +" is a Palindrome")
else:
    print(word +" is not a Palindrome")

#while loop
i = 0
j = len(word) -1 
ispalindrome = True
while(i < j):
    if word[i] != word[j]:
        ispalindrome = False
        break
    i += 1
    j -= 1
print("It is palindrome" if ispalindrome else "It is not palindrome")