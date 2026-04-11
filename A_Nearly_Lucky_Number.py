n = int(input())
def is_lucky(x): 
    while x >= 10 : 
        if (x %10 != 4) and x %10 != 7 : 
            return False 
        x //= 10
    if x == 7 or x == 4 : 
        return True 
    else : 
        return False
if is_lucky(str(n).count('7') + str(n).count('4')) : 
    print("YES")
else :
    print("NO")