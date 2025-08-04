for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=a.count(1)
    if c<n:
        min=0 if c%2==0 else 1
        max=c
    else:
        min=0 if c%2==0 else 1
        max=2*n-c
    print(min,max)
        