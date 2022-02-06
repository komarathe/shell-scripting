
"""
File Name:
    calculate_snp_maf.py

Description:
    This python script calculate minor allele frequency (MAF;
    definition shown in 1a) for each SNP.
    MAF is minimum(reference allele frequency, alternate allele frequency)
    Reference (or Alternate) allele frequency is defined by reference
    (or alternate) allele counts divided by the sum of reference and
    alternate allele counts for
    a given SNP.
    This code will print “SNPname” list and its corresponding MAF.

To execute the code on Command Line Terminal to get output for
both questions 1 and 2:
    python3 ./calculate_snp_maf.py sampleFile.txt 0
Expected output for operation 0:
    Displays SNP names and corresponding MAFs for each SNP,
    and displays file name with total number of SNPs with for which 0.02 <= MAF
    <= 0.3


To execute the code on Command Line Terminal to get output for question 1:
    python3 ./calculate_snp_maf.py sampleFile.txt 1
Expected output for operation 1:
    Displays SNP names and corresponding MAFs for each SNP


To execute the code on Command Line Terminal to get output for question 2:
    python3 ./calculate_snp_maf.py sampleFile.txt 2
Expected output for operation 2:
    Displays file name with total number of SNPs with for which 0.02 <= MAF
    <= 0.3
"""

import argparse


def main():
    """
    Main Logic
    """
    # Get the command line arguments
    args = get_cli_args()
    # Get input file name from command line
    file_path = args.file
    # Get operation number from command line
    operation = args.operation
    # Read SNP input file and collect the information in a list
    snps = read_snp_file(file_path)
    # Calculate the MAF for each SNP and get dictionary containing it
    mafs_dict = calculate_maf(snps)

    if operation == "0":
        # Get SNPnames with their MAF values
        get_snps_with_maf(mafs_dict)
        # Get input SNP file name and specific MAFs (0.02 <= MAF <= 0.3)
        get_filename_snp_ct(mafs_dict, file_path)

    elif operation == "1":
        # Get SNPnames with their MAF values
        get_snps_with_maf(mafs_dict)

    elif operation == "2":
        # Get input SNP file name and specific MAFs (0.02 <= MAF <= 0.3)
        get_filename_snp_ct(mafs_dict, file_path)


def get_cli_args():
    """
    :return: This function returns CLI argument
    """
    parser = argparse.ArgumentParser(description="Calculate MAF of SNPS")
    parser.add_argument("file",
                        help="Provide path to the input SNP text file")
    parser.add_argument("operation",
                        choices=["0", "1", "2"],
                        help="Pass 1 for 'SNPname' list and its corresponding "
                             "MAF OR Pass 2 for filename with count of SNPS "
                             "with 0.02 <= MAF <= 0.3 OR Pass 0 for both 1 "
                             "and 2")
    return parser.parse_args()


def read_snp_file(file_path):
    """
    :param file_path: Name of the input file containing SNP information
    :return: List of dictionaries where each dictionary contains SNPname, its
    ReferenceAlleleCount and AlternateAlleleCount
    """
    with open(file_path, "r") as fin:
        lines = fin.readlines()
        snp_info = lines[1:]
        snps = []
        for i in range(len(snp_info)):
            snp_with_alleles = snp_info[i].strip()
            snp_list = snp_with_alleles.split("\t")
            snp_dict = dict()
            snp_dict["snp_name"] = snp_list[0]
            snp_dict["ref_ct"] = int(snp_list[1])
            snp_dict["alt_ct"] = int(snp_list[2])
            snps.append(snp_dict)
        return snps


def calculate_maf(snps):
    """
    :param snps: List of dictionaries returned by read_snp_file()
    :return: Dictionary containing SNPname as keys and their MAFs as values
    """
    mafs_dict = dict()
    for i in range(len(snps)):
        # Calculate Reference Allele  frequency
        ref_freq = (snps[i]['ref_ct'])/(snps[i]['ref_ct'] + snps[i]['alt_ct'])
        # Calculate Alternate Allele frequency
        alt_freq = (snps[i]['alt_ct'])/(snps[i]['ref_ct'] + snps[i]['alt_ct'])
        # Get the minimum value between Reference Allele and Alternate Allele
        # frequency
        mafs_dict[snps[i]['snp_name']] = min([round(ref_freq, 3),
                                             round(alt_freq, 3)])
    return mafs_dict


def get_specific_snps(mafs_dict):
    """
    :param mafs_dict: SNPs with MAFs dictionaries returned by calculate_maf()
    :return: Count of SNPs where 0.02 <= MAF <= 0.3
    """
    count = 0
    # Access the MAF values of all the SNPs
    for value in mafs_dict.values():
        if (value >= 0.02) and (value <= 0.03):
            count += 1
    return count


def get_snps_with_maf(mafs_dict):
    """
    :param mafs_dict: SNPs with MAFs dictionaries returned by calculate_maf()
    :return: Prints SNPnames and corresponding MAF values
    """
    print('SNPname\tMAF')
    for key, value in mafs_dict.items():
        print(f'{key}\t{value}')


def get_filename_snp_ct(mafs_dict, file_path):
    """
    :param mafs_dict: SNPs with MAFs dictionaries returned by calculate_maf()
    :param file_path: Name of the input file containing SNP information
    :return: Prints SNP input file name and count of SNPs where 0.02 <= MAF
    <= 0.3
    """
    count = get_specific_snps(mafs_dict)
    print(f'{file_path} contains {count} SNPS with 0.02 <= MAF <= 0.3')


if __name__ == "__main__":
    main()
