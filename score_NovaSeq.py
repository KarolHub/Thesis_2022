#! /usr/bin/env python3

import sys, os

SAMPLE_LIST = open("sample.list", "r")
path_to_input = "/mnt/matrix/symbio/raw_data/20210120_NovaSeq_Batch01/renamed/"

os.system('echo "libname	16S-V4  COI-BF3BR2    Unclassified" > all_libs.info')
lib_count = 0

for line in SAMPLE_LIST:
    lib_count += 1
    os.system('echo "Processing library no. %s ... \n"' % lib_count)
    LINE = line.strip().split()
    Libname = LINE[0]
    R1 = path_to_input + LINE[1]
    R2 = path_to_input + LINE[2]
    
    ### Copying and unzipping files
    os.system("cp %s ." % R1)
    os.system("cp %s ." % R2)
    os.system("gunzip ./*gz")
    
    ### Running split_amplicon_libs.py, copying info
    os.system("echo %s %s %s > sample_list.txt" % (Libname, LINE[1][:-3], LINE[2][:-3]))
    os.system("split_amplicon_libs.py ~/phorid1800/my_primers.txt sample_list.txt ./NOVASEQ")
    os.system("tail -1 NOVASEQ/000_splitting_summary.txt >> all_libs.info")
    
    ### Searching for four quant plasmids
    
    """
    os.system("search_for_spikeins.py NOVASEQ/16S-V4/ /mnt/matrix/symbio/db/references/standard_spikein_plasmids.fasta .")
    os.system("tail -1 000_search_summary.txt >> all_plasmid.info")    
    os.system("search_for_spikeins.py NOVASEQ/16S-V1V2/ /mnt/matrix/symbio/db/references/standard_spikein_plasmids.fasta .")
    os.system("tail -1 000_search_summary.txt >> all_plasmid.info")    
    os.system("search_for_spikeins.py NOVASEQ/ITS1a/ /mnt/matrix/symbio/db/references/standard_spikein_plasmids.fasta .")
    os.system("tail -1 000_search_summary.txt >> all_plasmid.info")    
    os.system("search_for_spikeins.py NOVASEQ/ITS2/ /mnt/matrix/symbio/db/references/standard_spikein_plasmids.fasta .")
    os.system("tail -1 000_search_summary.txt >> all_plasmid.info")    
    """

    ### Cleaning up!
    os.system("chmod 777 *fastq")
    os.system("rm *fastq")
    os.system("rm sample_list.txt")    
    
    
