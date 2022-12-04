from argparse import ArgumentParser
import sys
# Replace this comment with your implementations of the evaluate() and main()
# functions.

def evaluate(line):
    operators = ['+', '-', '*', '/']
    tokenLine = line.strip().split(",")
    operandStack = float(tokenLine(2))
    
    for token in tokenLine:
        if token in operators:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
        
            result = line[token](operand1 , operand2)
            operandStack.append(result)
            return operators.pop()
            
    
def main(postfix_expressions):
    with open("postfix_expressions.txt" , "r" , encoding="utf-8") as f:
        for line in f:
            evaluate(line)
def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing reverse polish notation")
    args = parser.parse_args(arglist)
    return args
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)