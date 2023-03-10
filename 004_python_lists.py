# A list is an ordered collection of items

bassguitars = ['Yamaha','Fender','Sire','Ibanez']

# region changingcase
# Print out List
print(f"This is a list of bass guitar manufacturers {bassguitars}\n")

# Print out first bass guitar in list
print(f"The first bass guitar manufacturer in the list is {bassguitars[0]}\n")

# Upper Case
print(f"The first bass guitar in UPPER CASE is {bassguitars[0].upper()}\n")

# endregion changingcase

# region selectinganitembasedonindex
# Last item - Fender
print(f"The last bass guitar manufacturer in the list is {bassguitars[-1]}\n")

# Third last item - Fender
print(f"The third from last bass guitar manufacturer in the list is {bassguitars[-3]}\n")

# Note if there are fewer items in list than what you are asking for then index error. 
# E.g. [-1] of an empty list or [-3] of a list with 2 items will generate an error.

# endregion selectinganitembasedonindex

# region updatinganitembasedonindex
# Rename (update) an item in a list (Fender --> Squire) 
bassguitars[1] = "Squire"
print(f"Swapped out Fender for {bassguitars[1]}")
print(f"List of bass guitar manufacturers is now {bassguitars}\n")
# endregion updatinganitembasedonindex

# region addelementstolist
# Add elements to the end of a list - ** can only append one item at a time **
bassguitars.append('Fender')
print(f"Added {bassguitars[-1]}")
print(f"The list is now {bassguitars}\n")

# Insert elements into the list in any position you want e.g. 4th in the list as zero based index
bassguitars.insert(3,'Cort')
print(f"The list is now {bassguitars}\n")

# endregion addelementstolist

# region removeelementsfromlist
# Remove an item from a list based on index
print(f"The bass guitar manufacturer we are about to delete is {bassguitars[1]}")
del bassguitars[1]
print(f"The current list of bass guitar manufacturers is now {bassguitars}\n")

# Remove an item from a list based on value
# Only deletes first value - need to loop to capture all values
print(f"The bass guitar manufacturer we are about to delete is Ibanez")
bassguitars.remove('Ibanez')
print(f"The current list of bass guitar manufacturers is now {bassguitars}\n")

# endregion removeelementsfromlist

# region popitems

# Remove last item on list but still be able to reference it using pop[]
popped_bassguitars = bassguitars.pop()
print(f"The current list of bass guitar manufacturers is {bassguitars}")
print (f"The bass guitar manufacture last deleted (popped off the list) is {popped_bassguitars}\n")

# Pop items from anywhere on a list - e.g. second from list
popped_bassguitars = bassguitars.pop(1)
print(f"The current list of bass guitar manufacturers is {bassguitars}")
print (f"The bass guitar manufacture last deleted (popped off the list) is {popped_bassguitars}\n")

# endregion popitems


#region sortinglists
# Be aware that case sensitivity might make this more complex than simple examples below
#Permanently with sort() method

print(f"\nThe current list of bass guitar manufacturers is {bassguitars}")
bassguitars.sort()
print(f"\nThe list of bass guitar manufacturers sorted alphabetically is {bassguitars}")
bassguitars.sort(reverse=True)
print(f"\nThe list of bass guitar manufacturers sorted reverse alphabetically is {bassguitars}")
bassguitars.sort()
# Temporarily with sorted() method
print(f"\nThe list of bass guitars in alphabetical order is {sorted(bassguitars)}")

# reverse order of list (not alphabetically - just the order)
bassguitars.append ('Fender')
bassguitars.append ('Squire')
bassguitars.append ('Sire')
print(f"\nThe list is now {bassguitars}")

# .reverse() uses in place modification. You cannot print it directly. You need to modify the list first. 
bassguitars.reverse()
print(f"\nThe list in reverse is {bassguitars}")

# Number of items in a list
numbasses = len(bassguitars)
print(f"\nI now have {numbasses} bass guitars")


#endregion sortinglists

