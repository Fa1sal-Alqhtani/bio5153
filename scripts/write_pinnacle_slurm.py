#! /usr/bin/env python3

# set some variables
job_name = ''<job_name>'
queue = 'comp01'
walltime = 1
num_nodes = 1
num_processors = 24

# print bash header
print('#!/bin/bash')

print()

# print SBATCH commands
print('#SBATCH --job-name= ' + job_name)
print('#SBATCH --partition',  queue)
print('#SBATCH --nodes=' + str(num_nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=' + )
print('#SBATCH --time=72:00:00')
print('#SBATCH -o unknown.out')
print('#SBATCH -e unknown.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=fhalqhta@uark.edu')

cd $SLURM_SUBMIT_DIR

#job command here

