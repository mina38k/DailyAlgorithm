w,h,b=map(int,input().split())
e=(w*h*b)/(8*1024*1024)
print(format(e,".2f"),"MB")