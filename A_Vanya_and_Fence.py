n , h = map(int,input().split())
friends = list(map(int,input().split()))
l = 0
for friend in friends : 
    if friend > h : 
        l += 2
    else : 
        l +=1 
print(l)