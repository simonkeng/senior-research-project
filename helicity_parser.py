#!/usr/bin/env python
import math

protein_names_and_segments = {}
protein_names_and_sequences = {}
protein_name = ''
protein_sequence = ''


FILE_INPUT = 'BetaBarrelTrimericSeq.txt'
FILE_OUTPUT = 'BBarrelTriOUTTESTER.csv'
sequence_file = open(FILE_INPUT)
output_file = open(FILE_OUTPUT, 'w')

### not being used ###
# TM Finder helicity scale by Charles M. Deber, et al.
helical_propensity_scale = {
    'F': 1.26,
    'W': 1.07,
    'L': 1.28,
    'I': 1.29,
    'M': 1.22,
    'V': 1.27,
    'C': 0.79,
    'Y': 1.11,
    'A': 1.24,
    'T': 1.09,
    'E': 0.85,
    'D': 0.89,
    'Q': 0.96,
    'R': 0.95,
    'S': 1.00,
    'G': 1.15,
    'N': 0.94,
    'H': 0.97,
    'P': 0.57,
    'K': 0.88
}

### not being used ###
# hydrophobicity scale: Wimley & White
amino_acid_hydrophobicities = {
    'A': 0.5,
    'C': -0.02,
    'D': 3.64,
    'E': 3.63,
    'F': -1.71,
    'G': 1.15,
    'H': 0.11,
    'I': -1.12,
    'K': 2.8,
    'L': -1.25,
    'M': -0.67,
    'N': 0.85,
    'P': 0.14,
    'Q': 0.77,
    'R': 1.81,
    'S': 0.46,
    'T': 0.25,
    'V': -0.46,
    'W': -2.09,
    'Y': -0.71
}


def get_protein_name(line):
    return line.lstrip('>').split(':')[0]


def get_segments(line):
    segment = []
    for element in line.lstrip('>').split(':')[1].split(';'):
        segment.append([int(element.split('.')[1].split(',')[0]), int(element.split('.')[1].split(',')[1])])
    return segment


# output_file.write('protein' + '\t' + 'start' + '\t' + 'end' + '\t' + 'segment' + '\t' + 'length' + '\t' + 'Gly' + '\t' + 'Ala' + '\t' + 'Cys' + '\t' + 'Trp' + '\t' + 'Tyr' + '\t' + 'Pro' + '\t' + 'Thr' + '\t' + 'Ser' + '\t' + 'Asn' + '\t' + 'Gln' + '\t' + 'Asp' + '\t' + 'Glu' + '\t' + 'His' + '\t' + 'Lys' + '\t' + 'Arg' + '\t' + 'Met' + '\t' + 'Phe' + '\t' + 'Leu' + '\t' + 'Val' + '\t' + 'Ile' + '\n')


# print 'Protein' + 'Gly' + 'Ala' + 'Cys'


for line in sequence_file:
    if line.startswith('>'):
        protein_name = get_protein_name(line)
        protein_names_and_segments[protein_name] = get_segments(line)
        protein_names_and_sequences[protein_name] = ''
    else:
        sequence = protein_names_and_sequences.get(protein_name)
        sequence += line.strip('\n' and '\r' and '\r\n' and '\n\r')
        protein_names_and_sequences[protein_name] = sequence

for key in protein_names_and_segments.keys():

    l = []
    t = 0

    l.append(key)

    for segment in protein_names_and_segments.get(key):

        segment_sequence = protein_names_and_sequences.get(key)[segment[0] - 1:segment[1]]

        Gly = segment_sequence.count('G')
        Ala = segment_sequence.count('A')
        Cys = segment_sequence.count('C')
        Trp = segment_sequence.count('W')
        Tyr = segment_sequence.count('Y')
        Pro = segment_sequence.count('P')
        Thr = segment_sequence.count('T')
        Ser = segment_sequence.count('S')
        Asn = segment_sequence.count('N')
        Gln = segment_sequence.count('Q')
        Asp = segment_sequence.count('D')
        Glu = segment_sequence.count('E')
        His = segment_sequence.count('H')
        Lys = segment_sequence.count('K')
        Arg = segment_sequence.count('R')
        Met = segment_sequence.count('M')
        Phe = segment_sequence.count('F')
        Leu = segment_sequence.count('L')
        Val = segment_sequence.count('V')
        Ile = segment_sequence.count('I')

        t += len(segment_sequence)


        l.append(Ala)


    a = sum(l[1:])

    l.insert(1, a)
    l.insert(2, t)
    print ', '.join(str(i) for i in l[0:3])


    # output_file.write(', '.join(str(i) for i in l) + '\n')


        # output_file.write(key + '\t' + str(segment[0]) + '\t' + str(segment[1]) + '\t' + segment_sequence + '\t' + str(len(segment_sequence)) + '\t' + str(Gly) + '\t' + str(Ala) + '\t' +  str(Cys) + '\t' + str(Trp) + '\t' + str(Tyr) + '\t' + str(Pro) + '\t' + str(Thr) + '\t' + str(Ser) + '\t' + str(Asn) + '\t' + str(Gln) + '\t' + str(Asp) + '\t' + str(Glu) + '\t' + str(His) + '\t' + str(Lys) + '\t' + str(Arg) + '\t' + str(Met) + '\t' + str(Phe) + '\t' + str(Leu) + '\t' + str(Val) + '\t' + str(Ile) + '\n')



        # output_file.write(key + '\t' + str(segment[0]) + '\t' + str(segment[1]) + '\t' + segment_sequence + '\t' + str(len(segment_sequence)) + '\t' + 'Gly' + '\t' + str(Gly) + '\t' + 'Ala' + '\t' + str(Ala) + '\t' + 'Cys' + '\t' + str(Cys) + '\t' + 'Trp' + '\t' + str(Trp) + '\t' + 'Tyr' + '\t' + str(Tyr) + '\t' + 'Pro' + '\t' + str(Pro) + '\t' + 'Thr' + '\t' + str(Thr) + '\t' + 'Ser' + '\t' + str(Ser) + '\t' + 'Asn' + '\t' + str(Asn) + '\t' + 'Gln' + '\t' + str(Gln) + '\t' + 'Asp' + '\t' + str(Asp) + '\t' + 'Glu' + '\t' + str(Glu) + '\t' + 'His' + '\t' + str(His) + '\t' + 'Lys' + '\t' + str(Lys) + '\t' + 'Arg' + '\t' + str(Arg) + '\t' + 'Met' + '\t' + str(Met) + '\t' + 'Phe' + '\t' + str(Phe) + '\t' + 'Leu' + '\t' + str(Leu) + '\t' + 'Val' + '\t' + str(Val) + '\t' + 'Ile' + '\t' + str(Ile) + '\n')

sequence_file.close()
output_file.close()
