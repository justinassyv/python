#word = 'brontosaurus'
#d = dict()

#for c in word:
#    d[c] = d.get(c, 0) +1

#print(d)
#----------------------------------------------------------------------
#fname = input('Enter a file name:')
#try:
#    fhand = open(fname)
#except:
#    print('File can not be opened:', fname)
#    exit()
#
#counts = dict()
#
#for line in fhand:
#    words = line.split()
#    for word in words:
#        if word not in counts:
#            counts[word] = 1
#        else:
#            counts[word] += 1
#print(counts)
#--------------------------------------------------------------------------------
#!/usr/bin/env python3
"""
Exercise  9.2: Write a program that categorizes each mail message by which day
of the week the commit was done. To do this, look for lines that start with
"From", then look for the third word and keep a running count of each of the
days of the week. At the end of the program, print out the contents of your
dictionary (order does not matter).
Sample Line: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""

fname = input('Enter a file name:')
try:
    fhand = open(fname)
except:
    print('File can not be opened', fname)
    exit()

dictionary_days = dict()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1
        else:
            dictionary_days[words[2]] += 1
print(dictionary_days)
