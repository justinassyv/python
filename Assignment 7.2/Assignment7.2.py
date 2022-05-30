# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

counter = 0
result = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        p= float(line[20:])
        result = result + p
        counter = counter + 1
print('Average spam confidence:', result/counter)
