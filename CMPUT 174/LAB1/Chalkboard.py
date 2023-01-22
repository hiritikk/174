"""
This program is used to replicate the string multiple times

"""
string = input(" What is the phrase? ")                             # User enters the pharse when prompted
num = int(input(" How many times do you want to write it "))        # Number of times it needs to be replicated
space = string+" "                                                  # This acts as a fail-safe, this makes sure theres space between every replicated line

print(space * num, end=" ")