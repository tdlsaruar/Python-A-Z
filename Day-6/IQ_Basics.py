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
f =opent("saruar.txt")
for line in f:
    print(line,end="")
f.close()
