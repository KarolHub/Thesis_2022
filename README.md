# Thesis_2022
This repository contains all the scripts and data used during the bioinformatic part of the phorid flies analysis workflow.

Final_Data_Table.xlsx               contains the final dataset with 1462 phorid flies

sample_info.txt                     contains the collection site information, provided by the team responsible for insect sampling

COI_OTU_Table.txt                   table containing the COI "species" assignment
COI_zotu_table_expanded.txt         table containing the COI "genotypes" assignment
Decontaminated_16SV4_OTU_Table.txt  table containing the 16S-V4 OTU assignment of bacteria

score_NovaSeq.py                    custom Python script used for splitting the data between 16S-V4 and COI files
LSD.py                              custom Python script responsible for
MAO.py                              custom Python script containing basic tools for COI data management
QUACK_symbiont_exclude.py           custom Python script for decontamination and calculation of data for the quantification steps

add_seq_to_zotu.py                  supplementary Python script for the old version of the LSD.py script
combine_zOTU_files.py               supplementary Python script for the old version of the LSD.py script


Statistics_table.txt                this table contains the ratios of extraction spike-ins, used during the quantification step 
list_of_blanks.txt                  list of negative samples needed for the decontamination - QUACK.py script
list_of_spikeins.txt                list of used spike-ins needed for the decontamination - QUACK.py script
otus.tax                            list of taxonomic assignments for bacterial OTUs for the decontamination - QUACK.py script
