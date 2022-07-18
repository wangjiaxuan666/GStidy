"""Main module."""
import pandas as pd
from .fix import fix_table


def gstidy(in_file = "../data/fake_table.GWAS.sumstats.tsv"):
    data = pd.read_csv(in_file,sep="\t")
    return fix_table(data)
if __name__ == "__main__":
    new_data= gstidy()
