person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

person["email"] = "alice@example.com"  # Add new key-value pair
person["age"] = 26                     # Update existing value
del person["city"]  # Removes the key 'city'

print(person["name"])
print(person.get("age"))
print(person.get("networth", "Infinite"))


months = {
    'Jan': 'January',
    'feb' : 'February',
    'Mar' : 'March',
    'Apr' : 'April',
    'May' : 'May',
    'Jun' : 'June'
}

print(months["Jan"])
print(months.get("Jan"))
print(months.get("Jul", "Invalid"))
month=months.get("Apr")
print(month)


numbers= {
    1:"One",
    2:"2",
    3:"Three",
    4:"Four",
    5:5,
    "Six":6
    
}
print(numbers[1])
print(numbers["Six"])
