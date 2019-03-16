

s = input("Please, type your path (use U  - for uphill step, D - for downhill step): ")
n= len(s)

print ("Number of steps is:  ") 
print(n)
print ("Number of valley is: ")


def Counting_valley(s):
    valley = 0
    sea_level = 0
    
    for step in s:
        if step == 'D':
            sea_level -= 1 #sea_level = sea_level-1 = -1
        else:
            if sea_level == -1:
                valley += 1 #valley=valley+1 = 1
            sea_level += 1 #sea_level = -1+1 = 0 (vozvrashenie v ishodnoe polojenie.)
    return valley

print(Counting_valley(s))











   
   
    
    


