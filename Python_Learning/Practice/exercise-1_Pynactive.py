# num1 = int(input())
# num2 = int(input())

# if num1*num2 < 1000:
#     print(num1 * num2)
# else:
#     print(num1 + num2)
    
#-------------------------------------------------------------

# for i in range(0,11):
#     if i == 0:
#         print("sum :" , i)
#     else:
#         print("sum :" , i+i-1 )
        
#-------------------------------------------------------------

# str = "Hello World"

# for i in range(len(str)):
#     if i % 2 == 0:
#         print(str[i] + " ", end="")
        
#-------------------------------------------------------------

#remove characters from a string

# def remove_chars(word, n):
#     if n < 0 or n >= len(word):
#         return word
#     return word[n:]

# print(remove_chars("Hello World", 4))  # Output: "o World"

#-------------------------------------------------------------

#Check first and last numbers ina lis tare same or not

# def check_same(nums):
#     return nums[0] == nums[-1]

# nums = [10, 20, 30, 40, 10]
# print(check_same(nums))

#-------------------------------------------------------------

#numbers divisible by 5
# li = []
# def check_divisbility(nums):
#     for i in nums:
#         if i % 5 == 0:
#             li.append(i)

# nums = [10,11,12,15,25,58]
# check_divisbility(nums)
# print(li)

#-------------------------------------------------------------------
#no.of occurence
# s = list(map(str,input().split()))
# count = 0
# for i in s:
#     if i == "because":
#         count += 1
# print(count)

#-------------------------------------------------------------------------

#merge two list 
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# new_list = list1 + list2
# print(new_list)

#-----------------------------------------------------------------------
#get each digit in reverse order
# num = 6789
# result = []
# while (num != 0):
#     digit = (num % 10)
#     result.append(digit)
#     num = num // 10
# print(result)
    
#---------------------------------------------------------------------------
#income tax calculation

# salary = 45000
# if salary <= 10000:
#     print("No tax")
# elif salary > 10000 and salary < 25000:
#     taxation_amt = salary - 10000
#     print("Tax for salary = " , taxation_amt/100 * 10)
# else:
#     taxation_amout = salary - 20000
#     print("Tax for salary = ", (taxation_amout/100*20)+1000)

#-------------------------------------------------------------------------------
#simpkle count down
# import time
# seconds = int(input())
# while(seconds != 0):
#     print("seconds remaning",seconds)
#     time.sleep(1)
#     seconds -= 1
# print("Time is up!!!")

#---------------------------------------------------------------------------------

