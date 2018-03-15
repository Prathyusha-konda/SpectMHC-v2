#!/bin/sh
#inputs - netMHC folder, fasta-file, MHC alleles, MHC version, binding Rank cutoff
#-r -> save raw netmhc output
#-f -> final in fasta format
#-s -> split file
#-h -> help

raw_output='no'
fasta_output='no'
split_file='no'

while getopts ":rfhs:" flag; do
case "$flag" in
    r) raw_output='yes'
       ;;
	f) fasta_output='yes'
	   ;;
	s) split_file='yes'
	   ;;
	h) echo ""
	   echo "Usage: bash ./$0 [-r] [-f] [-s] <netMHC folder> <input fasta> <MHC version> <binding Rank cutoff> <allele> <number_of_split_files>"
	   echo ""
     	   echo "    -h -> help"
	   echo "    -r -> save raw netmhc output"
	   echo "    -f -> final in fasta format"
	   echo "    -s -> split file"
	   echo "    netMHC folder -> path to NetMHC folder, ex: "
     	   echo "    MHC version -> input the version of netMHC 3.4/4.0/pan"
	   echo "    input fasta -> input protein data in fasta format, .fa/.fasta" 
     	   echo "    binding Rank cutoff -> cutoff to be used, ex: 2"
     	   echo "    allele -> allele to predict, ex: H2-Kb"
	   echo "    number_of_split_files -> only works if -s is selected. enter a numeric value,\
	   	                        such that every split file has between 1000-2000 sequences"
	   echo ""
	   exit 1
	    ;;
    \?)
       echo "Invalid option: -$OPTARG" >&2
       ;;
  esac
done

shift $((OPTIND-1))

# parameters
if [ "$#" -ne 5 ]; then
  echo "bash ./$0 [-r] [-f] [-s] <netMHC folder> <MHC version> <input fasta> <binding Rank cutoff> <allele> <number_of_split_files>"
  exit 1
fi

path=$1
version=$2
files=$3
cut_off=$4
allele=$5

if [ $version == "3.4" ]; then
	echo "Using NetMHC version 3.4"
	
elif [ $version == "4.0" ]; then
	echo "Using NetMHC version 4.0"
	
elif [ $version == "pan" ]; then
	echo "Using NetMHC version pan"
	
else
	echo "Warning: Unrecognized version. NetMHC version must be 3.4/4.0/pan"
	exit 1
fi

#split files

if [ $to_remove == 1 ]; then
	python split_file.py $files $removal_file
	mv ${name}_odd_genome_sr.bedGraph ${name}_odd_genome_s.bedGraph
	python $norm_program ${name}_odd_genome_s.bedGraph $sizes ${name}_odd_genome_sr_norm.bedGraph
	python $remove_program ${name}_even_genome_s.bedGraph $removal_file ${name}_even_genome_sr.bedGraph
	mv ${name}_even_genome_sr.bedGraph ${name}_even_genome_s.bedGraph
	python $norm_program ${name}_even_genome_s.bedGraph $sizes ${name}_even_genome_sr_norm.bedGraph
	python $norm_program ${name}_input_genome_s.bedGraph $sizes ${name}_input_genome_sr_norm.bedGraph  # no need to remove
else 
	python $norm_program ${name}_odd_genome_s.bedGraph $sizes ${name}_odd_genome_sr_norm.bedGraph
	python $norm_program ${name}_even_genome_s.bedGraph $sizes ${name}_even_genome_sr_norm.bedGraph
	python $norm_program ${name}_input_genome_s.bedGraph $sizes ${name}_input_genome_sr_norm.bedGraph
fi
