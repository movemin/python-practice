my_file = open("file/test.txt", "r")
st = my_file.read()
print(st)
my_file.close()

with open("file/test.txt", "r") as my_file:
    st = my_file.read()
    print(st)

with open("file/write.txt", "w") as my_write_file:
    my_write_file.write("what's your name?")

with open("file/write.txt", "a") as add_file:
    add_file.write("My name is bulabulabula guackra")

with open("file/write.txt", "r") as wr:
    st = wr.read()
    print(st)