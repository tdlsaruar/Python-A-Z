av=5
var=int(input("How many time you wanna fly ?"))
i=1
while i<=var:
    if i>av:
        print("out of stock")
        break
    print("Saruar")
    i+=1
print("don't have")
for var in range(0,100):
    if var==20:
        continue
    print(var)