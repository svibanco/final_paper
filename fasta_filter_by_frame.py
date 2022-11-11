import argparse
import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


parser = argparse.ArgumentParser(description='Aim this program is filter sequence from fasta by info on id.')
parser.add_argument("-i", help="fasta input file", required=True)
parser.add_argument("-out", help="output file e.g: my-output-file.fasta", default="output.fna")

args = parser.parse_args()
input_file = args.i

POS_START = 0
POS_END = 2
BLANK_SPACE = " "
DEFAULT_FRAME = 2


between_square_brackets_recognition_pattern = '(?<=\[)(.*?)(?=\])'
recognizer_pattern = re.compile(between_square_brackets_recognition_pattern)


print("Reading fasta file ...")
sequences = []
for record in SeqIO.parse(input_file, "fasta"):
    desc = record.description
    start = int(recognizer_pattern.search(desc).group().split(BLANK_SPACE)[POS_START])
    # end = int(recognizer_pattern.search(s).group().split(BLANK_SPACE)[POS_END])
    if start == DEFAULT_FRAME:
        sequences.append(
            SeqRecord(
            Seq(record.seq),
            id=record.id,
            name=record.name,
            description=record.description
            )
        )


print("writing fasta file ...")

with open('{out_f_name}'.format(out_f_name=args.out), "w") as output_handle:
    SeqIO.write(sequences, output_handle, "fasta")

print('finished')
