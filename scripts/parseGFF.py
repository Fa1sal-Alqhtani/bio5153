#! /usr/bin/env python3

# import modules
import argparse
import csv

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

    # create a csv reader object
    reader = csv.reader(gff_file, delimiter='\t')

    # loop over all the lines in the file
    for line in reader:

        # skip blank lines
        if not line:
            continue

        # else it's not a blank line
        else:
            line = line.rstrip()

            # separate each line into individual columns
            columns = line.split("\t")

            # give variable names to the columns
            organism     = columns[0]
            source       = columns[1]
            feature_type = columns[2]
            start        = columns[3]
            end          = columns[4]
            length       = columns[5]
            strand       = columns[6]
            Attributes   = columns[8]

            # add the length to column 5 
            columns[5] = str(int(end) - int(start) + 1)

            new_line = "\t".join(columns)
            print(new_line)