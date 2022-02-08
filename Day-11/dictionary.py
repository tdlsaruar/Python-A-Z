dict={"tdl":"saruar","father":"Abdus Salik Talukder","mother":"roftara bibi talukder"}
user=input("Enter you are name :")
dict.update({"Saruar":"Talukder sAruar"})
print(dict)
dict.pop("tdl")
print(dict)
print(dict[user].title())

# list function
num=[1,3,2,5,4,7,9,41]
print(num.sort())
print(num.reverse())
a="Saruar"
b="Tdl"
a,b=b,a
print(a,b)
print(type(num))
ld=["saruar","sabbir","sihab"]
print(ld)
ld.append("saruar[0]")
print(ld)
ld.remove(ld[2])
print(ld)