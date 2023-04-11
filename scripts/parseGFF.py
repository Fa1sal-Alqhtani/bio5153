#! /usr/bin/env python3

# import modules
import argparse

#create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script parses a GFF file")

# add positional (required) arguments
parser.add_argument("gff", help="Name of the GFF file to parse", type=str)
parser.add_argument("fasta", help="Name of the FASTA file to parse", type=str)

# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args()

# open the GFF file
with open(args.gff) as gff_file:

    # loop over all the lines in the file
    for line in gff_file:

        # remove the newline character from each line
        line = line.rstrip()

        # separate each line into individual columns
        columns = line.split("\t")

        # calculate and print the feature type and its length, separated by a tab character
        feature_type = columns[2]
        feature_length = int(columns[4]) - int(columns[3]) + 1
        print(f"{feature_type}\t{feature_length}")