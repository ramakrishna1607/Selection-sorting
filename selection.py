l=[5,3,8,6,7,2]
for i in range(len(l)-1):
    min=i
    for j in range(i,len(l)):
        if l[j]<l[min]:
            min=j
    temp=l[i]
    l[i]=l[min]
    l[min]=temp
    
print(l)
