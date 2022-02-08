#Difference among
# list=square brackets[] changeable
# tuple=rounded brackets()unchangeable
# set=the set keyword 
#  dictionary=curly braces {}

list1=["Computer","Saruar","Tv","Cricket"]
print(type(list1))
list1[0]="Saruar"
print(list1)
tuple1=("saruar","sabbir")
# tuple1[0]="Pc"#not going to works!
# tuple is immutable
print(type(tuple1))
print(tuple1)
set1=set(["saruar","tv",20,23])
print(type(set1))
print(set1)

dic1={"saruar":"tdl","tdl":"234","12":"days"} #intiger can't be used trough dictonary oh!that's really nice infromation for tdl saruar

user=input("enter")

print(type(dic1))
print(dic1[user])
# print(dic1[0])
