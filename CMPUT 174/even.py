even = []
for number in range(1 , 101):
    if number % 5 == 0 or number % 7 ==0:
        if number % 2 == 0:
            even.append(number)      # var.append(loop)
        else:
            print(number)