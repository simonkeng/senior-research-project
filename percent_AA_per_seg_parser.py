#!/usr/bin/env python

import collections
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import csv
import os
import sys
import subprocess


protein_names_and_segments = {}
protein_names_and_sequences = {}
protein_name = ''
protein_sequence = ''


x = ''


FILE_INPUT = raw_input('enter file name: ')
sequence_file = open(FILE_INPUT)

# opens the newly created output file once the
# python script is executed
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

# get the protein name
def get_protein_name(line):
    return line.lstrip('>').split(':')[0]

# get the TM segment parameters
def get_segments(line):
    segment = []
    for element in line.lstrip('>').split(':')[1].split(';'):
        segment.append([int(element.split('.')[1].split(',')[0]),
                        int(element.split('.')[1].split(',')[1])])
    return segment

# bulk of the command line tool
for line in sequence_file:
    if line.startswith('>'):
        protein_name = get_protein_name(line)
        protein_names_and_segments[protein_name] = get_segments(line)
        protein_names_and_sequences[protein_name] = ''
    else:
        sequence = protein_names_and_sequences.get(protein_name)
        sequence += line.strip('\n' and '\r' and '\r\n')
        protein_names_and_sequences[protein_name] = sequence

for key in protein_names_and_segments.keys():

    for segment in protein_names_and_segments.get(key):

        segment_sequence = protein_names_and_sequences.get(key)[segment[0]
                                                                - 1:segment[1]]
        x += segment_sequence
        y = ProteinAnalysis(str(x))
        z = y.get_amino_acids_percent()


# visual for command line
print 'parsing ' + FILE_INPUT + '\n'

# build the output file as CSV
with open('percent_AA_per_seg_OUTPUT.csv', 'wb') as f:
    w = csv.writer(f)
    w.writerows(z.items())

# opens the ouput file
file = '/Users/simonkeng/senior-research-project/percent_AA_per_seg_OUTPUT.csv'
open_file(file)
