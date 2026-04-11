vowels = ('a','e','o','y','u','i')
s = input()
result=''
for i in s : 
    if i.lower() not in vowels : 
        result += '.'+ i.lower()
print(result)
    