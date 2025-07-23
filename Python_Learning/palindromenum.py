nums= []
n = int(input())
while (n > 0):
    rem = n % 10
    nums.append(rem)
    n = n // 10
    
print(nums)

#palindrome check
start = 0
end = len(nums) - 1
palindrome = True
while(start < end):
    if nums[start] == nums[end]:
        start += 1
        end -= 1
    else:
        palindrome = False
        break
if palindrome == True:
    print("It is a Palindrome number")
else:
    print( "It is not a Palindrome number")