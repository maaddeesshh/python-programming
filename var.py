character_name = "Eugene"
character_age = 99
# character_age = "102"
is_Male = True
print("My name is " + character_name)
print("My name is ", character_name)
print("My age is " + str(character_age) + " years old ") #convert to string so that you can join 
# print("My age is " + character_age + " years old") if stored as a string
character_name = "Madesh"
print("I'm now " + character_name)
print(character_name + " is cool \n") #concatenation
print(character_name.lower())
print(character_name.upper())
print(character_name.islower())
print(character_name.lower().isupper())
print(len(character_name))
print(character_name[0])
print(character_name.index("M"))
print(character_name.index("des")) #gives you the index where the words start 
character_name = "MADESH"
print(character_name.replace("MADESH", "MADEGWA"))
