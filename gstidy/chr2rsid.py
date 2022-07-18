import argparse

parser = argparse.ArgumentParser(
    description="The change the chr pos to rs id, Notice the the snp pos in chr must be first column  like '1:374747'")

parser.add_argument('--ref_file', '-r',
                    help="the file including the snp pos(1 column) and rsid(2 column), this parameter have default value")
parser.add_argument('--input_file', '-i',
                    help="the file need to change the pos to rsid ,the first column must be chr:pos")
parser.add_argument('--output_file', "-o", help="The output file name")

args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file
ref_file = args.ref_file

# input_file = "/jdfssz1/ST_HEALTH/P21Z10200N0092/wangjiaxuan/workflow/GWAS/snpid/data/test.csv"
# output_file = "./test.tsv"
# ref_file = "/jdfssz1/ST_HEALTH/P21Z10200N0092/wangjiaxuan/workflow/GWAS/snpid/refer/snp151.ref"

if ref_file == None:
    ref_file = "/public1/home/sc94571/wangjiaxuan/chrpos2rsid/snp_db/ref_rsid_db"

snps = {e[0]: e[1] for e in (l.strip().split() for l in open(ref_file))}
bim = (l.strip().split() for l in open(input_file))
new = open(output_file, 'w')
with open(input_file) as f:
    first = f.readline()
new.write(first)
for e in bim:
    e[0] = snps.get(e[0])
    if e[0] is not None:
        new.write('\t'.join(e) + '\n')
new.close()
bim.close()
