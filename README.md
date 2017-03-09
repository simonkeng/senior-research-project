![Translocon](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/OST_PM-1.jpg/220px-OST_PM-1.jpg)

# Undergraduate Bioinformatics Research

This repository contains the command line tools I built for my undergraduate research in CHEM 399 & 499 at California State University San Marcos, in the department of chemistry and biochemistry, May 2016 – April 2017.


### Abstract

To compare the difference in hydrophobicity and amphipathicity of various alpha helical and beta barrel transmembrane proteins, 46 proteins were analyzed using the transmembrane protein databases [MemProtMD](http://sbcb.bioch.ox.ac.uk/memprotmd/beta/) and [MPtopo](http://blanco.biomol.uci.edu/mptopo/) with bioinformatics tools such as [VMD](http://www.ks.uiuc.edu/Research/vmd/) and [MPEx](http://blanco.biomol.uci.edu/mpex/). Using FASTA files from MPtopo, several command line tools were developed in Python for parsing and running calculations on each proteins transmembrane segment (TMS), for each protein in the file. The output file was processed and analyzed in Excel and a plot was built comparing the hydrophobicity and hydrophobic moment (amphipathicity) of each category of protein. Analysis of each segment was individually carried out using lipid tail contact PDB files from the MemProtMD database, and analyzed in VMD. We found contradictory data for TMSs of certain alpha helical segments that suggests that there is a difference between the likely hood of segments being inserted into the inner membrane by the translocon, between alpha helices and beta barrels. Partitioning hydrogen bonded peptide bonds is much less energetically costly than partitioning peptide bonds without hydrogen bonds, and alpha helices have intra-strand hydrogen bonding in their peptide bonds while beta strand peptide bonds do not. Because of this, we expect the cost of partitioning a non-hydrogen bonded peptide bond to be the primary hindrance the translocon experiences when inserting a beta-strand TMS into the inner membrane.


### Story about this repo

`protein_parser.py`
`TMS_parser.py`

Initially these python scripts were written to exercise programming practice, from a "starting from scratch" approach, as to learn the Python programming language, learn to script small command line tools, and eventually write a tool for parsing FASTA files. Once this was acheived, our research progressed in Microsoft Excel and we pursued VMD and other bioinformatics related tools for the rest of our research. There were several instances where our python tools needed to be revised and improved, but overall these scripts were built for one purpose, and not revisted unless there were analysis errors.

That was until we decided to investigate using a [helical propensity scale](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2249854/) for our analysis. I implemented the new helicity scale into our previous script, replacing the [hydrophobicity scale](http://blanco.biomol.uci.edu/hydrophobicity_scales.html) with this one, but we noticed erroneous output and inconsistent data from this method (`helicity_parser.py`). At this time I had enough python scripting experience to realize that the utilization of bioinformatics python libraries would significantly accelerate and improve our research. After experiencing the "from scratch" approach, I was eager to use existing libraries that were designed for FASTA parsing and protein analysis. Hello [ProteinAnalysis](http://biopython.org/DIST/docs/api/Bio.SeqUtils.ProtParam.ProteinAnalysis-class.html), [SeqIO](http://biopython.org/wiki/SeqIO), and all of [Biopython](http://biopython.org/wiki/Biopython) and its glory. 


### Currently

`percent_AA_parser.py` 
`percent_AA_per_seg_parser.py` 

Using the biopython library, several new command line tools were built for analyzing the amino acid composition of our datasets. `TMS_parser.py` and `percent_AA_per_seg_parser.py` are the tried and true, refined, successfully working and effective tools that were used for the bulk of our research. 

### Instructions for running percent_AA_per_seg_parser.py

This command line tool will parse through a FASTA file with this format:

```
>1I78:A.10,21; B.49,61; C.64,73; D.109,119; E.126,137; F.177,189; G.192,203; H.230,241; I.244,255; J.285,297
STETLSFTPDNINADISLGTLSGKTKERVYLAEEGGRKVSQLDWKF
NNAAIIKGAINWDLMPQISIGAAGWTTLGSRGGNMVDQDWMDSSNP
GTWTDESRHPDTQLNYANEFDLNIKGWLLNEPNYRLGLMAGYQESR
YSFTARGGSYIYSSEEGFRDDIGSFPNGERAIGYKQRFKMPYIGLT
GSYRYEDFELGGTFKYSGWVESSDNDEHYDPGKRITYRSKVKDQNY
YSVAVNAGYYVTPNAKVYVEGAWNRVTNKKGNTSLYDHNNNTSDYS
KNGAGIENYNFITTAGLKYTF

```

Where the numbers between the commas are the transmembrane segment parameters. `percent_AA_per_seg_parser.py` will calculate the percent of each amino acid, per segment, for all the proteins in a given input file.

Note: there can be more than one protein in each file, like mine, see `BetaBarrelTrimericSeq.txt`

1. Clone this repository.
2. Open Terminal, `cd` into the directory where `percent_AA_per_seg_parser.py` is.
3. Type `python percent_AA_per_seg_parser.py` and click enter.
4. Enter the file you wish to parse, when prompted, then press enter.
5. The CSV ouput will open automatically in your native application, for most thats Microsoft Excel.

This tool was built for macOS but should work on Windows and Linux as well. Be sure to have Python and Biopython installed on your machine. 


For any questions, please contact me via [LinkedIn](https://www.linkedin.com/in/simonkeng). Thanks for visiting! 
