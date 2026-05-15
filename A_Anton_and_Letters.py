s = input()
not_wanted = [',', '{','}',' ']
out = []
for i in s : 
    if i not in not_wanted : 
        out.append(i)

print(len(set(out)))