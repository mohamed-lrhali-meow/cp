n = int(input())
string = input()
c = 0
for i in range(n-1) :
    if string[i] == string[i+1] : 
        c +=1 
print(c)