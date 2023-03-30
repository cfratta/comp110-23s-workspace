"""Example functions to learn definition and calling syntax"""

#def my_max(number1: int, number2: int) -> int:
#    """Returns the maxmimum value out of two numbers"""
 #   if number1 >= number2:
  #      return number1
   # else: # number1 < number2
    #    return number2
    
#max_number: int = my_max(1,10)
#other_max_number: int = my_max(11,3)
#print(other_max_number)

def my_function(number4: int, haha: str) -> bool:
    """test"""
    if number4 is not len(haha):
        return len(haha)
    
    return number4

q: bool = my_function(3, "daisy")
print(q)


# in class 23/02/09

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

x: str = mimic("Hey, Sally")
print(x)

my_words: str = "Hello!"
response: str = mimic(my_words)
print(response)

"""Write a different mimic function: you input a string and an index and it returns the letter at that index.
If the index is too high for the string length, return "Too high of an index"."""

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words): # if index is outside of bounds
        return "Too high of an index" # if you reach a return, you exit the function so I don't NEED an else.
    # else: # return the letter in the word at desired index # if I reach this line, that means the letter_idx is valid'''
    return my_words[letter_idx]
    
y: str = mimic_letter("python", 5)
print(y)

p: str = "Hello\nworld!!!\n:) :\\"
print(p)