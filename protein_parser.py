#!/usr/bin/env python

# molecular weights of amino acid residues, in g/mol
aar_MW = {
    'A': 71.0779,
    'R': 156.1857,
    'N': 114.1026,
    'D': 115.0874,
    'C': 103.1429,
    'E': 129.114,
    'Q': 128.1292,
    'G': 57.0513,
    'H': 137.1392,
    'I': 113.1576,
    'L': 113.1576,
    'K': 128.1723,
    'M': 131.1961,
    'F': 147.1739,
    'P': 97.1152,
    'S': 87.0773,
    'T': 101.1039,
    'U': 150.0379,
    'W': 186.2099,
    'Y': 163.1733,
    'V': 99.1311,
    '\n': 0
}

# pI calculation used on line 66 "average_pI()", has minimal accuracy and does not consider several other
# factors necessary when calculating the isoelectric point. This was an experiment.  
pI_each_AA = {'G': 5.97, 'A': 6.00, 'V': 5.96, 'L': 5.98, 'I': 6.02, 'M': 5.74, 'P': 6.30, 'F': 5.48, 'W': 5.89, 'N': 5.41,
'Q': 5.65, 'S': 5.68, 'T': 5.60, 'Y': 5.66, 'C': 5.07, 'D': 2.77, 'E': 3.22, 'K': 9.74, 'R': 10.76, 'H': 7.59}

file_name = 'acetylcholinesterase.txt'

f = open(file_name, 'r')
sequence = ''
header = ''
for line in f:
    if line.startswith('>'):
        header = line
    else:
        sequence += line.strip('\n')

# calculate total number of amino acids in sequence
def calc_AA_tot(sequence):
    return len(sequence)

# calculate molecular weight of sequence
def calc_MW(sequence):
    count = 18.02
    for aminoacid in sequence:
        count += aar_MW[aminoacid]
    return count

# calculate percent of each amino acid in sequence
def percent_each_AA(sequence):
    all_AA = 'ARNDCEQGHILKMFPSTUWYV'
    length = len(sequence)
    for AA in all_AA:
        num_AA = sequence.count(AA)
        percent_AA = num_AA * 100 / length
        print str(percent_AA) + '%' + ' of ' + AA + ' (' + str(num_AA) + ')'


# calculate (theoretical pI) <-- MINIMAL ACCURACY
# sum up all the pI's of each amino acid in the sequence and divide by length of the sequence
def average_pI(sequence):
    count = 0
    for aminoacid in sequence:
        count += pI_each_AA[aminoacid]
        count_2 = count / len(sequence)
    return count_2

print calc_AA_tot(sequence)
print calc_MW(sequence)
print average_pI(sequence)
percent_each_AA(sequence)
# print segment_seq(sequence)

"""
Additional Notes:
- Website for reference: protparam
- PIR database for accessing FASTA files to download
- hydrophobic amino acids: G, A, V, L, I, P, F, M, W (9 characteristic)
- using this source for calculating pI http://www.mhhe.com/physsci/chemistry/carey5e/Ch27/ch27-1-4-2.html
"""
