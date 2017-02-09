#!/usr/bin/env python
import math

protein_names_and_segments = {}
protein_names_and_sequences = {}
protein_name = ''
protein_sequence = ''


FILE_INPUT = 'BetaBarrelTrimericSeq.txt'
FILE_OUTPUT = 'BetaBarrelTrimericSeqHelicityOutput.txt'
sequence_file = open(FILE_INPUT)
output_file = open(FILE_OUTPUT, 'w')

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
        segment.append([int(element.split('.')[1].split(',')[0]), \
            int(element.split('.')[1].split(',')[1])])
    return segment



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
    for segment in protein_names_and_segments.get(key):

        segment_sequence = protein_names_and_sequences.get(key)[segment[0] - 1:segment[1]]
        hydrophobicity = 0.0
        helicity = 0.0

        for (index, aminoacid) in enumerate(segment_sequence):
            helicity += helical_propensity_scale.get(aminoacid)
            hydrophobicity += amino_acid_hydrophobicities.get(aminoacid)

        output_file.write(key + '\t' + str(segment[0]) + '\t' + str(segment[1]) + \
            '\t' + segment_sequence + '\t' + str(helicity) + '\t' + str(hydrophobicity) + '\n')

sequence_file.close()
output_file.close()
