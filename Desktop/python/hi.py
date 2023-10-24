x=int(input('enter'))
y=int(input('enter'))
if x>y:
    for i in range(1,1,-1):
        if x%i==0 and y%i==0:
            print(i)
else:
    for j in range(1,i+1):
        if x%j==0 an y%j==0:
            print(j)
print('lcm'(x*y)/2)
