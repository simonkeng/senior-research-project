
aar_MW = {'A':71.0779, 'R':156.1857, 'N':114.1026, 'D':115.0874, 'C':103.1429, 'E':129.114,
'Q':128.1292,'G': 57.0513, 'H': 137.1392, 'I':113.1576, 'L':113.1576, 'K':128.1723, 'M':131.1961,
'F':147.1739, 'P':97.1152, 'S':87.0773, 'T':101.1039, 'U':150.0379, 'W':186.2099, 'Y':163.1733, 'V':99.1311, '\n':0}


f = open('hemoglobin.txt', 'r')
sequence = ''
header = ''

for line in f:
    if line.startswith('>'):
        header = line
    else:
        sequence += line.strip('\n')


# calculate total number of amino acids
def calc_AA_tot(sequence):
    return len(sequence)

# calculate molecular weight of sequence
def calc_MW(sequence):
    count = 18.02
    for aminoacid in sequence:
        count += aar_MW[aminoacid]
    return count


print calc_AA_tot(sequence)
print calc_MW(sequence)












"""
NOTES:

l = ""
with open('hemoglobin.txt', 'r') as f:
    header = f.readline()
    for x in f:
        l += x.strip('\n')
        print l

## print the AA sequence and omit the first line of the file
f = open('hemoglobin.txt')
next(f)
for line in f:
    print line
## length including '\n'
    print len(line)
## length without '\n'
    print len(line.rstrip('\n'))

PIR database for accessing FASTA files to download
"""
