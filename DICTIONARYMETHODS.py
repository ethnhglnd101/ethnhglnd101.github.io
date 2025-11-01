"""
Name: Ethan Hoglund
Date: October 31st, 2025
Class: Python Section B
Assignment: Dictionary Methods
"""

# INPUT: None/String/Integer/etc. This is what the method RECEIVES. 
# RETURN: None/dict/int/etc
# Your own UNIQUE example of how to use it AND a sentence or two with a real world scenario where such a method would be useful. 
# For example, "The dictionary holds student information for each class, with student names as the key, and information about that student as the value. The last student who enrolled in the class decided to drop the class. I can use popitem() to remove that last enrollment. "
# Your example does not have to be perfect, but it must demonstrate that you are thinking about HOW each method is used.

"""
This method is called the clear() method and is used to empty out all the components of a list. 
For example if you had a list of people that were invited to a party
and then the party got cancelled, then you could clear the list to show
that there is no longer a need for the list!

There are no parameters and this function outputs None.
"""

dictionary = {
"Streamer":"Kai Cenat",
"Businessman":"Elon Musk",
"Actor":"Tom Cruise",
"Software Engineer":"Andrew Hoglund",
"Spider-man":"Miles Morales"
}

def clear(dict):
    dict.clear()
    
print("\n Clear Method: ")
print(clear(dictionary)) # outputs 'None'

# copy()

"""
The copy() method is a useful way to take a list and copy it to a new value. This would be useful if you wanted to
tell someone to go get the groceries when you had the list and they did not. Therefore, you could use the copy() method to 
copy the list and give it to them.

There are no parameters and this function outputs a copy of the dictionary.
"""

dictionary1 = {
"physics":"albert einstein",
"chemistry":"Ernest Rutherford",
"astrophysics":"Avri Loeb",
"computer science":"Alan Turing"
}

def copy_dict(dict):
    copied = dict.copy() # copies list
    print(copied)
    return copied

print("\n Copy Method: ")
copy_dict(dictionary1)

# fromkeys()

"""
This method is useful for taking a list or other method of storing information and assigning them values in a dictionary format. 
This would be useful for assigning your kids' bank account to 0 when they all buy something at Disney World. 

There are 2 parameters (both lists) and this function outputs a dictionary.
"""

x = ("1 + 1", "2 x 1", "100/50", "√4")
y = 2

def getkeys(x,y):
    new = dict.fromkeys(x,y) # compiles and stores dictionary
    print(new)
    return new
print("\n FremKeys Method: ")
getkeys(x,y)

# get()

"""
This method returns the value for the given key. This would be useful for 
finding the price of an item at a store when you input the name.

There is 1 parameter and this function outputs the value of the given key.
"""


dictionary2 = {
"Jordan 1":"7/10",
"Jordan 4":"6/10",
"Yeezy Boost":"7/10",
"Travis Scott Reverse Mocha Jordan 1":"10/10",
"Brick by Brick Jordan 4":"9/10",
"Yeezy Slides":"6/10"
}

extract = dictionary2.get("Brick by Brick Jordan 4")
print("\n Get Method: ")
print(extract)

# items()

"""
The next method is the items() method. 
This method could be used in the example of having to print out an account
number with each of their balances as pairs.

There are 0 parameters and this function outputs the entire dictionary in a list with tuples for each key.
"""

dictionary3 = {
"apple watch":"6/10",
"iphone 16 pro":"10/10",
"ipad":"8/10",
"android":"7/10",
"garmin watch":"7/10",
}

itemized = dictionary3.items()

print("\n Item Method: ")
print(itemized)

# keys()

"""
This method is called the keys() method and returns the values of the KEYS of a dictionary in a list. This 
could be utilized when wanting to provide the names of people who had entered into a raffle where their names and numbers
are correlated. 

There is 0 parameters and this function outputs a list of keys.
"""

dictionary4 = {
"ferrari":"scuderia corsa",
"porsche":"911",
"mclaren":"speedtail",
"audi":"R8",
"lexus":"IS500"
}

keyed = dictionary4.keys()
print("\n Keys Method: ")
print(keyed)

# pop()

"""
This method is called pop() and is used in order to pop a key and return the given value. This could be used
to remove a person from a list of debt and show the amount of debt that they've paid off.

There are 2 parameters: one is the keyname of the item to be removed and the other is an optional parameter
that returns a value if the parameter does not exist. 
"""

dictionary5 = {
"pistol":"glock",
"assault rifle":"AR-15",
"rifle":"M1 Garand",
"automatic machine gun":"M4 Carbine",
}


popped = dictionary5.pop("pistol")
print("\n Pop Method: ")
print(popped)

# popitem()

"""
This method is called popitem() and is used to remove the last key and value in a tuple. This could be used to cut 
someone out of a list of people because they did not show up on time for the ferry to leave to Manhattan Island from the 
Rockaways.

There are 0 parameters and this returns a key and its value.
"""

dictionary6 = {
"PLA":"Strong but melts quickly",
"ABS":"Tough yet warps on heat plate",
"TPU":"Great for flexible things",
"PETG":"Strong, cheap and shiny"
}

perforated = dictionary6.popitem()
print("\n Pop Item Method: ")
print(perforated)

# setdefault()

"""
This method returns the value for the given key. This could be used if a 
receptionist wanted to index the phone numbers of the clients.

There is 2 parameters: one of them is the keyname of the value you want to return
and the second one is an optional parameter that if the key does not exist, this becomes the key's value. The default
output is None. 
"""

dictionary7 = {
"green gas":"gas is inputted directly into magazine",
"co2":"cartridges are placed inside the magazine or gun",
"spring powered":"bbs are shot with spring power and manually loaded",
"battery powered":"battery runs motor that continuously shoots depending on firing mode"
}

set_to_default = dictionary7.setdefault("co2")
print("\n Set Default Method: ")
print(set_to_default)

# update()

"""
This method is similar to the append() feature with lists as it modifies the existing keys/values. This could be used 
for an account when a girl gets married and changes her last name.

This method has one parameter which is an iterable and outputs None.  
"""

dictionary8 = {
"tiger":"cat",
"wolf":"dog",
"panther":"cat",
"pereguine falcon":"bird"
}

updated = dictionary8.update({"komodo dragon":"lizard"})
print("\n Update Method: ")
print(dictionary8)

# values()

"""
This method is called values() and returns the values of the dictionary in a list. 
This can be used if an organization wants too collect the phone numbers of its members
for a text message.

There are 0 parameters and this outputs a list of the values.
"""

dictionary9 = {
"diamond":"carbon",
"gold":"natural element",
"aluminum":"natural element",
"silver":"natural element",
"graphene":"carbon"
}

keyvalues = dictionary9.values()
print("\n Values Method: ")
print(keyvalues)

### DICTIONARY METHODS ###

my_dict = {
  'Alabama': 'Southeast',
  'California': 'West',
  'Maine': 'New England',
  'Ohio': 'Midwest',
  'Arizona': 'South'
}

# Use the above dictionary to test the following methods
# Return all keys for the dictionary
def get_keys(my_dict):
    allkeys = my_dict
    print(allkeys)
    return allkeys

print("\n--get_keys() function: ")
get_keys(my_dict)

def get_values(my_dict, key):
    new = my_dict.pop(key)
    print(new)
    return new

print("\n--get_values() function: ")
get_values(my_dict, "California")

def update_dict(my_dict, key, new_value):
    my_dict[key] = new_value
    print(my_dict)
    return my_dict

print("\n--update_dict() function: ")
update_dict(my_dict, "Arizona", "Southwest")