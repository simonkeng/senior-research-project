import collections
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import csv


all_aas = collections.defaultdict(int)


for rec in SeqIO.parse("BetaBarrelTrimericSeq.txt", "fasta"):
    x = ProteinAnalysis(str(rec.seq))
    y = x.get_amino_acids_percent()


with open('mycsvfile.csv', 'wb') as f:
    w = csv.writer(f)
    w.writerows(y.items())
