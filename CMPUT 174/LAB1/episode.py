"""
This code converts a standard format of a show to an expanded format to make it more explanatory 

"""

name = input(" What is the name of the episode? ") #S33_E20_Marge the Meanie
position_E = name.index("E")                     #  To find index of E 
position_S = name.index("S")                     #  To find index of S 
position_underscore = name.index("_")            #  To find index of _


string_1 = name[ position_S + 1: position_underscore ]      #To extract the season number from the name 


string_2 = name[position_underscore + 1 : ]                 #To extract string from E__ until the end which is later used to extract the episode

string_4 = string_2[ position_underscore  : ]            #To extract name of the episode


string_3 = string_2[position_E - 3 :  position_underscore]  #To extract episode number from the name

#This is the format it will be expanded to 
print("Seasons", string_1 + "," ,"Episode",string_3 + ":", string_4,"(The Simpsons)")

