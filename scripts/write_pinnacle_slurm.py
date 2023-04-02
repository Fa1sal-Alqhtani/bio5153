#! /usr/bin/env python3

# set some variables
job_name = 'MlrA'
queue = 'comp01'
walltime = 1
num_nodes = 1
num_processors = 24

# print bash header
print('#!/bin/bash')

print()

# print SBATCH commands
print('#SBATCH --job-name=' + job_name)
print('#SBATCH --partition', queue)
print('#SBATCH --nodes=' + str(num_nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=' + str(num_processors))
print('#SBATCH --time=' + str(walltime) + ':00:00')
print('#SBATCH -o aja_%j.out')
print('#SBATCH -e aja_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=fhalqhta@uark.edu')

print()

# purge all the modules
print('module purge')

import argparse
from pickle import EXT1
import sys

# create an ArgumentParser object
parser = argparse.ArgumentParser(description='Submit a job to Pinnacle cluster using SLURM')

# add positional argument for job name
parser.add_argument('job_name', type=str, help='Name of the job')

# add optional arguments for queue, number of nodes, number of processors, and walltime
parser.add_argument('--queue', type=str, default='comp01', help='Queue name')
parser.add_argument('--nodes', type=int, default=1, help='Number of nodes')
parser.add_argument('--procs', type=int, default=24, help='Number of processors per node')
parser.add_argument('--walltime', type=int, default=1, help='Walltime in hours')

# parse the command-line arguments
try:
    args = parser.parse_args()
except SystemExit as e:
    print("Error parsing command-line arguments:", e)
    sys.exit(1)

# assign the parsed arguments to variables
job_name = args.job_name
queue = args.queue
num_nodes = args.nodes
num_processors = args.procs
walltime = args.walltime

# cd into the submit directory
print('cd $SLURM_SUBMIT_DIR')

print()

print('# job command here')

