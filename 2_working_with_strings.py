
# ----------------------------------------
# . Working with Strings
# ----------------------------------------

# Strings are sequences of characters enclosed in quotes (' ' or " ")
greeting = "Hello"
name = "World"

# ----------------------------------------
# Basic String Operations
# ----------------------------------------

# # 1. Concatenation: Combining strings using the + operator
# message = greeting + " " + name
# print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

phrase = "Python is FUN!"
name = "JOSHUA WOODWARD"
# Convert all characters to lowercase
print("Lowercase:", phrase.lower())  # Output: python is fun!
print("Lowercase name:", name.lower())
print("uppercase name:", name.upper())

# Convert all characters to uppercase
print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!

# Check if all characters are uppercase
print("Is Uppercase?", phrase.isupper())  # Output: False
print("Is Uppercase?", name.isupper())
# Find the length of the string
print("Length of phrase:", len(phrase))  # Output: 14

# ----------------------------------------
# 3. Indexing and Slicing
# ----------------------------------------

chicago_mayor = "Johnson"
print("First letter of mayor's name:", chicago_mayor[0])
print("Last letter of mayor's name:", chicago_mayor[-1])
print("middle letter of mayor's name", chicago_mayor[-3])
last_name = "Woodward"
print("First letter of last name:", last_name[0])
print("First letter of last name:", last_name[-1])                           
poppins = "supercalifragilisticexpialidocious" 
print("Last set of letters in poopins:", poppins[-7:])
print("first set of letters in poopins:", poppins[0:5])

declaration = "The unanimous Declaration of the thirteen united States of America, When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.--That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, --That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn, that mankind are more disposed to suffer, while evils are sufferable, than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.--Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world."
print(len(declaration)) 


# Indexing: Access characters by position (0-based index)
print("First character:", phrase[0])  # Output: P
print("Last character:", phrase[-1])  # Output: !
##FIRST NUMBER INCLUSIVE NEXT NUMBER EXCLUSIVE
# Slicing: Get a range of characters (start inclusive, end exclusive)
print("Characters 1 to 4:", phrase[1:4])  # Output: yth

# Example combining everything:
print("Formatted Example:", (greeting + " " + name + "!").upper())
# Output: HELLO WORLD!


# ----------------------------------------
# 7. Strings: Advanced Concepts
# ----------------------------------------

# Creating Strings: use single or double quotes
greeting1 = 'Hello'
greeting2 = "Hi there"

# Printing Strings
print(greeting1)
print(greeting2)

# ----------------------------------------
# String Methods
# ----------------------------------------

sentence = "Python is fun to learn"

# .split(): Splits the string into a list of words
words = sentence.split()
print("Split result:", words)

# .format(): Allows inserting values into strings using {}
name = "Marvin"
age = 35
intro = "My name is {} and I am {} years old.".format(name, age)
print(intro)

# You can also use f-strings (Python 3.6+)
intro_fstring = f"My name is {name} and I am {age} years old."
print(intro_fstring)
