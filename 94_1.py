n=int(input())
k=list(map(int,input().split()))

min=k[0]
for i in range(n):
    if k[i] < min:
        min=k[i]
print(min)