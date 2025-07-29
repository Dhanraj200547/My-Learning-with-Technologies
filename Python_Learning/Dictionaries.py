#simple dictionary
person_1 = {"color" : "green" , 'points' : 5}
print(person_1['color'])
print(person_1['points'])

person_2 = {}
person_2['name'] = 'dhanraj'
person_2['age'] = 20
print(person_2)

#looping through the dictionaries
for key,value in person_2.items():
    print("Key = " + key + " value = " + str(value))