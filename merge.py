f = open("/root/workspace/main.txt", "r")
contents = f.readlines()
f.close()

contents.insert(3,"""
b=8""")
f = open("/root/workspace/main.txt", "w")
contents = "".join(contents)
f.write(contents)
f.close()
