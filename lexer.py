import utils

class Lexer:
    def __init__(self, expression: str):
        self.expression = expression.replace(' ', '')
        self.output = []

    def tokenize(self):
        amountOfTokens = len(self.expression)

        currentToken = None
        previousToken = None

        for index in range(amountOfTokens):
            currentToken = self.expression[index]

            if index > 0 and index <= (amountOfTokens - 1):
                previousToken = self.expression[index - 1]
            
            if utils.Utils.isNumber(currentToken):
                if previousToken and utils.Utils.isNumber(previousToken):
                    self.output[-1] += currentToken
                else:
                    self.output.append(currentToken)

            if utils.Utils.isLetter(currentToken):
                if previousToken and utils.Utils.isLetter(previousToken):
                    self.output[-1] += currentToken
                else:
                    self.output.append(currentToken)

            if utils.Utils.isOperator(currentToken):
                self.output.append(currentToken)

            if utils.Utils.isDecimalPoint(currentToken):
                self.output[-1] += currentToken
                
        return self.output