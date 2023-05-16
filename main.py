import math

class Check:
    def isComma(token):
        final = token == ','

        return final

    def isDigit(token):
        final = token.replace('.', '').replace('-', '').isdigit()

        return final
    
    def isDecimalPoint(token):
        final = token == '.'

        return final
    
    def isEqualPrecedence(initial, token):
        final = Data.operators[initial] == Data.operators[token]

        return final
    
    def isFunction(token):
        final = token == ' '

        return final
    
    def isGreaterPrecedence(initial, token):
        final = Data.operators[initial] > Data.operators[token]

        return final
    
    def isLeftAssociative(token):
        final = Data.associative[token] == 'Left'

        return final

    def isLeftParenthesis(token):
        final = token == '('

        return final
    
    def isOperator(token):
        final = token in Data.operators

        return final

    def isRightParenthesis(token):
        final = token == ')'

        return final

class Data:
    associative = {'+': 'Left', '-': 'Left', '*': 'Left', '/': 'Left', '^': 'Right', ' ': 'Left'}
    functions = {}
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, ' ': 4}

    operatorStack = []
    outputAnswer = []
    outputQueue = []

class Helper:
    def evaluate(x, y, operator):
        try:
            x = float(x)
            y = float(y)
        except:
            return math.inf

        match operator:
            case '+':
                return x + y
            
            case '-':
                return x - y
            
            case '*':
                return x * y
            
            case '/':
                if y == 0:
                    return math.inf
                
                return x / y
            
            case '^':
                return x ** y
class Parser:
    def __init__(self, expression):
        self.expression = expression.replace(' ', '')

    # function: geneartes postfix notation from given expression (also known as the Reverse Polish notation).
    def generatePostfixNotation(self):
        # get the amount of tokens we will be looping through.
        amountOfTokens = len(self.expression)

        # loop through the tokens.
        for index in range(amountOfTokens):
            # get the current token.
            token = self.expression[index]

            # if the token is a comma.
            if Check.isComma(token):
                # makre sure that something has been pushed into the operator stack. make sure the latest item in the operator stack is not a left parenthesis.
                while Data.operatorStack and not Check.isLeftParenthesis(Data.operatorStack[-1]):
                    # pop an operator from the operator stack into the output queue.
                    Data.outputQueue.append(Data.operatorStack.pop())

            # if the token is a number.
            if Check.isDigit(token):
                # make sure that something has been pushed into the output queue. make sure that there was a number or a decimal point previous to our current token.
                if Data.outputQueue and self.expression[index - 1] and (Check.isDigit(self.expression[index - 1]) or Check.isDecimalPoint(self.expression[index - 1])):
                    # joim the latest item in the output queue and the token.
                    Data.outputQueue[-1] += token
                else:
                    # push the number into the output queue.
                    Data.outputQueue.append(token)

            # if the token is a decimal point (punctuation).
            if Check.isDecimalPoint(token):
                # make sure that something has been pushed into the output queue.
                if Data.outputQueue:
                    # join the latest item in the output queue and the token.
                    Data.outputQueue[-1] += token

            # if the token is a function.
            # TODO: identify functions.
            if Check.isFunction(token):
                # push the function into the operator stack.
                Data.operatorStack.append(token)

            # if the token is a left parenthesis.
            if Check.isLeftParenthesis(token):
                # push the left parenthesis into the operator stack.
                Data.operatorStack.append(token)

            # if the token is an operator.
            if Check.isOperator(token):
                # make sure that somthing has been pushed into the operator stack. make sure that the latest item pushed into the operator stack is not a left parenthesis and has a greater precedence of the current token or has equal precedence of the current token and current token is left associative.
                while Data.operatorStack and not Check.isLeftParenthesis(Data.operatorStack[-1]) and (Check.isGreaterPrecedence(Data.operatorStack[-1], token) or (Check.isEqualPrecedence(Data.operatorStack[-1], token) and Check.isLeftAssociative(token))):
                    # pop an operator from the operator stack into the output queue.
                    Data.outputQueue.append(Data.operatorStack.pop())

                # push the operator into the operator stack.
                Data.operatorStack.append(token)

            # if the token is a right parenthesis.
            if Check.isRightParenthesis(token):
                # make sure something has been pushed into the operator stack. make sure that the latest item pushed into the operator stack is not a left parenthesis.
                while Data.operatorStack and not Check.isLeftParenthesis(Data.operatorStack[-1]):
                    # pop an operator from the operator stack into the output queue.
                    Data.outputQueue.append(Data.operatorStack.pop())

                # pop the left parenthesis from the operator stack and discard it.
                Data.operatorStack.pop()

                # make sure something has been pushed into the operator stack. make sure that the latest item pushed into the operator stack is a function.
                if Data.operatorStack and Check.isFunction(Data.operatorStack[-1]):
                    # pop the function from the operator stack into the output queue.
                    Data.outputQueue.append(Data.operatorStack.pop())

        # pop the remaining items from the operator stack into the output queue.
        while Data.operatorStack:
            # make sure that the token on top of the stack is not a parenthesis, otherwise there are mismatched parentheses.
            if not Check.isLeftParenthesis(Data.operatorStack[-1]) and not Check.isRightParenthesis(Data.operatorStack[-1]):
                # pop the operator from operator stack into the output queue.
                Data.outputQueue.append(Data.operatorStack.pop())

    # function: evaluates the postfix notation generated by self.generatePostfixNotation().
    def evaluatePostfixNotation(self):
        # get the amount of tokens we will be looping through.
        amountOfTokens = len(Data.outputQueue)

        # loop through the tokens.
        for index in range(amountOfTokens):
            # get the current token.
            token = Data.outputQueue[index]

            # if our token is a number.
            if Check.isDigit(token):
                # push the number into the answer stack.
                Data.outputAnswer.append(token)

            # if our token is an operator.
            if Check.isOperator(token):
                # evaluate our given expression.
                final = Helper.evaluate(Data.outputAnswer[-2], Data.outputAnswer[-1], token)

                # pop latest item from the answer stack.
                Data.outputAnswer.pop()
                
                # push the evaluated expression into the answer stack.
                Data.outputAnswer[-1] = final
            
        print(Data.outputAnswer[0])

    # function: calls our two previous functions (self.generatePostfixNotation() & self.evaluatePostfixNotation()).
    def finalSolution(self):
        self.generatePostfixNotation()
        self.evaluatePostfixNotation()

Parser('3 + 4 * 2 / (1 - 5) ^ 2 * 3').finalSolution()

# We hate blacks & minorities
# God, Honor, Homeland
# Heil white Evropa
# Heil victory