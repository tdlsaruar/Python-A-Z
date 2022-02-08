import re


print(1,2,3)
print(1,2,3)
print(1,2,3)
def displaying(row,row1,row3):
    print(row)
    print(row1)
    print(row2)
row=[' ',' ',' ']
row1=[' ',' ',' ']
row2=[' ',' ',' ']

row1[1]='X'
displaying(row,row1,row2)


index_position=int(input("Enter you are number "))
print(row2[index_position])

def user_choice():
# while choice.isdigit()==False:
    choice=input("Enter you are number 0-10 : ")
    if choice.isdigit()==False:
        print("sorry")
        return int(choice)
        