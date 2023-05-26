import lexer
import utils

class Parser:
    def __init__(self, expression):
        self.outputQueue = []
        self.operatorStack = []
        self.tokens = lexer.Lexer(expression).tokenize()

    def generatePostfixNotation(self):
        amountOfTokens = len(self.tokens)

        currentToken = None

        for index in range(amountOfTokens):
            currentToken = self.tokens[index]

            print(currentToken)

            if utils.Utils.isNumber(currentToken):
                self.outputQueue.append(currentToken)

            if utils.Utils.isFunction(currentToken):
                self.operatorStack.append(currentToken)

            if utils.Utils.isOperator(currentToken):
                while self.operatorStack and not utils.Utils.isLeftParenthesis(self.operatorStack[-1]) and (utils.Utils.isGreaterPrecedence(self.operatorStack[-1], currentToken) or (utils.Utils.isEqualPrecedence(self.operatorStack[-1], currentToken) and utils.Utils.isLeftAssociative(currentToken))):
                    self.outputQueue.append(self.operatorStack.pop())

                self.operatorStack.append(currentToken)
             
            if utils.Utils.isComma(currentToken):
                while self.operatorStack and not utils.Utils.isLeftParenthesis(self.operatorStack[-1]):
                    self.outputQueue.append(self.operatorStack.pop())

            if utils.Utils.isLeftParenthesis(currentToken):
                self.operatorStack.append(currentToken)

            if utils.Utils.isRightParenthesis(currentToken):
                while self.operatorStack and not utils.Utils.isLeftParenthesis(self.operatorStack[-1]):
                    self.outputQueue.append(self.operatorStack.pop())

                self.operatorStack.pop()

                if self.operatorStack and utils.Utils.isFunction(self.operatorStack[-1]):
                    self.outputQueue.append(self.operatorStack.pop())

        while self.operatorStack:
            if not utils.Utils.isLeftParenthesis(self.operatorStack[-1]):
                self.outputQueue.append(self.operatorStack.pop())

        return self.outputQueue

print(Parser('sin(3) + 2 * 3 (1 - 5) + cos(12)').tokens)