# Senior Research Project

Senior research project for CHEM 499 and CHEM 399. Research students include Simon Keng and Bin Tu, working under the principal investigator Sajith Jayasinghe, Ph.D. from the department of chemistry and biochemistry at California State University San Marcos. 

## Abstract

To compare the difference in hydrophobicity and amphipathicity of various alpha helical and beta barrel transmembrane proteins, 46 proteins were analyzed using several protein databases and bioinformatics software such as VMD(1) and MPEx(4). Using FASTA files from MPtopo(2), two command line tools were developed in Python for parsing and running calculations on each proteins transmembrane segment (TMS), for each protein in the file. The output file was processed and analyzed in Excel and a plot was built comparing the hydrophobicity and hydrophobic moment (amphipathicity) of each category of protein. Analysis of each segment was individually carried out using lipid tail contact PDB files from the MemProtMD(3) database, and analyzed in VMD. We found contradictory data for TMSs of certain alpha helical segments that suggests that there is a difference between the likely hood of segments being inserted into the inner membrane by the translocon, between alpha helices and beta barrels. Partitioning hydrogen bonded peptide bonds is much less energetically costly than partitioning peptide bonds without hydrogen bonds, and alpha helices have intra-strand hydrogen bonding in their peptide bonds while beta strand peptide bonds do not(9). Because of this, we expect the cost of partitioning a non-hydrogen bonded peptide bond to be the primary hindrance the translocon experiences when inserting a beta-strand TMS into the inner membrane.

### References

1.	Visual Molecular Dynamics, http://www.ks.uiuc.edu/Research/vmd/
2.	Jayasinghe et al. (2001) Protein Sci. 10:455-458. MPtopo, membrane protein topology database, Stephen White at UCI. http://blanco.biomol.uci.edu/mptopo/
3.	Phillip J. Stansfeld, Joseph E. Goose, Martin Caffrey, Elisabeth P. Carpenter, Joanne L. Parker, Simon Newstead, Mark S.P. Sansom. Structure Volume 23, Issue 7, 7 July 2015, Pages 1350–1361. http://sbcb.bioch.ox.ac.uk/memprotmd/beta/
4.	Snider C, Jayasinghe S, Hristova K, & White SH (2009). MPEx: A tool for exploring membrane proteins. Protein Sci 18:2624-2628. http://blanco.biomol.uci.edu/mpex/
5.	Moran, L.A., Horton, H.R., Scrimgeour, K.G., Perry, M.D.,Principles of Biochemistry, fifth edition, 2012.  
6.	RCSB Protein Data Bank, D.W. Heinz, W.A. Baase, F.W. Dahlquist, B.W. Matthews (1993) How Amino-Acid Insertions are Allowed in an Alpha-Helix of T4 Lysozyme Nature 361:561. An Information Portal to Biological Macromolecular Structure.
7.	My GitHub repository for this project: https://github.com/simonkeng/senior-research-project
8.	Wolfenden, Richard. Experimental Measures of Amino Acid Hydrophobicity and the Topology of Transmembrane and Globular Proteins, J Gen Physiology, 129(5): 357-362, 2007. 
9.	Keng, S., Tu, B., Poyrazoglu, H., Kadevari, P., Jayasinghe, S., Comparing the Hydrophobicity and Amphipathicity of Transmembrane Segments of Bacterial Outer-membrane and Inner-membrane Proteins, 2016.







