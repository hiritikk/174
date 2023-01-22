#cat-fishing

catch_limit = 7
release_limt = 3
trout_needed = 5

caught = 0
released = 0
trouts = 0                                                          

condition = caught < catch_limit and trouts <= trout_needed
while condition:
    catch = input(" trout y/n" )
    if catch == 'y':
        trouts += 1
        caught += 1
    else:
        if released < release_limt:
            print("Relesaing the fish back into the lake")
            released += 1
        else:
            caught += 1 
    print(f'caught: {caught}/{catch_limit}')
    print(f'released: {released}/{release_limt}')
    print(f'Trouts: {trouts}/{trout_needed}')
    condition = caught < catch_limit and trouts <= trout_needed
print("fishing ends here")
if trouts == trout_needed:
    print("Trout cake! ")
else: 
    print('Seafood medley')
    
