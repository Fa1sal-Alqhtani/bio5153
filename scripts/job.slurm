#!/bin/bash

#SBATCH --job-name=<insert job name>
#SBATCH --partition comp72
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --time=72:00:00
#SBATCH -o unknown.out
#SBATCH -e unknown.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=fhalqhta@uark.edu

cd $SLURM_SUBMIT_DIR

# Purge modules and load blast module
module purge
module load blast

# Concatenate all genomes into a single file called genomes.fas
cat *.fasta > genomes.fas

# Create blast database
makeblastdb -in genomes.fas -dbtype nucl

# Run blastn search
blastn -query unknown.fa -db genomes.fas > unknown.vs.genomes.blastn
