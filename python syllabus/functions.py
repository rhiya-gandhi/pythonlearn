#sample text
text = " welcome to imcc"
#upper case
print("upper case", text.upper())

#lower case
print("lower case", text.lower())

#capitalize text
text = text.strip() # remove the spaces from the start
print("capitalize 1st word", text.capitalize())

#title case
print(text.title())

#strip spaces from both sides 
text = text.strip()
print("strip spaces from both sides", text)

#count concurrency of a substring
print("letter c occurs ", text.count("c"), "times in the text")

#find the index of a substring
print("position of letter imcc is ", text.find("imcc"))

#replace a substring with another substring
print(text.replace("imcc", "python magic")) #we can remove as well as add

#check if string start with a substring or ends with a substring
print("does the text start with 'rhi' ", text.startswith("rhi"))
print("does the text end with 'imcc' ", text.endswith("imcc"))

#split the string into a list of words
print("split the string into a list of words", text.split())

#join the list of words into a string
words = ["welcome", "to", "imcc"]
print("join the list of words into a string", " ".join(words))


