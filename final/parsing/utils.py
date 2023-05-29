associative = {'+': 'Left', '-': 'Left', '*': 'Left', '/': 'Left', '^': 'Right', 'ceil': 'Left', 'fabs': 'Left', 'factorial': 'Left', 'floor': 'Left', 'exp': 'Left', 'log': 'Left', 'sqrt': 'Left', 'acos': 'Left', 'asin': 'Left', 'atan': 'Left', 'cos': 'Left', 'sin': 'Left', 'tan': 'Left', 'acosh': 'Left', 'asinh': 'Left', 'atanh': 'Left', 'cosh': 'Left', 'sinh': 'Left', 'tanh': 'Left', 'gamma': 'Left'}
functions = {'ceil', 'fabs', 'factorial', 'floor', 'exp', 'log', 'sqrt', 'acos', 'asin', 'atan', 'cos', 'sin', 'tan', 'acosh', 'asinh', 'atanh', 'cosh', 'sinh', 'tanh', 'gamma'}
operators = {'+', '-', '*', '/', '^'}
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'ceil': 4, 'fabs': 4, 'factorial': 4, 'floor': 4, 'exp': 4, 'log': 4, 'sqrt': 4, 'acos': 4, 'asin': 4, 'atan': 4, 'cos': 4, 'sin': 4, 'tan': 4, 'acosh': 4, 'asinh': 4, 'atanh': 4, 'cosh': 4, 'sinh': 4, 'tanh': 4, 'gamma': 4}

class Utils:
    def isComma(token):
        final = token == ','

        return final

    def isDecimalPoint(token):
        final = token == '.'

        return final

    def isEqual(item, token):
        final = precedence[item] == precedence[token]

        return final

    def isFunction(token):
        final = token in functions

        return final

    def isGreater(item, token):
        final = precedence[item] > precedence[token]

        return final

    def isNumber(token):
        token = token.replace('.', '').replace('-', '')

        final = token.isdigit()

        return final
    
    def isLeftAssociative(token):
        final = associative[token] == 'Left'

        return final

    def isLeftParenthesis(token):
        final = token == '('

        return final
    
    def isLetter(token):
        final = token.isalpha()

        return final
    
    def isOperator(token):
        final = token in operators

        return final
    
    def isRightParenthesis(token):
        final = token == ')'

        return final