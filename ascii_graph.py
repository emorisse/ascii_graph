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
        print("Warning: Zero input range")
        return None

    if nMin == nMax:
        print("Warning: Zero output range")
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
size = m - 19 * diff/20
#dot = str(size - int(size))
dot = len('{:.100f}'.format(size - int(size)))
#dot = len(str(size - int(size))) - 3 # remove for initial "0."
size = len(str(size)) + 1

#format_str = "{" + ":{}.{}f".format(size,dot) + "}\t{}"
#format_str = "{:.3e}\t{}"
if (diff>100):
    format_str = "{:>10.1f}\t{}"
elif (diff>10):
    format_str = "{:>10.2f}\t{}"
elif (diff>1):
    format_str = "{:>10.3f}\t{}"
else:
    format_str = "{:>10.10f}\t{}"
#print(format_str)
bins = [ M-x*diff/19 for x in range(0,20) ]
#bins.reverse()
#print(bins)
for i,line in zip(bins,lines):
    print(format_str.format(i,"".join(line)))
