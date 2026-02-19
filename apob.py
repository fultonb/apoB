#!/usr/bin/env python3
"""
Author : Brad Fulton <fultonbd@gmail.com>
Date   : 2026-02-17
Purpose: Calculation to estimate the plasma concentration of 
         Apolipoprotein B (ApoB) in milligrams per deciliter (mg/dL).
"""

import argparse
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    total_cholesterol: int
    hdlc_cholesterol: int
    triglycerides: int


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Calculates the concentration of Apolipoprotein B (ApoB) in mg/dL.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-tc',
                        '--total_cholesterol',
                        help='Total Cholesterol',
                        metavar='int',
                        type=int,
                        default=166)
    
    parser.add_argument('-hdlc',
                        '--hdlc_cholesterol',
                        help='High-Density Lipoprotein Cholesterol',
                        metavar='int',
                        type=int,
                        default=34)
    
    parser.add_argument('-tg',
                        '--triglycerides',
                        help='Triglycerides',
                        metavar='int',
                        type=int,
                        default=188)

    args = parser.parse_args()

    if args.total_cholesterol <= 0:
        parser.error(f'-tc/--total_cholesterol "{args.total_cholesterol}" must be a positive number greater than 0')

    if args.hdlc_cholesterol <= 0:
        parser.error(f'-hdlc/--hdlc_cholesterol "{args.hdlc_cholesterol}" must be a positive number greater than 0')

    if args.triglycerides <= 0:
        parser.error(f'-tg/--triglycerides "{args.triglycerides}" must be a positive number greater than 0')
    
    
    return Args(args.total_cholesterol, args.hdlc_cholesterol, args.triglycerides)


# --------------------------------------------------
def main() -> None:
    """Run program."""

    args = get_args()
    tc: int = args.total_cholesterol
    hdlc: int = args.hdlc_cholesterol
    tg: int = args.triglycerides

    apob: float = (0.65 * tc)-(0.59 * hdlc)+(0.01 * tg) 

    risk_chart: str = """ 
    * Optimal/Low Risk: < 90 mg/dL (some sources suggest).
    * Borderline/Moderate Risk: 90 - 129 mg/dL.
    * High Risk: >= 130 mg/dL.
    * Very High Risk: > 150 mg/dL. 

    Note:  mg/dL = milligrams per deciliter
    """
    risk: str = ''
    if apob < 90: risk = 'Optimal/Low Risk'
    elif apob < 130: risk = 'Borderline/Moderate Risk'
    elif apob < 150: risk = 'High Risk'
    else: risk = 'Very High Risk'

    print(f"TC: {tc}, HDLC: {hdlc}, TG: {tg}")
    print(f"ApoB = {apob:.2f} mg/dL \t{risk} \n{risk_chart}")



# --------------------------------------------------
if __name__ == '__main__':
    main()
