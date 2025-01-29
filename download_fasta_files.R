# Load required libraries
library(rentrez)
library(Biostrings)

# Accession numbers
accession_numbers <- c("NM_000014.6", "NM_000015.4", "NM_000016.6")  # Example accession numbers

# Function to download and write sequences to a file
download_sequences <- function(accession_numbers, output_file) {
  # Fetch sequences from GenBank
  sequences <- entrez_fetch(db = "nucleotide", id = accession_numbers, rettype = "fasta", retmode = "text")
  
  # Write sequences to a file
  write(sequences, file = output_file)
}

# Specify output file
output_file <- "all_sequences.fasta"

# Download and write sequences to a file
download_sequences(accession_numbers, output_file)
