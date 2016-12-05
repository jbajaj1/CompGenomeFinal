
from Bio import SeqIO

for seq_record in SeqIO.parse('chr10.fa', 'fasta'):
    print(seq_record.id)
    print(seq_record.seq)
