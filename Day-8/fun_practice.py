def las_char(name):
    return name[-1]
tdl=las_char("tdl")
print(tdl)

def name(name):
    return name
s=name("tdl saruar")
print(s)

def odd_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
saruar=odd_even(5)
print(saruar)

def is_even(sum):
    if sum%2==0:
        return True
    else:
        return False
total=is_even(6)
print(total)

def fun(a,b):
    if a>b:
        return a
    else:
        return b
num1=int(input("Enter the number :"))
num2=int(input("Enter the number 2 :"))
ans=fun(num1,num2)
print(f"{fun} the number is")