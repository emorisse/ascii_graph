import fileinput

items = []
for line in fileinput.input():
    items.append(float(line.strip()))

#print(items)

# assume 80 x 24 terminal
# let's use 20 lines for display

lines = [[" " for i in range(len(items))] for x in range(20)]
#print(lines)


for k,i in enumerate(items):
    I = int(i/max(items) * 20) -1
    #print("{},{},{}".format(k,i,I))
    #print(lines[I][k])
    lines[I][k] = "*"
    #print(lines[I][k])

lines.reverse()
for i,line in enumerate(lines):
    i = round(max(items)/(i+1),1)
    print("{}\t{}".format(i,"".join(line)))
