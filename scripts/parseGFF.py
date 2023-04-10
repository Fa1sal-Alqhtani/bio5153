# set the file name
infile = '~/Documents/example_files/covid_genome/covid.gff3'

# open the file
genome = open(infile, "r")

# print(genome)

# read the file
dna_sequence = genome.read()

# print the contents
print(dna_sequence)

# reading a file line by line

# open file with all the songs on Blood on the Tracks
genome = open('blood_on_the_tracks.txt', "r")

# count the lines
lines_num = 0

# loop over all the lines in the file
for genome in genome:
    lines_num += 1
    track = track.rstrip()
    print(str(genome_num) + ': ' + track)
    # genome_num = genome_num + 1