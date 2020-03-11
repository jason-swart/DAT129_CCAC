"""
JSwart DAT129 Week 7
Peer tutorial exercise on Lambda functions.

This takes a list of dictionaries and uses the lambda function embeded into a sorted()
print function to sort the list by the categories defined in the dictionaries.

"""


#creating a list of dictionaries that will need to be sorted
horrorAuthors = [{ "name" : "Stephen King", "books" : 94 }, 
{ "name" : "Clark Ashton Smith", "books" : 87 }, 
{ "name" : "Edgar Allen Poe", "books" : 43 }, 
{ "name" : "H.P.Lovecraft", "books" : 34 }, 
{ "name" : "Ramsey Campbell", "books" : 30 }, 
{ "name" : "Brian Lumely", "books" : 100 }, 
{ "name" : "Kim Newman", "books" : 37 }, 
{ "name" : "Neil Gaiman", "books" : 32 }, 
{ "name" : "Clive Barker", "books" : 7 }]

#Brief output explaining what's being displayed after sorting.
print("The authors list printed, sorting by name and number of books: ")

#Printing using the sorted() function with an embeded lambda function to sort the list by name and number of books.
#I was going to use pprint, but the sorted() function does not work with pprint - or I couldn't get it to work.
print sorted(horrorAuthors, key = lambda i: (i["name"], i["books"]))