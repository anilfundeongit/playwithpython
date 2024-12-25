fruits = ["Cherry", "Apple", "Pear"]
print(fruits)

fruits.append(["Banana", "Watermelon"])
print(fruits)
# ['Cherry', 'Apple', 'Pear', ['Banana', 'Watermelon']]

# TODO : list.extend(iterable) : Extend the list by appending all the items from the iterable.
fruits.extend(["Keli", "Kalingad"])
print(fruits)
# ['Cherry', 'Apple', 'Pear', ['Banana', 'Watermelon'], 'Keli', 'Kalingad']

fruits.extend("String_Is_IterableToo")
print(fruits)

#BUT
# fruits.extend(4)
# will throw - TypeError: 'int' object is not iterable as INT is not iterable

# TODO Observe - append vs extends

# TODO : list.insert(i, x) : Insert an item at a given position.
#  The first argument is the index of the element before which to insert,
#  so a.insert(0, x) inserts at the front of the list,
#  and a.insert(len(a), x) is equivalent to a.append(x).

states = ["MH", "KA", 1, 2]
print(states)
states.insert(2, "GJ")
print(states)
states.insert(4, 3)
print(states)

# TODO : list.remove(x)
#  Remove the first item from the list whose value is equal to x.
#  It raises a ValueError if there is no such item.
removed_item = states.remove("GJ")
print(states)
# ['MH', 'KA', 1, 3, 2]

# observe - it returns nothing
print("Removed item - ", removed_item)
# Removed item -  None

# TODO : list.pop([i]) :Remove the item at the given position in the list, and return it.
#  If no index is specified, a.pop() removes and returns the last item in the list.
#  It raises an IndexError if the list is empty or the index is outside the list range.

cities = ["Pune", "Mumbai", "Nagpur", "Delhi"]
city = cities.pop(1)

print(cities)
# ['Pune', 'Nagpur', 'Delhi']
print(city)
# Mumbai

# if no index is used in argument, removes and returns last item from list
city = cities.pop()
print(cities)
# ['Pune', 'Nagpur']
print(city)
# Delhi

# TODO : list.clear() : Remove all items from the list.
removedCities = cities.clear()
print(removedCities)
# None
# observe it return nothing

# TODO : list.index(x[, start[, end]]) : Return zero-based index in the list
#  of the first item whose value is equal to x.
#  Raises a ValueError if there is no such item.
#  The optional arguments start and end are interpreted
#  as in the slice notation and are used to limit the search to
#  a particular subsequence of the list.
#  The returned index is computed relative to the beginning of the
#  full sequence rather than the start argument.

cars = ["Ertiga", "Creta", "Amaze", "Hycross", "Roxx", "GLS", "X7"]
gls_position_in_list = cars.index("GLS")
print("GLS position_in_list-", gls_position_in_list)
# GLS position_in_list- 5

hycross_position_in_list = cars.index("Hycross")
print("Hycross position_in_sub_list-", hycross_position_in_list)
# Hycross position_in_sub_list- 3

hycross_position_in_list = cars.index("Hycross", 1, 4)
print("Hycross position_in_sub_list-", hycross_position_in_list)

# Hycross position_in_sub_list- 3

# TODO : list.count(x) : Return the number of times x appears in the list.
cars.append("Hycross")
how_many_times_x = cars.count("Hycross")
print(how_many_times_x)
# 2

# TODO : list.sort(*, key=None, reverse=False)
#  key	Optional. A function to specify the sorting criteria(s)
#  reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
sorted_cars = cars.sort()

print("Sorted cars - ", sorted_cars)
# Sorted cars -  None

print("Sorted cars In place - ", cars)
# Sorted cars In place -  ['Amaze', 'Creta', 'Ertiga', 'GLS', 'Hycross', 'Hycross', 'Roxx', 'X7']
# observe sort function sorts list itself and not returns sorted list as return value

# TODO : list.reverse() - Reverse the elements of the list in place.
cars.reverse()
print(cars)
# ['X7', 'Roxx', 'Hycross', 'Hycross', 'GLS', 'Ertiga', 'Creta', 'Amaze']

# TODO - list.copy() : Return a shallow copy of the list.
#  You cannot copy a list simply by typing list2 = list1,
#  because: list2 will only be a reference to list1,
#  and changes made in list1 will automatically also be made in list2.
#  You can use the built-in List method copy() to copy a list.


new_car_list = cars.copy()
print(new_car_list)

# TODO : note - not all data can be sorted or compared
secular_list = [None, 'hello', 10]
# secular_list.sort() - will throw error  TypeError: '<' not supported between instances of 'str' and 'NoneType'
# because integers can’t be compared to strings and None can’t be compared to other types.

# TODO : The del statement - There is a way to remove an item from a list
#  given its index instead of its value as opposite to remove(x) function.

aList = [-1, 1, 66.25, 333, 333, 1234.5]
del aList[0]
print(aList)
# [1, 66.25, 333, 333, 1234.5]

del(aList[2:4])
print(aList)
# [1, 66.25, 1234.5]

# del can also be used to delete entire variables:
del aList
# Referencing the name aList hereafter is an error
print(aList)
