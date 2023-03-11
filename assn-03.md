I uploaded all fasta files to my storage with
scp *.fasta fhalqhta@hpc-portal2.hpc.uark.edu:/storage/fhalqhta/mt_genomes

after that I uploaded the unknown.fa with
scp unknown.fa fhalqhta@hpc-portal2.hpc.uark.edu:/storage/fhalqhta/mt_genomes

after that, I made the following slurm file

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

and synced all the files to my local storage with this command,
rsync -r fhalqhta@hpc-portal2.hpc.uark.edu:/storage/fhalqhta/mt_genomes /home/faisal/Documents/bio5153/scripts/


>How long did it take your job to complete?
the job toke around three minutes to complete.


>What is the closest match in the database?
from the database, Cucurbita was the closest with 1566 out of 1584 base pair identification. 

>Cucurbita
Length=982833

 Score = 2826 bits (1530),  Expect = 0.0
 Identities = 1566/1584 (99%), Gaps = 0/1584 (0%)
 Strand=Plus/Plus

