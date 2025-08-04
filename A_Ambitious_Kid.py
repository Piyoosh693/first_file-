t= int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(abs(i))
print(min(b))