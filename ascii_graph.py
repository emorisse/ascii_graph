import fileinput

items = []
for line in fileinput.input():
    items.append(float(line.strip()))

# assume 80 x 24 terminal
# let's use 20 lines for display

lines = [[" " for i in range(len(items))] for x in range(20)]

M = max(items)
m = min(items)
diff = abs(M-m)

# source for remap: https://stackoverflow.com/a/15537393 by PenguinTD
def remap( x, oMin=m, oMax=M, nMin=0, nMax=19):

    #range check
    if oMin == oMax:
        print "Warning: Zero input range"
        return None

    if nMin == nMax:
        print "Warning: Zero output range"
        return None

    #check reversed input range
    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    #check reversed output range
    reverseOutput = False
    newMin = min( nMin, nMax )
    newMax = max( nMin, nMax )
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result

for k,i in enumerate(items):
    I = int(remap(i))
    #print("{},{},{}".format(k,i,I))
    lines[I][k] = "*"

lines.reverse()
size=len(str(max(items)/20*(20-i)))
for i,line in enumerate(lines):
    i = M - i * diff/20
    print("{:10.4f}\t{}".format(i,"".join(line)))
