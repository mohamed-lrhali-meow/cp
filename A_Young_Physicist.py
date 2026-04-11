n = int(input())
x=0
y = 0 
z = 0 
for i in range(n): 
    temp_x , temp_y , temp_z = map(int,input().split())
    x += temp_x
    y += temp_y
    z += temp_z

print("YES" if x == 0 and y == 0 and z == 0 else "NO" )