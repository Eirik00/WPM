import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
name = "TEJIATJEII"
f = open("LOCALSAVE/" + name + ".dll", "w")
f.write("cool")
f.close()

input()
