# a=[2,3,4,5,6]
# for i in range (len(a)):
#     print(i)

# for i in range (len(a)):
#     print(a[i])

a=[7,4,5,6,4]
n=len(a)
c=0
for i in range (n):
    for j in range(n-1):
        c=c+1
        if a[j]>a[j+1 ]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print("outtttttt" )
for i in a:
    print(i,end=" ")
print("total hits=",c)