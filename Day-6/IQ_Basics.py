# IQ basics 
# "r" - Open file for reading
# "w" --- Open a file for writing
# "x"- Create file fi not exists
# "a"-Add moe content to a file
# "t"-text mode
# "b"--binary mode/ 
# "+"-- read and write 
# f=open("saruar.txt")
# content=f.read()
# print(content)
with open('saruar.txt',mode='r') as f:
    print(f.read())
with open ('saruar.txt',mode='a') as f:
    f.write('\n this is fourth lines')
with open ('saruar.txt',mode='r') as f:
    print(f.read())