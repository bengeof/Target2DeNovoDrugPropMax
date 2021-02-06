outputlist=[]
with open('smilesoutt2d.txt', 'r') as output:
    for line in output:
        line = line.split(';')
        outputlist.append(line[1][:-1])
print(outputlist)        
with open('benoutt2d.txt', 'a') as outfile:
    outfile.write(str(outputlist))
