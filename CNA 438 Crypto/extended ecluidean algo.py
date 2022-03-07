a=7
b=4
x1=0 #(Xi-2)
x2 = 1 #(Xi-1)
y1 = 1 #(Yi-1)
y2 = 0 #(Yi-2)

if(b<a):
    a,b=b,a
r=a
while(r!=0):
    q=a//b
    r=a%b
    x=x2 - q*x1
    y=y2 - q*y1
    x2=x1
    x1 = x
    y2 = y1
    y1 = y

print(r, q, x, y)
    
