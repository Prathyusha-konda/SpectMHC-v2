# SpectMHC-v2
=================

This is a set of scripts that together predict MHC ligands and output a fasta file to be used for downstream mass spectrometry based searches.

This is second version of SpectMHC software (version 1: https://github.com/Prathyusha-konda/SpectMHC)

Please cite 
------
MHC-I Ligand Discovery Using Targeted Database Searches of Mass Spectrometry Data: Implications for T-Cell Immunotherapies (https://pubs.acs.org/doi/abs/10.1021/acs.jproteome.6b00971)

Usage 
------
`bash ./spectmhc.sh [-r] [-s] <NetMHC folder> <MHC version> <input fasta> <binding cutoff> <allele> <number_of_split_files>`

Example: `bash ./spectmhc.sh -s /home/prathyusha/NetMHC_4.0_for_Linux/netMHC-4.0 4.0 human_proteins.fasta 2 HLA-A0301 10`

### Required arguments:

position | description
------------------|------------------------------------------------
NetMHC folder | path to NetMHC folder
MHC version   | input the version of netMHC 3.4/4.0/pan
input fasta   | input protein data in fasta format
binding cutoff| cutoff to be used (rank for netmhc 4.0/pan, binding affinity for 3.4)
allele        | MHC allele to predict
number_of_split_files | only works if -s is selected. enter a numeric value, such that every split file has between 1000-2000 sequences
                              
### Optional arguments:
-h -> help

-r -> save raw netmhc output

-s -> split file

Installation instructions and dependencies
--------------

- Clone this repository by running one of the following:
	- `git clone git@github.com:Prathyusha-konda/SpectMHC-v2.git` if you use ssh authentication
	- `git clone https://github.com/Prathyusha-konda/SpectMHC-v2.git` otherwise

- Dependencies
  NetMHC (ligand prediction):
  - NetMHCpan 4.0: http://www.cbs.dtu.dk/services/NetMHCpan/
  - NetMHC 4.0: http://www.cbs.dtu.dk/services/NetMHC-4.0/
  - NetMHC 3.4: http://www.cbs.dtu.dk/services/NetMHC-3.4/
  - Python (helper code): https://www.python.org/download/releases/2.7/


Output
-----
- A targeted database of MHC ligands in fasta format to be used for mass spectrometry searches.

For queries, contact:
------
prathyusha.konda@dal.ca
