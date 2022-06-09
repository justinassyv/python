"""
Exercise 5: This program records the domain name (instead of the address)
 where the message was sent from instead of who the mail came from
 (i.e., the whole email address). At the end of the program, print out
 the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

"""
stuff = dict()
print(stuff['candy'])
fname = input('Enter the file name:')

try:
    fhand = open(fname)
except:
    print('Not possible to open the file', fname)
    exit()

dictionary_domains = dict()

for line in fhand:
    word = line.split()
    if len(word) < 2 or word[0] != 'From':
        continue
    else:
        domain = word[1].split('@')[1]
        if domain not in dictionary_domains:
            dictionary_domains[domain] = 1
        else:
            dictionary_domains[domain] += 1

print(dictionary_domains)
