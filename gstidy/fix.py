import math
import sys

import numpy as np
from scipy.special import chdtri
from scipy.stats import norm

from .check import check_header, clean_header
from .info import get_info


def fix_table(data):
    check_result = check_header(data)
    # caculate the se
    if "SE" in check_result[1]:
        if "BETA" in check_result[0] and 'P' in check_result[0]:
            data['SE'] = data.apply(lambda row: math.sqrt(((row.BETA) ** 2) / chdtri(1, row.P)), axis=1)
        elif "OR" in check_result[0] and 'P' in check_result[0]:
            data['SE'] = data.apply(lambda row: abs(np.log(row.OR) / norm.ppf((row.P) / 2)), axis=1)
    # caculate the OR
    if "OR" in check_result[1]:
        if "BETA" in check_result[0]:
            data['OR'] = data.apply(lambda row: np.exp(row.BETA), axis=1)
        else:
            sys.exit("Please check the download link , the file never have OR and BETA")
    # caculate the BETA
    if "BETA" in check_result[1]:
        if "OR" in check_result[0]:
            data['BETA'] = data.apply(lambda row: np.log(row.OR), axis=1)
        else:
            sys.exit("Please check the download link , the file never have OR and BETA")
    # caculate the Z-scores
    if "Z" in check_result[1]:
        data['Z'] = data.apply(lambda row: row.BETA / row.SE, axis=1)
    data_header = [clean_header(x) for x in data.columns]
    if "SNP" in check_result[0]:
        if "CHR" not in data_header:
            data['CHR'] = data.apply(
                lambda row: "chr" + str(get_info(row[check_result[2].get("SNP")], "snp2chrpos").split(":")[0]), axis=1)
        if "BP" not in data_header:
            data["BP"] = data.apply(lambda row: get_info(row[check_result[2].get("SNP")], "snp2chrpos").split(":")[1],
                                    axis=1)
        if "FRQ" in check_result[1]:
            data['MAF'] = data.apply(lambda row: get_info(row[check_result[2].get("SNP")], "snp2maf"), axis=1)
    else:
        data.to_csv("test.tsv", sep="\t", index=False)
        # sys.exit("Not have chr or base in data, please use parameter --chr and --bp")
        sys.exit("NO REID,please use script to get the info")
    return data
