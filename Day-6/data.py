# python has the following data types buit-in by defeult,in these categories
# string,integer,floating,list,tuple,range,dictonary,boolean,binary
# getting the data type 

# write type(var)
var="Saruar"
var1=1
var2="Tdl"
var,var2=var2,var
print(var,var2)
name=var+" " +var2
print(name)
# index slicing mathods
index=[2,234,23,"tdl saruar"]
index.append("good")
print(f"How was the learning trip man{index[0:]}")
list=[2,234,234,23,3,34]
list.remove(2)
print(list)
list.sort() #if i use sort class number listing 1,2,3,4,.... how cool this class
print(list)
fun=[0,2,3,3,5,"saruar"]
print(fun.insert(0,3))
print(fun.count('saruar'))#if we use count mathod we have to provide something count (bla) but it has to one thing it takes one 
print(len(fun))
mathod="tdl saruar how are you "
print(mathod.title())#upper lower title 
task=input("Enter you are name :")
print(f"You are name is {task.title()}")


dict={"tdl":"Saruar","father":"abdus salik","mother":"Roftara bibi","age":19,"class":"hsc22"}
user=input("Enter you are question about me :")
print(f"you are information is :{dict[user]}")


