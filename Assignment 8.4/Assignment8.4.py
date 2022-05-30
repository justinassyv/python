fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    dataSet = line.split()
    for i in dataSet:
        if(i not in lst):
            lst.append(i)
lst.sort()
print(lst)
