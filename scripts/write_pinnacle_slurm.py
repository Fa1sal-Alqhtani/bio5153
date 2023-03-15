#!/bin/bash

#SBATCH --job-name=python_script
#SBATCH --partition comp72
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --time=72:00:00
#SBATCH -o unknown.out
#SBATCH -e unknown.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=fhalqhta@uark.edu

cd $SLURM_SUBMIT_DIR

#job command here

