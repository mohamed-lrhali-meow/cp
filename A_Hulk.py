n = int(input())
out = ''
if n == 1 : 
    print("I hate it")
else : 
    for i in range(1,n+1): 
        if i %2 == 0 : 
            out += 'I love '
        else : 
            out += 'I hate '
        if i != n :
            out += "that "
    print(out + 'it')