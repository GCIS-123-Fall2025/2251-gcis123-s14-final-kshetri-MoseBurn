
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""


def balance_parenthesis(a_string):
    
    openBracket = 0
    closedBracket = 0
    for i in a_string:
        if i == ")":
            closedBracket += 1
        if i == "(":
            openBracket += 1
    
    if closedBracket > openBracket:
        return -1
    if closedBracket == openBracket:
        return 0
    if closedBracket < openBracket:
        return  2


def main():
    assert balance_parenthesis("__(---(------)--") == 2
    assert balance_parenthesis("()----)") == -1
    assert balance_parenthesis("-----()--(())") == 0

if __name__ == "__main__":    main()
