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
    



