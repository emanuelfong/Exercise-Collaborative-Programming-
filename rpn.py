from argparse import ArgumentParser
import sys


def evaluate(expression):
    """Evaluate a postfix expression.
    
    Args:
        expression (str): a postfix expression.
    
    Returns:
        float: the result of the expression.
    """
    stack = []
    for token in expression.split(" "):
        try:
            stack.append(float(token))
        except ValueError:
            num2 = stack.pop()
            num1 = stack.pop()
            if token == "+":
                value = num1+num2
            elif token == "-":
                value = num1-num2
            elif token == "*":
                value = num1*num2
            else:
                value = num1/num2
            stack.append(value)
    return stack.pop()


def main(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            expression = line.strip()
            print(f"{expression} = {evaluate(expression)}")


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
