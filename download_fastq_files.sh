#!/usr/bin/env bash

# Define variables
base_endpoint="ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR174/"

fastq_file_names=(
    "057/SRR17406457/SRR17406457"
    "058/SRR17406458/SRR17406458"
    "059/SRR17406459/SRR17406459"
    "060/SRR17406460/SRR17406460"
    "061/SRR17406461/SRR17406461"
    "062/SRR17406462/SRR17406462"
    "063/SRR17406463/SRR17406463"
    "064/SRR17406464/SRR17406464"
    "065/SRR17406465/SRR17406465"
    "066/SRR17406466/SRR17406466"
    "067/SRR17406467/SRR17406467"
    "068/SRR17406468/SRR17406468"
)

data_dir="data"

for fastq_file in ${fastq_file_names[@]}; do
  echo "Downloading ${fastq_file}_1..."
  echo wget -q -P ${data_dir} ${base_endpoint}${fastq_file}_1.fastq.gz
  echo "Downloading ${fastq_file}_2..."
  echo wget -q -P ${data_dir} ${base_endpoint}${fastq_file}_2.fastq.gz
  echo "---------- Download completed! ----------"
  echo ""
done

echo "All fastq files have been downloaded. Please check ${data_dir} directory."
