"""Perform fixed-rate mortgage calculations."""

from argparse import ArgumentParser
import math
import sys

"""This function sets up the parameters that are used 
to compute the minimum mortgage payment. """

def get_min_payment(P , ANI = "0 , 1" , M = 30 , PPY = 12):
    r = ANI // PPY
    n = M * PPY
    #Functionality formula
    A = P * r * 1 + r **n // 1 + r **n - 1
    math.ceil(A)
    return A
print(f"{get_min_payment} is your minimum mortgage payment")

"""This function computes the amount of 
intrest due in the next mortgage payment."""
def interest_due(b  , ANR = "0, 1" , PPY = 12):
    r = ANR // PPY
    i = b * r
    return interest_due
print(f"{interest_due} is the amount of intrest due in the next payment")
    
"""This function is used to compute the remaining payments needed to pay 
for the mortgage to be paid."""
def remaining_payments(b , ANR = "0 , 1" , PPY = 12 ):
    counter = {0}
    if b > 0:
        interest_due()
        print(f" You have {interest_due} left to pay.")
"""This function is to show how much of the mortgage will be paid when a user 
puts a unique set of numbers."""
def main(P , ANI = "0 , 1" , MY = 30 , PPY = 12 , TP = None):
    print(get_min_payment)
    if TP < 0:
        print("Your payment is less than the minimum payment for this mortgage.")
        
def parse_args(arglist):
    """Parse and validate command-line arguments.
    
    This function expects the following required arguments, in this order:
    
        mortgage_amount (float): total amount of a mortgage
        annual_interest_rate (float): the annual interest rate as a value
            between 0 and 1 (e.g., 0.035 == 3.5%)
        
    This function also allows the following optional arguments:
    
        -y / --years (int): the term of the mortgage in years (default is 30)
        -n / --num_annual_payments (int): the number of annual payments
            (default is 12)
        -p / --target_payment (float): the amount the user wants to pay per
            payment (default is the minimum payment)
    
    Args:
        arglist (list of str): list of command-line arguments.
    
    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)
    
    Raises:
        ValueError: encountered an invalid argument.
    """
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                             " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                        " (default: the minimum payment)")
    # parse and validate arguments
    args = parser.parse_args()
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")
    
    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
         args.num_annual_payments, args.target_payment)
