    """
This program is used to convert degree celcius temperature in canada to farenheit in Springfield.

"""

temp_C = int(input(" Whats the Temperature is canada? "))             # This is to collect the temperature for the user 

# Formula to convert celcius to fahrenheit
temp_F = int(temp_C*( 9 / 5) + 32)                                       # This will convert the degree celcius to fahrenheit

print(temp_C,"Degrees in canada would be",temp_F,"degrees in Springfield. D'oh!") 

