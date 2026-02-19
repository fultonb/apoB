import argparse
from typing import NamedTuple


"""
Calcualates your ApoB score (mg/dL) using:
1. Total chloesterol
2. HDL cholesteral
3. Tryglicerides

The following YouTube video inspired this program:
        https://www.youtube.com/watch?v=RQdL3e0cBlI

"""

class Args(NamedTuple):
    """Command-line arguments"""
    total_cholesterol: int
    hdl_cholesterol: int
    triglycerides: int


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="ApoB Calculator",
        epilog="""
        The following YouTube video inspired this program:
        https://www.youtube.com/watch?v=RQdL3e0cBlI
        """,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("-tc", "--total_cholesterol", help="total cholesterol (mg/dL)",
                            metavar="int", type=int, default=166)
    parser.add_argument("-hdl", "--hdl_cholesterol", help="hdl cholesterol (mg/dL)",
                            metavar="int", type=int, default=34)
    parser.add_argument("-tri", "--triglycerides", help="triglycerides (mg/dL)",
                            metavar="int", type=int, default=188)

    args = parser.parse_args()
    if args.total_cholesterol <= 0:
        parser.error(f'--total_cholesterol "{args.total_cholesterol}" must be a positive number greater than 0')
    if args.hdl_cholesterol <= 0:
        parser.error(f'--hdl_cholesterol "{args.hdl_cholesterol}" must be a positive number greater than 0')
    if args.triglycerides <= 0:
        parser.error(f'--triglycerides "{args.triglycerides}" must be a positive number greater than 0')

    return Args(
        args.total_cholesterol,
        args.hdl_cholesterol,
        args.triglycerides
    )


# --------------------------------------------------
def main() -> float:
    """Run program."""
    args = get_args()
    tc = args.total_cholesterol
    hdl = args.hdl_cholesterol
    tg = args.triglycerides

    ApoB = 0.65 * tc - 0.59 * hdl + 0.01 * tg
    print(f"Your ApoB is {ApoB} mg/dL")
    print("""
ApoB levels:
    * Optimal: <80
    * Moderate Risk: 80-99
    * High Risk: ≥100 (or >110) 
          """)

    return ApoB

if __name__ == "__main__":
    main()
