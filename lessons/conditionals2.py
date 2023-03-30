"""Knock knock joke with conditionals"""

inter_cow: str = input("Do you want an interruption cow? ")

if (inter_cow == "yes"):
    print("Knock, knock.")
    print(". . . who's there?")
    print("Interruption cow.")
    print(". . . interrupting cow wh--")
    print("MOO!")
elif (inter_cow == "you're not funny"):
    print("Wow . . . that hurts my feelings . . . :'(")
else:
    print("Oh . . . okay. . . :(")