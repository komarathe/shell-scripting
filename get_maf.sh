#!/usr/bin/env bash

# Use this shell script to get my solution to Question 1 and 2

# Example to execute this script on command line terminal given that
# sample file sampleFile.txt, python script calculate_snp_maf.py and
# this shell script calculate_snp_maf.sh are in the same directory:
# ./calculate_snp_maf.sh sampleFile.txt 2

# Variable to store SNP file
snp_input_file=$1
# Variable to store the specific number assigned to the type of desired operation
operation=$2

python3 calculate_snp_maf.py $snp_input_file $operation
