import fileinput

items = []
for line in fileinput.input():
    items.append(float(line.strip()))

#print(items)

# assume 80 x 24 terminal
# let's use 20 lines for display

lines = [[" " for i in range(len(items))] for x in range(20)]
#print(lines)

# assumes all numbers are positive
for k,i in enumerate(items):
    I = int(round(i/max(items) * 19,0))
    #print("{},{},{}".format(k,i,I))
    #print(lines[I][k])
    lines[I][k] = "*"
    #print(lines[I][k])

lines.reverse()
size=len(str(max(items)/20*(20-i)))
for i,line in enumerate(lines):
    i = max(items)/20*(20-i)
    print("{:10.4f}\t{}".format(i,"".join(line)))
