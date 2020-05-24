f = open("main.py", "r")
contents = f.readlines()
f.close()

contents.insert(3,"""
b=8""")
f = open("main.py", "w")
contents = "".join(contents)
f.write(contents)
f.close()