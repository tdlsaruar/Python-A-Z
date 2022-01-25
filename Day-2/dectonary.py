mind={"flock":"group of bird" ,"dazzling":"very nice","amazing":"nice"}#this type is set 
print(mind["flock"])
mind.update({"tdl":"Saruar"})#update mathod for add something or edit data you can change word meaning or data 
mind.update({"dazzling":"very very nice"})
del mind["flock"]#del use for delet thing or data 
mind.pop("amazing")#pop also use for delet files or data etc
print(mind)
newdic=mind.copy()#copy class use for copy files or anything 
print(mind)
user_input=input("Enter you are word :")
print(mind[user_input])