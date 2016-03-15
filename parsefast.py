
aar_MW = {'A':71.0779, 'R':156.1857, 'N':114.1026, 'D':115.0874, 'C':103.1429, 'E':129.114,
'Q':128.1292,'G': 57.0513, 'H': 137.1392, 'I':113.1576, 'L':113.1576, 'K':128.1723, 'M':131.1961,
'F':147.1739, 'P':97.1152, 'S':87.0773, 'T':101.1039, 'U':150.0379, 'W':186.2099, 'Y':163.1733, 'V':99.1311}


with open('hemoglobin.txt', 'r') as f:
    header = f.readline()
    sequence = ''
    print 'FASTA file: ' + header
    print 'amino acid sequence:\n'
    for x in f:
        print x


# alex is cool 



"""
l = ""
with open('hemoglobin.txt', 'r') as f:
    header = f.readline()
    for x in f:
        l += x.strip('\n')
        print l
"""





"""
## print the AA sequence and omit the first line of the file
f = open('hemoglobin.txt')
next(f)
for line in f:
    print line
## length including '\n'
    print len(line)
## length without '\n'
    print len(line.rstrip('\n'))
"""


"""
WITH-NEXT IDEA
with open('hemoglobin.txt') as f:
    next(f)
    for line in f:
        print line
        l = len(line)
        print l

WHILE-LOOP IDEA
f = open('hemoglobin.txt', 'r')

line = f.readline()

while line:
    print line

ENUMERATE IDEA
file_name = "hemoglobin.txt"
the_file = open(file_name)
file_contents = the_file.readlines()

for x, line in enumerate(the_file):
    print line[4]

with open("hemoglobin.txt") as f:
    print f.readlines()

->PIR database for accessing FASTA files to download

Syntax: with -to open a file:
with open("file","mode") as variable:
    # Read or write to the file

is

OBJECTIVE:
for amino_acid in l
make a new for loop
calculate the MW of hemoglobin, make a dictionary
Learn how to read the line at a given position
"""
