"""
Exercise 4: Add code to the above program to figure out who has the most
messages in the file. After all the data has been read and the dictionary
 has been created, look through the dictionary using a maximum loop
 (see Chapter 5: Maximum and minimum loops) to find who has the most messages
  and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195

"""
fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('The file cant be opened', fname)
    exit()

mails = dict()
highest = None
sender = None

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in mails:
            mails[words[1]] = 1
        else:
            mails[words[1]] += 1

for mail, number in mails.items():
    if highest is None or number > highest:
        highest = number
        sender = mail

print(sender, highest)
