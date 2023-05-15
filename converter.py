import classes
filename='input.txt'
file = open(filename)

g=classes.graf(file.readline().strip(),file.readline().split(),file.readline().split())

lines=file.read().splitlines()
for line in lines:
    g.add(*line.split())


g.get_dfa()
