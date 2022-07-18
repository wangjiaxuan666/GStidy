import json
import os

def get_default_info():
    ndict = {
        # RS NUMBER
        'SNP': 'SNP',
        'MARKERNAME': 'SNP',
        'SNPID': 'SNP',
        'RS': 'SNP',
        'RSID': 'SNP',
        'RS_NUMBER': 'SNP',
        'RS_NUMBERS': 'SNP',
        # NUMBER OF STUDIES
        'NSTUDY': 'NSTUDY',
        'N_STUDY': 'NSTUDY',
        'NSTUDIES': 'NSTUDY',
        'N_STUDIES': 'NSTUDY',
        # P-VALUE
        'P': 'P',
        'PVALUE': 'P',
        'P_VALUE': 'P',
        'PVAL': 'P',
        'P_VAL': 'P',
        'GC_PVALUE': 'P',
        # ALLELE 1
        'A1': 'A1',
        'ALLELE1': 'A1',
        'ALLELE_1': 'A1',
        'EFFECT_ALLELE': 'A1',
        'REFERENCE_ALLELE': 'A1',
        'INC_ALLELE': 'A1',
        'EA': 'A1',
        # ALLELE 2
        'A2': 'A2',
        'ALLELE2': 'A2',
        'ALLELE_2': 'A2',
        'OTHER_ALLELE': 'A2',
        'NON_EFFECT_ALLELE': 'A2',
        'DEC_ALLELE': 'A2',
        'NEA': 'A2',
        # N
        'N': 'N',
        'NCASE': 'N_CAS',
        'CASES_N': 'N_CAS',
        'N_CASE': 'N_CAS',
        'N_CASES': 'N_CAS',
        'N_CONTROLS': 'N_CON',
        'N_CAS': 'N_CAS',
        'N_CON': 'N_CON',
        'N_CASE': 'N_CAS',
        'NCONTROL': 'N_CON',
        'CONTROLS_N': 'N_CON',
        'N_CONTROL': 'N_CON',
        'WEIGHT': 'N',  # metal does this. possibly risky.
        # SIGNED STATISTICS
        'ZSCORE': 'Z',
        'Z-SCORE': 'Z',
        'GC_ZSCORE': 'Z',
        'Z': 'Z',
        'OR': 'OR',
        'B': 'BETA',
        'BETA': 'BETA',
        'LOG_ODDS': 'LOG_ODDS',
        'EFFECTS': 'BETA',
        'EFFECT': 'BETA',
        'SIGNED_SUMSTAT': 'SIGNED_SUMSTAT',
        # standard errors
        'SE': 'SE',
        'STANDARD ERRORS': 'SE',
        # INFO
        'INFO': 'INFO',
        # MAF
        'EAF': 'FRQ',
        'FRQ': 'FRQ',
        'MAF': 'FRQ',
        'FRQ_U': 'FRQ',
        'F_U': 'FRQ',
        # phenotype
        'PHENOTYPE': 'PHENOTYPE',
        "PHENO": 'PHENOTYPE',
    }

    describe_ndict = {
        'SNP': 'Variant ID (e.g., rs number)',
        'P': 'p-Value',
        'A1': 'Allele 1, interpreted as ref allele for signed sumstat.',
        'A2': 'Allele 2, interpreted as non-ref allele for signed sumstat.',
        'N': 'Sample size',
        'SE': 'standard errors',
        # 'N_CAS': 'Number of cases',
        # 'N_CON': 'Number of controls',
        'Z': 'Z-score (0 --> no effect; above 0 --> A1 is trait/risk increasing)',
        'OR': 'Odds ratio (1 --> no effect; above 1 --> A1 is risk increasing)',
        'BETA': '[linear/logistic] regression coefficient (0 --> no effect; above 0 --> A1 is trait/risk increasing)',
        # 'LOG_ODDS': 'Log odds ratio (0 --> no effect; above 0 --> A1 is risk increasing)',
        'INFO': 'INFO score (imputation quality; higher --> better imputation)',
        'FRQ': 'Allele frequency',
        # 'SIGNED_SUMSTAT': 'Directional summary statistic as specified by --signed-sumstats.',
        # 'NSTUDY': 'Number of studies in which the SNP was genotyped.',
        'PHENOTYPE': 'The disease PHENOTYPE, If you want add ,need -N parameter',
    }
    return ndict, describe_ndict


def get_info(value, type):
    """
    Get the value according to the rsid
    :param value: RSID
    :param type: the snp2chrpos and snp2maf
    :return: the value (snp2maf is maf values; snp2chrpos is chr and bp)
    """
    ref_dir = os.path.join(os.path.dirname(__file__), "../data/")
    #ref_dir = "../data/"
    if type == "snp2chrpos":
        ref_snp = json.load(open(os.path.join(ref_dir,"snp2chrpos.json")))
        return ref_snp.get(value)
    if type == "snp2maf":
        ref_snp = json.load(open(os.path.join(ref_dir,"snp2maf.json")))
        return ref_snp.get(value)
