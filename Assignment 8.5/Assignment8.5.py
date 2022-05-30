fname = input("Enter a file name: ")
if len(fname) < 1:
    fname = "test.txt"

fh = open(fname)
count = 0

for line in fh:
    if not line.startswith("From"):
        continue
    elif line.startswith("From:"):
            continue
    else:
        count = count+1
        address = line.split()
        print(address[1])

print("There were", count, "lines in the file with From as the first word")
