#!/usr/bin/env python
import math

protein_names_and_segments = {}
protein_names_and_sequences = {}
protein_name = ''
protein_sequence = ''

# FILE_INPUT is the name of the .txt FASTA file you wish to parse,
# FILE_OUTPUT will be the file name in which the output of this program is
# placed into, once the code is run.
FILE_INPUT = 'BetaBarrelTrimericSeq.txt'
FILE_OUTPUT = 'BetaBarrelTrimericSeqOutput3.txt'
sequence_file = open(FILE_INPUT)
output_file = open(FILE_OUTPUT, 'w')

# hydrophobicity scale: Wimley & White
amino_acid_hydrophobicities = {
	'A': 0.5,
	'C': -0.02,
	'D': 3.64,
	'E': 3.63,
	'F': -1.7,
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
	# print key
	for segment in protein_names_and_segments.get(key):
		# print segment
		segment_sequence = protein_names_and_sequences.get(key)[segment[0] - 1:segment[1]]
		hydrophobicity = 0.0
		xcomp = 0.0
		ycomp = 0.0
		moment = 0.0
		for (index, aminoacid) in enumerate(segment_sequence):
			# debug # print aminoacid
			# debug # print amino_acid_hydrophobicities.get(aminoacid)
			hydrophobicity += amino_acid_hydrophobicities.get(aminoacid)
			xcomp += amino_acid_hydrophobicities.get(aminoacid) * math.cos(100 * index) # for alpha helices use 100
			ycomp += amino_acid_hydrophobicities.get(aminoacid) * math.sin(100 * index) # for beta sheets use 180
			moment = math.sqrt(math.pow(xcomp, 2) + math.pow(ycomp, 2))
		output_file.write(key + '\t' + str(segment[0]) + '\t' + str(segment[1]) + '\t' + segment_sequence + '\t'\
		+ str(hydrophobicity) + '\t' + str(moment) + '\n')
		# print segment_sequence + ':' + str(hydrophobicity) + ':' + str(moment)

sequence_file.close()
output_file.close()
