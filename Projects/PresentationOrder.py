import random
names = ["Thomas", "Daniel", "Mitchell", "Matthew", "Issa", "Justin","Brisa","Kolade","Reed"]

random.shuffle(names)

i = 1

for name in names:
    print(str(i) + "    " + name)
    i += 1
