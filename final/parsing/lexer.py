from parsing.utils import Utils

class Lexer:
    def __init__(self, expression):
        self.expression = expression.replace(' ', '')
        self.tokens = []

    def tokenize(self):
        amountOfTokens = len(self.expression)

        currentToken = None
        previousToken = None

        for index in range(amountOfTokens):
            currentToken = self.expression[index]

            if index >= 1 and index <= (amountOfTokens - 1):
                previousToken = self.expression[index - 1]

            if Utils.isComma(currentToken) or Utils.isLeftParenthesis(currentToken) or Utils.isOperator(currentToken) or Utils.isRightParenthesis(currentToken):
                self.tokens.append(currentToken)

            if Utils.isDecimalPoint(currentToken):
                if previousToken and Utils.isNumber(previousToken):
                    self.tokens[-1] += currentToken

            if Utils.isNumber(currentToken):
                if previousToken and (Utils.isDecimalPoint(previousToken) or Utils.isNumber(previousToken)):
                    self.tokens[-1] += currentToken
                else:
                    self.tokens.append(currentToken)
            
            if Utils.isLetter(currentToken):
                if previousToken and Utils.isLetter(previousToken):
                    self.tokens[-1] += currentToken
                else:
                    self.tokens.append(currentToken)

        return self.tokens