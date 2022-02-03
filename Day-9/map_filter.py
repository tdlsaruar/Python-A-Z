def var(x):
    return x*x
num=[1,2,5,5,6,7,8]
result=list(map(var,num))
print(result)

# filtering
list2=[1,23,12,1,24,5,34,5,2]
total=list(filter (lambda x:x%2==0,list2))
print(total)